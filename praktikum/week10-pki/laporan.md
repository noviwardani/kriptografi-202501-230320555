# Laporan Praktikum Kriptografi
Minggu ke-: 10  
Topik: [Public Key Infrastructure (PKI & Certificate Authority)]  
Nama: [Novi Ari Wardani]  
NIM: [230320555]  
Kelas: [5DSRA]  


## 1. Tujuan
(Tuliskan tujuan pembelajaran praktikum sesuai modul.)

1. Membuat sertifikat digital sederhana.
2. Menjelaskan peran Certificate Authority (CA) dalam sistem PKI.
3. Mengevaluasi fungsi PKI dalam komunikasi aman (contoh: HTTPS, TLS).


## 2. Dasar Teori
(Ringkas teori relevan (cukup 2–3 paragraf).  

Sertifikat digital merupakan dokumen elektronik yang berfungsi untuk mengikat identitas suatu entitas dengan kunci publiknya menggunakan teknik kriptografi kunci publik. Sertifikat digital sederhana dapat dibuat dengan cara membangkitkan pasangan kunci publik dan privat, kemudian menandatangani informasi identitas dan kunci publik tersebut menggunakan tanda tangan digital. Sertifikat ini memungkinkan pihak lain untuk mengenali identitas pemilik kunci publik dan menjadi dasar kepercayaan dalam proses komunikasi aman.

Certificate Authority (CA) berperan sebagai pihak tepercaya dalam sistem Public Key Infrastructure (PKI) yang bertugas memverifikasi identitas pemilik sertifikat sebelum menerbitkannya. CA menandatangani sertifikat digital menggunakan kunci privatnya sehingga keaslian sertifikat dapat diverifikasi menggunakan kunci publik CA. Dengan adanya CA, pengguna tidak perlu saling mengenal secara langsung, karena kepercayaan dibangun melalui otoritas pusat yang diakui bersama.

Public Key Infrastructure (PKI) berfungsi sebagai kerangka kerja yang mengatur pembuatan, distribusi, validasi, dan pencabutan sertifikat digital untuk menjamin keamanan komunikasi. PKI digunakan secara luas pada protokol seperti HTTPS dan TLS untuk memastikan autentikasi server, menjaga kerahasiaan data melalui enkripsi, serta menjamin integritas informasi yang dikirimkan. Dengan demikian, PKI memainkan peran penting dalam menciptakan komunikasi yang aman dan terpercaya di jaringan modern.

## 3. Alat dan Bahan
(- Python 3.x  
- Visual Studio Code / editor lain  
- Git dan akun GitHub  
- Library tambahan (misalnya pycryptodome, jika diperlukan)  )

---

## 4. Langkah Percobaan
(Tuliskan langkah yang dilakukan sesuai instruksi.  
Contoh format:

Langkah 1 — Membuat Sertifikat Digital (Root CA + CSR + Sertifikat Server)

    . Install library yang dipakai program pip install cryptography
    . Buat file program:
        1.Buat file: pubkey_infrastruktur.py
        2.Isi dengan source code yang sudah dibuat (versi CA + CSR + signing).
    . Jalankan program untuk generate semua komponen PKI
    . python pubkey_infrastruktur.py --cn localhost --san  ocalhost --outdir artifacts

Pastikan output file terbentuk di folder artifacts/ :
    . artifacts/ca_key.pem → private key Root CA
    . artifacts/ca_cert.pem → sertifikat Root CA (self-signed)
    . artifacts/server_key.pem → private key server
    . artifacts/server.csr.pem → CSR server (permintaan sertifikat)
    . artifacts/server_cert.pem → sertifikat server (ditandatangani CA)
    . artifacts/server_chain.pem → gabungan server cert + CA cert

Langkah 2 — Memverifikasi Sertifikat Verifikasi dilakukan dua lapis internal dan external

    Verifikasi internal dari program

    . Saat program selesai, bagian “Verifikasi Internal” akan tampil dan mengecek:
    . Signature valid: tanda tangan sertifikat server cocok jika diverifikasi pakai public key CA
    . Issuer cocok: issuer server cert sama dengan subject CA
    . Masa berlaku valid: tanggal sekarang masih dalam rentang validitas sertifikat    Yang tampil di output:
    . Signature valid (CA -> Server Cert) : True
    . Issuer cocok dengan Subject CA : True
    . Masa berlaku valid saat ini : True

Verifikasi eksternal pakai OpenSSL Ini simulasi cara tool nyata memvalidasi chain:

      "C:\Program Files\Git\usr\bin\openssl.exe" overify -CAfile artifacts/ca_cert.pem artifacts/server_cert.pem  

  Kalau benar, hasilnya : artifacts/server_cert.pem: OK
    . untuk lihat detail sertifikat server
      "C:\Program Files\Git\usr\bin\openssl.exe" x509 -in artifacts/server_cert.pem -noout -text 

Langkah 3 — Analisis PKI (Menghubungkan ke HTTPS/TLS) Di langkah ini menjelaskan hubungan hasil praktikum dengan dunia nyata

    . Hubungkan ke proses TLS/HTTPS:
        . Server mengirim server_cert.pem saat handshake TLS.
        . Browser/klien memverifikasi:
            . signature sertifikat server valid
            . issuer dan chain menuju CA tepercaya
            . domain cocok dengan SAN (contoh: example.local, localhost)
            . sertifikat belum expired.

    . Simulasikan “rantai kepercayaan”:
        . ca_cert.pem adalah anchor kepercayaan (root).
        . server_cert.pem dipercaya karena ditandatangani CA.
        . server_chain.pem itu versi praktis yang sering dipakai untuk mengirim chain.

Browser memverifikasi HTTPS dengan mengecek chain of trust ke CA tepercaya (trust store), memvalidasi tanda tangan digital, mencocokkan domain dengan SAN, dan memastikan masa berlaku (kadang juga cek revoke via OCSP/CRL).

Jika CA palsu menerbitkan sertifikat: kalau CA itu tidak dipercaya, browser akan memberi peringatan/blok. Kalau CA itu berhasil dipercaya (dikompromi/masuk trust store), sertifikat bisa terlihat valid dan MITM bisa terjadi tanpa warning.

PKI penting karena memberi jaminan identitas (server benar), mendukung TLS/HTTPS, dan membantu mencegah penyadapan/MITM pada transaksi online.


## 5. Source Code
(Salin kode program utama yang dibuat atau dimodifikasi.  
Gunakan blok kode:

import argparse
from pathlib import Path
from datetime import datetime, timedelta, timezone

from cryptography import x509
from cryptography.x509.oid import NameOID, ExtendedKeyUsageOID
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import rsa, padding


def utc_now():
    return datetime.now(timezone.utc)


def ensure_utc(dt: datetime) -> datetime:
    # cryptography kadang mengembalikan naive datetime (UTC). Kita rapikan biar konsisten.
    if dt.tzinfo is None:
        return dt.replace(tzinfo=timezone.utc)
    return dt


def build_name(country: str, org: str, common_name: str) -> x509.Name:
    return x509.Name(
        [
            x509.NameAttribute(NameOID.COUNTRY_NAME, country),
            x509.NameAttribute(NameOID.ORGANIZATION_NAME, org),
            x509.NameAttribute(NameOID.COMMON_NAME, common_name),
        ]
    )


def save_pem(path: Path, data: bytes):
    path.write_bytes(data)


def gen_rsa_key(bits: int = 2048) -> rsa.RSAPrivateKey:
    return rsa.generate_private_key(public_exponent=65537, key_size=bits)


def pem_private_key(key: rsa.RSAPrivateKey) -> bytes:
    # untuk praktikum: tanpa password biar gampang diuji
    return key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.TraditionalOpenSSL,
        encryption_algorithm=serialization.NoEncryption(),
    )


def pem_cert(cert: x509.Certificate) -> bytes:
    return cert.public_bytes(serialization.Encoding.PEM)


def pem_csr(csr: x509.CertificateSigningRequest) -> bytes:
    return csr.public_bytes(serialization.Encoding.PEM)


def make_root_ca(country: str, org: str, ca_cn: str, days: int = 3650):
    ca_key = gen_rsa_key(2048)
    subject = issuer = build_name(country, org, ca_cn)

    now = utc_now()
    builder = (
        x509.CertificateBuilder()
        .subject_name(subject)
        .issuer_name(issuer)
        .public_key(ca_key.public_key())
        .serial_number(x509.random_serial_number())
        .not_valid_before(now - timedelta(minutes=1))
        .not_valid_after(now + timedelta(days=days))
        .add_extension(x509.BasicConstraints(ca=True, path_length=0), critical=True)
        .add_extension(
            x509.KeyUsage(
                digital_signature=True,
                key_encipherment=False,
                content_commitment=False,
                data_encipherment=False,
                key_agreement=False,
                key_cert_sign=True,
                crl_sign=True,
                encipher_only=False,
                decipher_only=False,
            ),
            critical=True,
        )
        .add_extension(x509.SubjectKeyIdentifier.from_public_key(ca_key.public_key()), critical=False)
    )

    ca_cert = builder.sign(private_key=ca_key, algorithm=hashes.SHA256())
    return ca_key, ca_cert


def make_server_csr(country: str, org: str, server_cn: str, sans: list[str]):
    server_key = gen_rsa_key(2048)
    subject = build_name(country, org, server_cn)

    san_list = [x509.DNSName(name.strip()) for name in sans if name.strip()]
    csr_builder = x509.CertificateSigningRequestBuilder().subject_name(subject)

    if san_list:
        csr_builder = csr_builder.add_extension(x509.SubjectAlternativeName(san_list), critical=False)

    csr = csr_builder.sign(private_key=server_key, algorithm=hashes.SHA256())
    return server_key, csr


def sign_server_cert(
    ca_key: rsa.RSAPrivateKey,
    ca_cert: x509.Certificate,
    csr: x509.CertificateSigningRequest,
    days: int = 365,
):
    now = utc_now()

    # Ambil SAN dari CSR jika ada
    try:
        san_ext = csr.extensions.get_extension_for_class(x509.SubjectAlternativeName).value
    except x509.ExtensionNotFound:
        san_ext = None

    builder = (
        x509.CertificateBuilder()
        .subject_name(csr.subject)
        .issuer_name(ca_cert.subject)
        .public_key(csr.public_key())
        .serial_number(x509.random_serial_number())
        .not_valid_before(now - timedelta(minutes=1))
        .not_valid_after(now + timedelta(days=days))
        .add_extension(x509.BasicConstraints(ca=False, path_length=None), critical=True)
        .add_extension(
            x509.KeyUsage(
                digital_signature=True,
                key_encipherment=True,
                content_commitment=False,
                data_encipherment=False,
                key_agreement=False,
                key_cert_sign=False,
                crl_sign=False,
                encipher_only=False,
                decipher_only=False,
            ),
            critical=True,
        )
        .add_extension(x509.ExtendedKeyUsage([ExtendedKeyUsageOID.SERVER_AUTH]), critical=False)
        .add_extension(x509.SubjectKeyIdentifier.from_public_key(csr.public_key()), critical=False)
        .add_extension(x509.AuthorityKeyIdentifier.from_issuer_public_key(ca_key.public_key()), critical=False)
    )

    if san_ext is not None:
        builder = builder.add_extension(san_ext, critical=False)

    server_cert = builder.sign(private_key=ca_key, algorithm=hashes.SHA256())
    return server_cert


def verify_signature(issuer_cert: x509.Certificate, leaf_cert: x509.Certificate) -> bool:
    pub = issuer_cert.public_key()
    try:
        pub.verify(
            leaf_cert.signature,
            leaf_cert.tbs_certificate_bytes,
            padding.PKCS1v15(),
            leaf_cert.signature_hash_algorithm,
        )
        return True
    except Exception:
        return False


def print_summary(ca_cert: x509.Certificate, server_cert: x509.Certificate):
    ca_fp = ca_cert.fingerprint(hashes.SHA256()).hex()
    srv_fp = server_cert.fingerprint(hashes.SHA256()).hex()

    nb = ensure_utc(server_cert.not_valid_before_utc)
    na = ensure_utc(server_cert.not_valid_after_utc)

    print("=== Ringkasan PKI Simulation ===")
    print(f"CA Subject   : {ca_cert.subject.rfc4514_string()}")
    print(f"CA Issuer    : {ca_cert.issuer.rfc4514_string()} (self-signed)")
    print(f"CA Fingerprint (SHA-256): {ca_fp}")
    print("")
    print(f"Server Subject: {server_cert.subject.rfc4514_string()}")
    print(f"Server Issuer : {server_cert.issuer.rfc4514_string()} (ditandatangani CA)")
    print(f"Valid From    : {nb.isoformat()}")
    print(f"Valid Until   : {na.isoformat()}")
    print(f"Server Fingerprint (SHA-256): {srv_fp}")

    try:
        san = server_cert.extensions.get_extension_for_class(x509.SubjectAlternativeName).value
        dns_names = [x.value for x in san]
        print(f"SAN (DNS)     : {', '.join(dns_names)}")
    except x509.ExtensionNotFound:
        print("SAN (DNS)     : (tidak ada)")

    print("")


def main():
    parser = argparse.ArgumentParser(
        description="Simulasi PKI: Root CA -> tanda tangan CSR server -> verifikasi sertifikat."
    )
    parser.add_argument("--country", default="ID", help="Kode negara (default: ID)")
    parser.add_argument("--org", default="UPB Kriptografi Lab", help="Nama organisasi (default: UPB Kriptografi Lab)")
    parser.add_argument("--ca-cn", default="UPB Root CA", help="Common Name untuk CA (default: UPB Root CA)")
    parser.add_argument("--cn", required=True, help="Common Name untuk server certificate (contoh: example.local)")
    parser.add_argument(
        "--san",
        default="",
        help="Subject Alternative Names dipisah koma (contoh: example.local,localhost)",
    )
    parser.add_argument("--outdir", default="artifacts", help="Folder output (default: artifacts)")
    args = parser.parse_args()

    outdir = Path(args.outdir)
    outdir.mkdir(parents=True, exist_ok=True)

    sans = [s.strip() for s in args.san.split(",")] if args.san else []

    # 1) Buat Root CA
    ca_key, ca_cert = make_root_ca(args.country, args.org, args.ca_cn)

    # 2) Buat CSR server
    server_key, csr = make_server_csr(args.country, args.org, args.cn, sans)

    # 3) CA tanda tangan CSR jadi server certificate
    server_cert = sign_server_cert(ca_key, ca_cert, csr)

    # 4) Simpan file output
    save_pem(outdir / "ca_key.pem", pem_private_key(ca_key))
    save_pem(outdir / "ca_cert.pem", pem_cert(ca_cert))

    save_pem(outdir / "server_key.pem", pem_private_key(server_key))
    save_pem(outdir / "server.csr.pem", pem_csr(csr))
    save_pem(outdir / "server_cert.pem", pem_cert(server_cert))

    # chain (server cert + CA cert)
    save_pem(outdir / "server_chain.pem", pem_cert(server_cert) + pem_cert(ca_cert))

    # 5) Verifikasi sederhana (signature + waktu berlaku + issuer match)
    sig_ok = verify_signature(ca_cert, server_cert)

    now = utc_now()
    nb = ensure_utc(server_cert.not_valid_before_utc)
    na = ensure_utc(server_cert.not_valid_after_utc)
    time_ok = (nb <= now <= na)

    issuer_ok = (server_cert.issuer == ca_cert.subject)

    print_summary(ca_cert, server_cert)
    print("=== Verifikasi Internal ===")
    print(f"Signature valid (CA -> Server Cert) : {sig_ok}")
    print(f"Issuer cocok dengan Subject CA      : {issuer_ok}")
    print(f"Masa berlaku valid saat ini         : {time_ok}")
    print("")
    print("=== Output Files ===")
    for p in [
        "ca_key.pem",
        "ca_cert.pem",
        "server_key.pem",
        "server.csr.pem",
        "server_cert.pem",
        "server_chain.pem",
    ]:
        print(f"- {outdir / p}")
    print("")
    print("Selesai. Kalau OpenSSL verify gagal, biasanya karena file CA salah atau waktu sistem kacau.")


if __name__ == "__main__":
    main()



---

## 6. Hasil dan Pembahasan
(- Lampirkan screenshot hasil eksekusi program (taruh di folder `screenshots/`).  
- Berikan tabel atau ringkasan hasil uji jika diperlukan.  
- Jelaskan apakah hasil sesuai ekspektasi.  
- Bahas error (jika ada) dan solusinya. 

Hasil eksekusi program Caesar Cipher:

![Hasil Eksekusi](screenshots/output.png)
![Hasil Input](screenshots/input.png)
![Hasil Output](screenshots/output.png)
)

---

## 7. Jawaban Pertanyaan
(Jawab pertanyaan diskusi yang diberikan pada modul.  
- Pertanyaan 1: 

Fungsi utama Certificate Authority (CA) adalah sebagai pihak tepercaya yang memverifikasi identitas pemilik sertifikat digital dan menerbitkan sertifikat yang mengaitkan identitas tersebut dengan kunci publik. CA menandatangani sertifikat menggunakan kunci privatnya sehingga pihak lain dapat memverifikasi keaslian sertifikat dan mempercayai kunci publik yang digunakan dalam komunikasi.

- Pertanyaan 2: 

Fungsi utama Certificate Authority (CA) adalah sebagai pihak tepercaya yang memverifikasi identitas pemilik sertifikat digital dan menerbitkan sertifikat yang mengaitkan identitas tersebut dengan kunci publik. CA menandatangani sertifikat menggunakan kunci privatnya sehingga pihak lain dapat memverifikasi keaslian sertifikat dan mempercayai kunci publik yang digunakan dalam komunikasi.

- Pertanyaan 3 : 

PKI mencegah serangan MITM dalam komunikasi TLS/HTTPS dengan memastikan bahwa sertifikat server diverifikasi oleh CA yang tepercaya sebelum koneksi aman dibuat. Proses verifikasi ini menjamin bahwa kunci publik yang digunakan benar-benar milik server yang sah, sehingga penyerang tidak dapat menyamar atau mengganti kunci publik tanpa terdeteksi.

)


## 8. Kesimpulan
(Tuliskan kesimpulan singkat (2–3 kalimat) berdasarkan percobaan.  )

Berdasarkan seluruh pembahasan, sertifikat digital dan Certificate Authority (CA) merupakan komponen utama dalam sistem Public Key Infrastructure (PKI) untuk membangun kepercayaan pada komunikasi berbasis kriptografi kunci publik. PKI memungkinkan autentikasi, kerahasiaan, dan integritas data dalam protokol keamanan seperti TLS/HTTPS serta mencegah serangan Man-in-the-Middle melalui verifikasi sertifikat. Dengan demikian, penggunaan PKI dan CA yang tepercaya menjadi faktor penting dalam menjamin keamanan komunikasi pada sistem dan jaringan modern.

## 9. Daftar Pustaka
(Cantumkan referensi yang digunakan.  
Contoh:  
- Katz, J., & Lindell, Y. *Introduction to Modern Cryptography*.  
- Stallings, W. *Cryptography and Network Security*.  )

---

## 10. Commit Log
(Tuliskan bukti commit Git yang relevan.  
Contoh:
```
commit week10 Public Key Infrastructure (PKI & Certificate Authority)
Author: Novi Ari Wardani <wardani101103@gmail.com>
Date:   2025-12-15

    week10-Public Key Infrastructure (PKI & Certificate Authority )
```
