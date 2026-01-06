# Laporan Praktikum Kriptografi
Minggu ke-: 6 
Topik: Cipher-Modern  
Nama: Novi Ari Wardani
NIM: 230320555 
Kelas: 5DSRA  

---

## 1. Tujuan
(Tuliskan tujuan pembelajaran praktikum sesuai modul.)

1. Mengimplementasikan algoritma DES untuk blok data sederhana.
2. Menerapkan algoritma AES dengan panjang kunci 128 bit.
3. Menjelaskan proses pembangkitan kunci publik dan privat pada algoritma RSA.

## 2. Dasar Teori
(Ringkas teori relevan (cukup 2–3 paragraf).  
Contoh: definisi cipher klasik, konsep modular aritmetika, dll.  )

Algoritma DES (Data Encryption Standard) adalah algoritma kriptografi simetris yang mengenkripsi data dalam blok 64 bit menggunakan kunci 56 bit. Proses enkripsi dilakukan melalui 16 putaran dengan teknik substitusi dan permutasi. DES relatif mudah diimplementasikan pada blok data sederhana, namun saat ini sudah dianggap kurang aman karena panjang kuncinya kecil.

Algoritma AES (Advanced Encryption Standard) dengan panjang kunci 128 bit juga merupakan algoritma simetris yang bekerja pada blok data 128 bit. AES melakukan proses enkripsi melalui beberapa tahap transformasi seperti substitusi, pergeseran baris, pencampuran kolom, dan penambahan kunci. AES lebih cepat dan aman dibandingkan DES sehingga banyak digunakan pada sistem keamanan modern.

Algoritma RSA merupakan algoritma kriptografi asimetris yang menggunakan kunci publik dan kunci privat. Pembangkitan kunci RSA dilakukan dengan memilih dua bilangan prima besar dan menghitung nilai matematika tertentu untuk menghasilkan pasangan kunci. Kunci publik digunakan untuk enkripsi, sedangkan kunci privat digunakan untuk dekripsi, sehingga RSA cocok untuk keamanan data dan pertukaran kunci.

## 3. Alat dan Bahan
(- Python 3.x  
- Visual Studio Code / editor lain  
- Git dan akun GitHub  


## 4. Langkah Percobaan
(Tuliskan langkah yang dilakukan sesuai instruksi.  
Implementasi DES

. Enkripsi DES
    - Masukkan plaintext dan key.
    - Sesuaikan key menjadi 8 byte (ditambah 0 atau dipotong).
    - Ubah key dan plaintext ke bentuk byte.
    - Tambahkan padding agar panjang data kelipatan 8 byte.
    - Enkripsi data menggunakan DES mode ECB.
    - Ubah hasil enkripsi menjadi hex sebagai output.

. Deskripsi DES
     - mbil input berupa ciphertext dalam format hex dan key.
     - Sesuaikan key menjadi 8 byte (ditambah 0 jika kurang, dipotong jika lebih).
     - Ubah ciphertext hex menjadi byte.
     - Buat cipher DES menggunakan key yang sama dengan mode ECB.
     - Lakukan proses dekripsi untuk memperoleh data dalam bentuk byte.
     - Hapus padding PKCS#7 dari hasil dekripsi.
     - Ubah hasil byte menjadi string plaintext.
     - Kembalikan plaintext sebagai output.

. Enkripsi AES
     - Ambil input berupa plaintext dan key.
     - Pastikan panjang key 128 bit (16 byte).
     - Konversi plaintext dan key ke dalam b   bentuk byte.
     - Lakukan padding agar panjang plaintext menjadi kelipatan 16 byte.
     - Buat cipher AES menggunakan key yang telah ditentukan (misalnya mode ECB).
     - Lakukan proses enkripsi AES pada plaintext yang sudah dipadding.
     - Hasil enkripsi berupa ciphertext dalam bentuk byte.
     - Konversi ciphertext menjadi format hex sebagai output.

. Deskripsi AES
     - Masukkan plaintext dan key (128 bit).
     - Bagi plaintext menjadi blok 128 bit.
     - Lakukan AddRoundKey (XOR dengan kunci).
     - Lakukan proses SubBytes.
     - Lakukan ShiftRows.
     - Lakukan MixColumns.
     - Ulangi langkah 4–6 sampai 10 round.
     - Pada round terakhir, MixColumns dihilangkan.
     - Hasil akhir berupa ciphertext.

Implementasi RSA

. Enkripsi AES
     - Tentukan terlebih dahulu ukuran modulus (contohnya 64 bit).
     - Bagi ukuran tersebut menjadi dua bagian untuk p dan q (misalnya masing-masing 32 bit).
     - Bangkitkan bilangan prima p menggunakan uji probabilistik Miller–Rabin.
     - Bangkitkan bilangan prima q.
     - Hitung nilai n = p × q dan φ(n) = (p − 1)(q − 1).
     - Pilih nilai e = 65537 sebagai eksponen publik.
     - Pastikan gcd(e, φ(n)) = 1; jika tidak terpenuhi, ulangi proses pembangkitan prima.
     - Hitung kunci privat d sebagai invers modulo dari e terhadap φ(n).

. Deskripsi RSA
     - Terima input berupa gabungan IV dan ciphertext dalam bentuk byte.
     - Pisahkan data menjadi IV (16 byte pertama) dan ciphertext (sisa data).
     - Buat objek cipher AES menggunakan key dan IV yang sama.
     - Lakukan proses dekripsi terhadap ciphertext.
     - Hapus padding PKCS#7 dari hasil dekripsi.
     - Ubah hasil dekripsi dari byte ke string plaintext.


## 5. Source Code
(Salin kode program utama yang dibuat atau dimodifikasi.  
Gunakan blok kode:



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

DES, AES, dan RSA merupakan algoritma kriptografi yang memiliki perbedaan mendasar pada jenis kunci dan tingkat keamanannya.
DES (Data Encryption Standard) dan AES (Advanced Encryption Standard) termasuk algoritma kriptografi simetris, yaitu menggunakan satu kunci yang sama untuk proses enkripsi dan dekripsi. Perbedaannya terletak pada panjang kunci dan kekuatan keamanan. DES hanya memiliki panjang kunci 56 bit, sehingga rentan terhadap serangan brute force dan tidak lagi dianggap aman.

AES merupakan pengembangan algoritma simetris yang lebih modern dengan panjang kunci 128 bit, 192 bit, atau 256 bit, sehingga memiliki tingkat keamanan yang jauh lebih tinggi dan masih aman digunakan hingga saat ini.

Sementara itu, RSA merupakan algoritma kriptografi asimetris yang menggunakan dua kunci berbeda, yaitu kunci publik dan kunci privat. Keamanan RSA tidak bergantung pada panjang kunci yang pendek seperti DES, melainkan pada kesulitan matematis dalam memfaktorkan bilangan prima besar. Oleh karena itu, RSA umumnya menggunakan panjang kunci minimal 2048 bit.

- Pertanyaan 2: 

AES lebih banyak digunakan karena memiliki tingkat keamanan yang jauh lebih tinggi dibanding DES serta lebih efisien dan cepat. Selain itu, AES telah menjadi standar internasional dan digunakan secara luas dalam sistem keamanan modern, sedangkan DES sudah tidak direkomendasikan.

- Pertanyaan 3 :
RSA disebut algoritma asimetris karena menggunakan dua kunci berbeda, yaitu kunci publik dan kunci privat. Kunci dibangkitkan dengan memilih dua bilangan prima besar, menghitung nilai hasil perkaliannya, serta menentukan pasangan eksponen publik dan privat. Keamanan RSA bergantung pada sulitnya memfaktorkan bilangan besar tersebut.
---

## 8. Kesimpulan
(Tuliskan kesimpulan singkat (2–3 kalimat) berdasarkan percobaan.  )

DES, AES, dan RSA memiliki perbedaan mendasar pada jenis kunci dan tingkat keamanannya, di mana DES dan AES bersifat simetris sedangkan RSA bersifat asimetris. DES sudah tidak aman karena panjang kuncinya pendek, sementara AES menawarkan keamanan dan efisiensi yang jauh lebih baik sehingga menjadi standar kriptografi modern. RSA digunakan terutama untuk pertukaran kunci dan keamanan komunikasi karena keamanannya bergantung pada kesulitan faktorisasi bilangan prima besar.

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
commit week6 Cipher-Modern 
Author: Novi Ari Wardani <wardani101103@gmail.com>
Date:   2025-11-20

    week2-Cipher-Modern : Implementasi AES, DES, RSA)
```
