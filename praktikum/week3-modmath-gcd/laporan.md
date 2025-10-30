# Laporan Praktikum Kriptografi
Minggu ke-: 3  
Topik: Modular Math 
Nama: Novi Ari Wardani 
NIM: 230320555 
Kelas: 5DSRA  

---

## 1. Tujuan
(Tuliskan tujuan pembelajaran praktikum sesuai modul.)

1. Menyelesaikan operasi aritmetika modular.  
2. Menentukan bilangan prima dan menghitung GCD (Greatest Common Divisor).  
3. Menerapkan logaritma diskrit sederhana dalam simulasi kriptografi

## 2. Dasar Teori

Operasi aritmetika modular adalah konsep matematika yang penting, terutama dalam kriptografi dan ilmu komputer. Contohnya, kita dapat menghitung hasil penjumlahan dua bilangan, seperti 17 dan 23, kemudian mencari sisa pembagiannya terhadap angka 5. Hasilnya adalah 0, yang menunjukkan bahwa penjumlahan tersebut habis dibagi oleh 5 jika dilihat dalam ruang lingkup modulo 5. Operasi ini membantu dalam mengelola perhitungan pada sistem yang memiliki batas tertentu.

Menentukan bilangan prima dan menghitung Greatest Common Divisor (GCD) juga merupakan hal fundamental dalam matematika dan kriptografi. Bilangan prima seperti 29 memiliki peran penting karena hanya bisa dibagi oleh 1 dan dirinya sendiri, yang membuatnya berguna dalam enkripsi. Sedangkan GCD, seperti yang dihitung antara 56 dan 98 dengan hasil 14, berguna untuk menemukan faktor bersama terbesar dari dua bilangan. Ini sangat membantu dalam menyederhanakan perhitungan dan memecahkan masalah terkait pembagian.

Logaritma diskrit adalah konsep yang digunakan khususnya dalam kriptografi untuk menemukan pangkat suatu bilangan dalam operasi modular. Contohnya, mencari nilai x dalam persamaan 3^x≡13mod"  " 17 dengan cara mencoba berbagai nilai x hingga persamaan terpenuhi. Dalam kasus ini, nilai x adalah 4. Konsep ini adalah dasar bagi berbagai algoritma keamanan yang memanfaatkan kesulitan logaritma diskrit untuk menjaga keamanan data.



## 3. Alat dan Bahan
(- Python 3.x  
- Visual Studio Code / editor lain  
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
- Pertanyaan 1: Peran aritmetika modular dalam kriptografi modern sangat penting karena digunakan sebagai dasar dalam berbagai algoritma kriptografi kunci publik dan simetris. Operasi aritmetika modular memungkinkan penghitungan dalam ruang terbatas yang aman dan efisien, seperti pada algoritma RSA dan Diffie-Hellman yang menggunakan eksponen modular untuk enkripsi dan dekripsi. Selain itu, aritmetika modular juga digunakan dalam kurva elips dan algoritma kunci simetris seperti AES, sehingga menjadi fondasi utama dalam menjaga keamanan data digital saat ini.
- Pertanyaan 2: Invers modular sangat penting dalam algoritma kunci publik seperti RSA karena digunakan untuk menghasilkan kunci privat dari kunci publik. Pada RSA, enkripsi dilakukan dengan eksponen modular dan dekripsi membutuhkan invers modular eksponen tersebut dalam bidang modulo bilangan prima atau hasil perkalian bilangan prima. Tanpa invers modular, proses dekripsi tidak bisa dilakukan secara matematis, sehingga fungsi invers modular adalah kunci agar pesan yang dienkripsi dapat kembali pada bentuk aslinya secara benar dan aman.
- Pernyataan 3: Tantangan utama dalam menyelesaikan logaritma diskrit untuk modulus besar adalah tingkat kesulitan komputasi yang sangat tinggi. Logaritma diskrit merupakan masalah matematis yang sulit diselesaikan secara efisien, karena tidak ada algoritma yang dapat menyelesaikan masalah ini secara cepat untuk modulus yang sangat besar dalam praktik kriptografi. Kesulitan ini menjadi dasar keamanan metode enkripsi yang menggunakan logaritma diskrit, seperti Diffie-Hellman dan kriptografi kurva elips, karena pemecahan logaritma diskrit secara brute force membutuhkan waktu yang tidak praktis dalam skala besar.


## 8. Kesimpulan
(Tuliskan kesimpulan singkat (2–3 kalimat) berdasarkan percobaan.  )

Praktikum ini mengilustrasikan kemampuan mengubah teori matematika modular dan logaritma diskrit menjadi kode yang dapat dijalankan. Melalui penerapan algoritma Euclidean untuk GCD, konsep abstrak tersebut diwujudkan dalam penyelesaian masalah nyata. Keberhasilan eksekusi program sesuai harapan menegaskan pemahaman praktis terhadap prinsip dasar kriptografi.



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
commit abcweek3-modmath-gcd
Author: Novi Ari Wardani <wardani101103@gmail.com>
Date:   2025-10-30

    week2-modmath-gdc: Modular Math
```
