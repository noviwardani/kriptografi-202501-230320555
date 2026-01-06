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
- Pertanyaan 1: 

Diffie–Hellman memungkinkan pertukaran kunci di saluran publik karena kunci rahasia tidak pernah dikirimkan secara langsung, melainkan dihasilkan secara mandiri oleh masing-masing pihak menggunakan kunci privat dan parameter publik, serta dilindungi oleh kesulitan matematis masalah logaritma diskrit yang sangat sulit dipecahkan oleh penyerang.

- Pertanyaan 2: 

Kelemahan utama protokol Diffie–Hellman murni adalah tidak adanya mekanisme autentikasi identitas, sehingga protokol ini rentan terhadap serangan Man-in-the-Middle di mana penyerang dapat menyamar sebagai pihak yang sah tanpa terdeteksi.

- Pertanyaan 3 : 

Serangan Man-in-the-Middle pada Diffie–Hellman dapat dicegah dengan menambahkan mekanisme autentikasi seperti tanda tangan digital, sertifikat digital (PKI), atau menggunakan protokol terautentikasi seperti TLS dengan DHE/ECDHE yang memastikan keaslian identitas pihak yang berkomunikasi.
)


## 8. Kesimpulan
(Tuliskan kesimpulan singkat (2–3 kalimat) berdasarkan percobaan.  )

Berdasarkan percobaan yang dilakukan, protokol Diffie–Hellman terbukti mampu menghasilkan kunci rahasia bersama meskipun proses pertukaran dilakukan melalui saluran komunikasi publik, karena keamanan algoritma bergantung pada kesulitan masalah logaritma diskrit. Namun, simulasi juga menunjukkan bahwa Diffie–Hellman murni memiliki kelemahan serius, yaitu tidak adanya mekanisme autentikasi sehingga rentan terhadap serangan Man-in-the-Middle. Oleh karena itu, untuk menjamin keamanan komunikasi, protokol Diffie–Hellman harus dikombinasikan dengan mekanisme autentikasi seperti tanda tangan digital atau sertifikat digital agar pertukaran kunci benar-benar aman.

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
commit week7 Diffie-hellman 
Author: Novi Ari Wardani <ewardani101103@gmail.com>
Date:   2025-11-2022

    week7-Diffie-hellman: Key Exchange )
```
