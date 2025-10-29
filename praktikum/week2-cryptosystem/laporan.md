# Laporan Praktikum Kriptografi
Minggu ke-: 2 
Topik:cryptosystem  
Nama:Novi Ari Wardani  
NIM: 230320555 
Kelas: 5DSRA  



## 1. Tujuan
(Tuliskan tujuan pembelajaran praktikum sesuai modul.)
1.Mengidentifikasi komponen dasar kriptosistem (plaintext, ciphertext, kunci, algoritma).
2.Menggambarkan proses enkripsi dan dekripsi sederhana.
3.Mengklasifikasikan jenis kriptosistem (simetris dan asimetris).


## 2. Dasar Teori
(Ringkas teori relevan (cukup 2–3 paragraf).  
Contoh: definisi cipher klasik, konsep modular aritmetika, dll.  )

Kriptosistem secara umum diklasifikasikan menjadi dua jenis utama, yaitu kriptosistem simetris dan kriptosistem asimetris, berdasarkan cara penggunaan kunci dalam proses enkripsi dan dekripsi. Pada kriptosistem simetris, kunci yang digunakan untuk mengenkripsi dan mendekripsi pesan adalah sama. Artinya, baik pengirim maupun penerima pesan harus memiliki dan menjaga kerahasiaan kunci yang identik. Sistem ini cenderung lebih cepat dan efisien, serta cocok digunakan untuk mengenkripsi data dalam jumlah besar. Contoh algoritma simetris yang terkenal adalah AES (Advanced Encryption Standard) dan DES (Data Encryption Standard).

Sementara itu, kriptosistem asimetris menggunakan sepasang kunci yang berbeda, yaitu kunci publik dan kunci privat. Kunci publik digunakan untuk mengenkripsi pesan dan dapat dibagikan secara luas, sedangkan kunci privat digunakan untuk mendekripsi pesan dan harus dijaga kerahasiaannya oleh pemilik. Sistem ini lebih aman untuk pertukaran data melalui jaringan terbuka karena tidak memerlukan pengiriman kunci rahasia. Kriptosistem asimetris banyak digunakan dalam komunikasi digital modern, termasuk dalam protokol keamanan seperti SSL/TLS. Salah satu contoh algoritma asimetris paling terkenal adalah RSA (Rivest–Shamir–Adleman).


## 3. Alat dan Bahan
(- Python 3.x  
- Python  
- Visual Studio Code  
- Git dan akun Github


## 4. Langkah Percobaan
Langkah 1 — Membuat Skema Kriptosistem

Buat diagram sederhana (pakai draw.io)
Simpan diagram di folder screenshots/diagram_kriptosistem.png.
Lampirkan ke laporan
Langkah 2 — Implementasi Program Sederhana

Tulis program Python untuk simulasi enkripsi & dekripsi menggunakan substitusi sederhana menggunakan vigenere
Langkah 3 — Klasifikasi Simetris & Asimetris

Tambahkan penjelasan di laporan mengenai perbedaan kriptografi simetris dan asimetris.
Sertakan minimal 1 contoh algoritma dari masing-masing:
Simetris → AES, DES
Asimetris → RSA, ECC


## 5. Source Code
(Salin kode program utama yang dibuat atau dimodifikasi.  
Gunakan blok kode:

def vigenere_enkripsi(plaintext, kunci):
    ciphertext = ""
    kunci = kunci.upper()
    kunci_index = 0
    
    for char in plaintext:
        if 'A' <= char.upper() <= 'Z':
            # Tentukan pergeseran
            shift = ord(kunci[kunci_index % len(kunci)]) - ord('A')
            
            # Tentukan base (A=0 atau a=0)
            base = ord('A') if char.isupper() else ord('a')
            
            # Enkripsi: (char_index + shift) mod 26
            enkripsi_char = chr((ord(char) - base + shift) % 26 + base)
            ciphertext += enkripsi_char
            
            # Pindah ke huruf kunci berikutnya
            kunci_index += 1
        else:
            # Karakter non-alfabet (spasi, tanda baca) tidak diubah
            ciphertext += char
            
    return ciphertext

def vigenere_dekripsi(ciphertext, kunci):
    plaintext = ""
    kunci = kunci.upper()
    kunci_index = 0
    
    for char in ciphertext:
        if 'A' <= char.upper() <= 'Z':
            # Tentukan pergeseran
            shift = ord(kunci[kunci_index % len(kunci)]) - ord('A')
            
            # Tentukan base (A=0 atau a=0)
            base = ord('A') if char.isupper() else ord('a')
            
            # Dekripsi: (char_index - shift) mod 26
            dekripsi_char = chr((ord(char) - base - shift) % 26 + base)
            plaintext += dekripsi_char
            
            # Pindah ke huruf kunci berikutnya
            kunci_index += 1
        else:
            # Karakter non-alfabet (spasi, tanda baca) tidak diubah
            plaintext += char
            
    return plaintext

# Contoh Penggunaan
teks_asli = "pesan"
kunci_vigenere = "kunci"
teks_terenkripsi = vigenere_enkripsi(teks_asli, kunci_vigenere)
teks_terdekripsi = vigenere_dekripsi(teks_terenkripsi, kunci_vigenere)

print(f"Plaintext: {teks_asli}")
print(f"Kunci: {kunci_vigenere}")
print(f"Ciphertext (Vigenere): {teks_terenkripsi}")
print(f"Decrypted Text: {teks_terdekripsi}")

## 6. Hasil dan Pembahasan
(- Lampirkan screenshot hasil eksekusi program (taruh di folder `screenshots/`).  
- Berikan tabel atau ringkasan hasil uji jika diperlukan.  
- Jelaskan apakah hasil sesuai ekspektasi.  
- Bahas error (jika ada) dan solusinya. 

Diagram /skema kriptosistem dasar:



## 7. Jawaban Pertanyaan
(Jawab pertanyaan diskusi yang diberikan pada modul.  
- Pertanyaan 1: plaintext,chipertext,algoritma enkripsi,algoritma dekripsi,key  
- Pertanyaan 2: Keunggulan dari symmetric key cryptography adalah proses enkripsi dan dekripsinya relatif cepat dibandingkan dengan jenis kriptografi lainnya. Namun, kekurangan dari metode ini adalah distribusi kunci yang aman dikarenakan kriptografi simetris memiliki kunci enkripsi dan dekripsi yang sama maka penggunaan
- Pertanyaan 3 : karena saat distribusi kunci terdapat Penyadap (eavesdropper), penyadap adalah orang yang mencoba menangkap pesan selama ditransmisikan. Tujuan penyadap adalah untuk mendapatkan informasi sebanyakbanyaknya mengenai sistem kriptografi yang digunakan untuk berkomunikasi dengan maksud untuk memecahkan cipherteks dikarenakan kriptografi simetris memiliki kunci enkripsi dan dekripsi yang sama maka penggunaan kriptografi simetris rentan terhadap kebocoran apabila si penyadap mengetahui kuncinya. )


## 8. Kesimpulan
(Tuliskan kesimpulan singkat (2–3 kalimat) berdasarkan percobaan.  )

Praktikum ini berhasil mengidentifikasi komponen utama dari suatu kriptosistem serta melakukan simulasi proses enkripsi dan dekripsi sederhana menggunakan Vigenere Cipher, yang termasuk dalam kategori kriptografi simetris. Perbedaan pokok antara kriptografi simetris (lebih cepat, menggunakan satu kunci, namun menghadapi tantangan dalam distribusi kunci) dan kriptografi asimetris (lebih lambat, menggunakan pasangan kunci publik dan privat, serta lebih unggul dalam hal autentikasi) telah berhasil dipahami. Kesimpulannya, pemilihan jenis kriptografi harus mempertimbangkan kebutuhan akan kecepatan dan tingkat keamanan dalam pertukaran kunci

## 9. Daftar Pustaka
(Cantumkan referensi yang digunakan.  
Contoh:  
- Katz, J., & Lindell, Y. *Introduction to Modern Cryptography*.  
- Stallings, W. *Cryptography and Network Security*.  )



## 10. Commit Log
(Tuliskan bukti commit Git yang relevan.  
Contoh:

commit abc12345
Author: Nama Mahasiswa <email>
Date:   2025-09-20

    week2-cryptosystem: implementasi Caesar Cipher dan laporan )

