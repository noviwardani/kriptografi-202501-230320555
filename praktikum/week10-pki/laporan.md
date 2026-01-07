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

```python
# contoh potongan kode
def encrypt(text, key):
    return ...
```
)

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
