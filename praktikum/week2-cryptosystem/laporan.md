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
- Visual Studio Code / editor lain  
- Git dan akun GitHub  
- Library tambahan 


## 4. Langkah Percobaan
(Tuliskan langkah yang dilakukan sesuai instruksi.  
Contoh format:
1. Membuat file `caesar_cipher.py` di folder `praktikum/week2-cryptosystem/src/`.
2. Menyalin kode program dari panduan praktikum.
3. Menjalankan program dengan perintah `python caesar_cipher.py`.)

---

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
- Pertanyaan 1: …  
- Pertanyaan 2: …  
)
---

## 8. Kesimpulan
(Tuliskan kesimpulan singkat (2–3 kalimat) berdasarkan percobaan.  )

---

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
commit abc12345
Author: Nama Mahasiswa <email>
Date:   2025-09-20

    week2-cryptosystem: implementasi Caesar Cipher dan laporan )
```
