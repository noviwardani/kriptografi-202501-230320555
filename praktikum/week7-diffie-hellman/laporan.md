# Laporan Praktikum Kriptografi
Minggu ke-: 7  
Topik: Diffie-hellman 
Nama: Novi Ari Wardani 
NIM:230320555  
Kelas: 5DSRA 


## 1. Tujuan
(Tuliskan tujuan pembelajaran praktikum sesuai modul.)

1. Melakukan simulasi protokol Diffie-Hellman untuk pertukaran kunci publik.
2. Menjelaskan mekanisme pertukaran kunci rahasia menggunakan bilangan prima dan logaritma diskrit.
3. Menganalisis potensi serangan pada protokol Diffie-Hellman (termasuk serangan Man-in-the-Middle / MITM).

## 2. Dasar Teori
(Ringkas teori relevan (cukup 2–3 paragraf).  

Diffie–Hellman merupakan protokol kriptografi yang digunakan untuk melakukan pertukaran kunci rahasia melalui jaringan yang tidak aman. Protokol ini memungkinkan dua pihak untuk membentuk kunci bersama tanpa harus mengirimkan kunci rahasia tersebut secara langsung. Dengan demikian, komunikasi dapat tetap terjaga kerahasiaannya meskipun dilakukan melalui media publik.
Mekanisme Diffie–Hellman memanfaatkan bilangan prima, generator, dan operasi perpangkatan modulo untuk menghasilkan kunci publik dan kunci privat. Kunci publik dipertukarkan secara terbuka, sedangkan kunci privat tetap dirahasiakan oleh masing-masing pihak. Keamanan protokol ini bergantung pada sulitnya menyelesaikan masalah logaritma diskrit, sehingga pihak ketiga tidak dapat dengan mudah menebak kunci rahasia.
Meskipun aman secara matematis, Diffie–Hellman memiliki kelemahan karena tidak menyediakan autentikasi bawaan. Hal ini menyebabkan protokol rentan terhadap serangan Man-in-the-Middle, di mana penyerang dapat menyamar sebagai pihak komunikasi. Oleh karena itu, penerapan Diffie–Hellman dalam sistem nyata biasanya dikombinasikan dengan mekanisme autentikasi seperti sertifikat digital atau tanda tangan kriptografi.

## 3. Alat dan Bahan
(- Python 3.x  
- Visual Studio Code  
- Git dan akun GitHub  

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
