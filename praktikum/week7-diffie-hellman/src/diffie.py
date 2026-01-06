import random

def print_header(title):
    """Fungsi untuk mencetak header dengan format yang rapi"""
    print("\n" + "="*60)
    print(f"  {title}")
    print("="*60)

def diffie_hellman_normal():
    """Simulasi Diffie-Hellman normal tanpa serangan"""
    print_header("SIMULASI DIFFIE-HELLMAN NORMAL")
    
    # Langkah 1: Parameter publik (disepakati bersama)
    p = 23  # bilangan prima
    g = 5   # generator
    
    print(f"\n[1] Parameter Publik:")
    print(f"    Bilangan Prima (p) = {p}")
    print(f"    Generator (g)      = {g}")
    
    # Langkah 2: Generate private key untuk Alice dan Bob
    a = random.randint(1, p-1)  # secret Alice
    b = random.randint(1, p-1)  # secret Bob
    
    print(f"\n[2] Private Key (Rahasia):")
    print(f"    Alice (a)          = {a}")
    print(f"    Bob (b)            = {b}")
    
    # Langkah 3: Hitung public key
    A = pow(g, a, p)  # A = g^a mod p
    B = pow(g, b, p)  # B = g^b mod p
    
    print(f"\n[3] Public Key (Dikirim melalui saluran publik):")
    print(f"    Alice menghitung: A = {g}^{a} mod {p} = {A}")
    print(f"    Bob menghitung:   B = {g}^{b} mod {p} = {B}")
    
    # Langkah 4: Pertukaran public key
    print(f"\n[4] Pertukaran Public Key:")
    print(f"    Alice mengirim A = {A} ke Bob")
    print(f"    Bob mengirim B = {B} ke Alice")
    
    # Langkah 5: Hitung shared secret
    shared_secret_A = pow(B, a, p)  # Alice: s = B^a mod p
    shared_secret_B = pow(A, b, p)  # Bob: s = A^b mod p
    
    print(f"\n[5] Perhitungan Shared Secret:")
    print(f"    Alice menghitung: s = B^a mod p = {B}^{a} mod {p} = {shared_secret_A}")
    print(f"    Bob menghitung:   s = A^b mod p = {A}^{b} mod {p} = {shared_secret_B}")
    
    # Verifikasi
    print(f"\n[6] HASIL:")
    print(f"    Kunci bersama Alice: {shared_secret_A}")
    print(f"    Kunci bersama Bob:   {shared_secret_B}")
    
    if shared_secret_A == shared_secret_B:
        print(f"    ✓ SUKSES! Kedua pihak memiliki kunci yang sama.")
    else:
        print(f"    ✗ GAGAL! Kunci tidak sama.")
    
    return shared_secret_A, shared_secret_B


def diffie_hellman_mitm():
    """Simulasi serangan Man-in-the-Middle pada Diffie-Hellman"""
    print_header("SIMULASI SERANGAN MAN-IN-THE-MIDDLE (MITM)")
    
    # Langkah 1: Parameter publik
    p = 23
    g = 5
    
    print(f"\n[1] Parameter Publik:")
    print(f"    Bilangan Prima (p) = {p}")
    print(f"    Generator (g)      = {g}")
    
    # Langkah 2: Private key untuk Alice, Bob, dan Eve (attacker)
    a = random.randint(1, p-1)  # secret Alice
    b = random.randint(1, p-1)  # secret Bob
    e = random.randint(1, p-1)  # secret Eve (attacker)
    
    print(f"\n[2] Private Key:")
    print(f"    Alice (a)          = {a}")
    print(f"    Bob (b)            = {b}")
    print(f"    Eve/Attacker (e)   = {e}")
    
    # Langkah 3: Hitung public key
    A = pow(g, a, p)  # Public key Alice
    B = pow(g, b, p)  # Public key Bob
    E = pow(g, e, p)  # Public key Eve
    
    print(f"\n[3] Public Key:")
    print(f"    Alice: A = {g}^{a} mod {p} = {A}")
    print(f"    Bob:   B = {g}^{b} mod {p} = {B}")
    print(f"    Eve:   E = {g}^{e} mod {p} = {E}")
    
    # Langkah 4: SERANGAN! Eve mencegat dan mengganti public key
    print(f"\n[4] SERANGAN MITM:")
    print(f"    ⚠ Alice ingin mengirim A = {A} ke Bob")
    print(f"    ⚠ Eve MENCEGAT dan mengganti dengan E = {E}")
    print(f"    → Bob menerima E = {E} (bukan A = {A})")
    print()
    print(f"    ⚠ Bob ingin mengirim B = {B} ke Alice")
    print(f"    ⚠ Eve MENCEGAT dan mengganti dengan E = {E}")
    print(f"    → Alice menerima E = {E} (bukan B = {B})")
    
    # Langkah 5: Perhitungan shared secret
    # Alice menghitung dengan public key Eve (bukan Bob)
    shared_secret_Alice = pow(E, a, p)  # Alice: s = E^a mod p
    
    # Bob menghitung dengan public key Eve (bukan Alice)
    shared_secret_Bob = pow(E, b, p)    # Bob: s = E^b mod p
    
    # Eve menghitung dua kunci berbeda
    shared_secret_Eve_Alice = pow(A, e, p)  # Eve dengan Alice: s = A^e mod p
    shared_secret_Eve_Bob = pow(B, e, p)    # Eve dengan Bob: s = B^e mod p
    
    print(f"\n[5] Perhitungan Shared Secret:")
    print(f"    Alice menghitung: s = E^a mod p = {E}^{a} mod {p} = {shared_secret_Alice}")
    print(f"    Bob menghitung:   s = E^b mod p = {E}^{b} mod {p} = {shared_secret_Bob}")
    print(f"    Eve dengan Alice: s = A^e mod p = {A}^{e} mod {p} = {shared_secret_Eve_Alice}")
    print(f"    Eve dengan Bob:   s = B^e mod p = {B}^{e} mod {p} = {shared_secret_Eve_Bob}")
    
    # Hasil
    print(f"\n[6] HASIL SERANGAN:")
    print(f"    Kunci Alice:       {shared_secret_Alice}")
    print(f"    Kunci Bob:         {shared_secret_Bob}")
    print(f"    Kunci Eve-Alice:   {shared_secret_Eve_Alice}")
    print(f"    Kunci Eve-Bob:     {shared_secret_Eve_Bob}")
    
    print(f"\n    ⚠ ANALISIS:")
    if shared_secret_Alice == shared_secret_Eve_Alice:
        print(f"    ✓ Eve dapat mendekripsi pesan dari Alice (kunci sama)")
    if shared_secret_Bob == shared_secret_Eve_Bob:
        print(f"    ✓ Eve dapat mendekripsi pesan dari Bob (kunci sama)")
    if shared_secret_Alice != shared_secret_Bob:
        print(f"    ✗ Alice dan Bob memiliki kunci BERBEDA!")
        print(f"    ✗ Mereka tidak dapat berkomunikasi dengan benar")
    
    print(f"\n    💀 Eve berhasil melakukan MITM attack!")
    print(f"    💀 Eve dapat membaca dan memodifikasi semua pesan!")
    
    return {
        'alice': shared_secret_Alice,
        'bob': shared_secret_Bob,
        'eve_alice': shared_secret_Eve_Alice,
        'eve_bob': shared_secret_Eve_Bob
    }


def demonstrate_mitm_attack_flow():
    """Demonstrasi alur komunikasi dengan MITM"""
    print_header("ALUR KOMUNIKASI DENGAN MITM ATTACK")
    
    print("""
    SKENARIO: Alice ingin mengirim pesan "HELLO" ke Bob
    
    [Tanpa MITM - Normal]
    Alice --[enkripsi dengan kunci bersama]--> Bob
          Bob dapat dekripsi dengan kunci yang sama
    
    [Dengan MITM - Serangan]
    Alice --[enkripsi dengan kunci_Eve_Alice]--> Eve --[dekripsi]
                                                   |
                                                   | Eve baca pesan: "HELLO"
                                                   | Eve bisa ubah jadi: "HALLO"
                                                   |
    Eve --[enkripsi ulang dengan kunci_Eve_Bob]--> Bob --[dekripsi]
    
    DAMPAK:
    ✗ Bob menerima "HALLO" (bukan "HELLO")
    ✗ Alice dan Bob tidak tahu pesan sudah diubah
    ✗ Eve dapat membaca semua komunikasi
    ✗ Eve dapat memodifikasi pesan tanpa terdeteksi
    """)


def mitigasi_mitm():
    """Penjelasan cara mitigasi serangan MITM"""
    print_header("MITIGASI SERANGAN MITM")
    
    print("""
    CARA MENCEGAH SERANGAN MITM:
    
    1. AUTENTIKASI DENGAN SERTIFIKAT DIGITAL
       - Gunakan PKI (Public Key Infrastructure)
       - Verifikasi identitas dengan Certificate Authority (CA)
       - Contoh: TLS/SSL certificates
    
    2. DIGITAL SIGNATURE
       - Tandatangani public key dengan private key
       - Verifikasi signature sebelum pertukaran kunci
       - Pastikan public key berasal dari pihak yang benar
    
    3. PRE-SHARED SECRET (Out-of-Band Verification)
       - Verifikasi fingerprint melalui saluran terpisah
       - Contoh: PIN, QR code, phone call
       - WhatsApp: verifikasi security code
    
    4. STATION-TO-STATION (STS) PROTOCOL
       - Kombinasi Diffie-Hellman dengan digital signatures
       - Autentikasi mutual antara kedua pihak
       - Mencegah MITM attack
    
    5. PERFECT FORWARD SECRECY
       - Generate kunci baru setiap sesi
       - Jika satu kunci bocor, sesi lain tetap aman
       - Digunakan dalam TLS 1.3
    
    CONTOH IMPLEMENTASI NYATA:
    • HTTPS (TLS/SSL) = Diffie-Hellman + Certificates
    • SSH = Diffie-Hellman + Host key verification
    • Signal/WhatsApp = Extended Diffie-Hellman + Digital signatures
    • VPN (IPSec) = Diffie-Hellman + Pre-shared keys atau certificates
    """)


def main():
    
    # Simulasi 1: Diffie-Hellman Normal
    diffie_hellman_normal()
    
    input("\n\nTekan ENTER untuk melanjutkan ke simulasi MITM...")
    
    # Simulasi 2: Serangan MITM
    diffie_hellman_mitm()
    
    input("\n\nTekan ENTER untuk melihat alur serangan MITM...")
    
    # Demonstrasi alur MITM
    demonstrate_mitm_attack_flow()
    
    input("\n\nTekan ENTER untuk melihat cara mitigasi...")
    
    # Cara mitigasi
    mitigasi_mitm()
    
    print("\n" + "▓"*60)
    print("▓" + "  SIMULASI SELESAI".center(58) + "▓")
    print("▓"*60 + "\n")


if __name__ == "__main__":
    main()