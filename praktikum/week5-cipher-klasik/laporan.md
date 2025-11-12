# Laporan Praktikum Kriptografi
Minggu ke-: 5  
Topik: Cipher Klasik (Caesar, Vigenère, Transposisi)  
Nama: Novi Ari Wardani 
NIM: 230320555  
Kelas: 5DSRA  

---

## 1. Tujuan
(Tuliskan tujuan pembelajaran praktikum sesuai modul.)

1. Menerapkan algoritma Caesar Cipher untuk enkripsi dan dekripsi teks.
2. Menerapkan algoritma Vigenère Cipher dengan variasi kunci.
3. Mengimplementasikan algoritma transposisi sederhana.
4. Menjelaskan kelemahan algoritma kriptografi klasik.
---

## 2. Dasar Teori
(Ringkas teori relevan (cukup 2–3 paragraf).  

Kriptografi klasik merupakan metode enkripsi tertua yang banyak digunakan sebelum era komputerisasi. Algoritma ini biasanya menggunakan kunci simetris dan teknik sederhana seperti substitusi dan transposisi untuk mengubah pesan asli menjadi pesan terenkripsi. Misalnya, substitusi mengganti setiap huruf dalam pesan dengan huruf lain, sedangkan transposisi mengubah urutan huruf dalam pesan.

Contoh terkenal dari cipher klasik adalah Caesar Cipher, yang melakukan penggeseran posisi huruf dalam alfabet dengan sejumlah langkah tertentu. Meskipun sederhana, metode ini sudah cukup efektif pada masa lalu, namun mudah dipecahkan dengan analisis frekuensi atau brute force saat ini. Selain Caesar, ada juga cipher lain seperti Vigenere dan Hill cipher yang menggunakan variasi teknik penggantian dan pengacakan huruf.

Kelemahan utama kriptografi klasik adalah ruang kunci yang kecil dan algoritma yang relatif mudah dianalisis, membuatnya rentan terhadap serangan modern. Meskipun begitu, prinsip dasar cipher klasik menjadi landasan penting bagi pengembangan algoritma kriptografi modern yang lebih kompleks dan aman. Penggabungan teknik substitusi dan transposisi dalam cipher klasik juga menjadi inspirasi terciptanya product cipher atau super enkripsi yang kuat.

---

## 3. Alat dan Bahan
(- Python 3.x  
- Visual Studio Code   
- Git dan akun GitHub  
---

## 4. Langkah Percobaan
(Tuliskan langkah yang dilakukan sesuai instruksi.  
Contoh format:
1. Langkah 1 - Implementasi Caesar Cipher

  1. Mulai program Caesar_cipher.py.
  2. Minta pengguna memasukkan:
    - Teks yang akan dienkripsi atau didekripsi
    - Nilai shift (pergeseran huruf)
    - Mode (e untuk enkripsi, d untuk dekripsi)
  3. Jika mode = d, ubah shift menjadi negatif.
  4. Buat variabel kosong bernama hasil.
  5. Untuk setiap karakter dalam teks:
    - Jika huruf alfabet:
       . Tentukan nilai dasar ('A' atau 'a').
       . Geser posisi huruf dengan rumus:
         (kode_huruf + shift) mod 26
       . Ubah kembali ke huruf.
    - Jika bukan huruf, tambahkan langsung ke hasil tanpa perubahan
    
  6. Tampilkan hasil enkripsi atau dekripsi.
  7. Selesai.


2. Langkah 2 - Implementasi Vigenere Cipher

  1. Mulai program Vigenere.py.
  2. Minta pengguna memasukkan:
    - Teks yang akan dienkripsi atau didekripsi
    - Kunci (key)
    - Mode (e untuk enkripsi, d untuk dekripsi)
  3. Ubah semua huruf kunci menjadi huruf kapital.
  4. Buat variabel kosong bernama hasil.
  5. Untuk setiap karakter dalam teks:
    - Jika huruf alfabet:
      . Tentukan nilai shift berdasarkan huruf kunci:
         shift = (kode huruf kunci) - 'A'
      . Geser huruf teks dengan rumus:
         (kode huruf + shift) mod 26
   - Tambahkan hasil ke ciphertext.
   - Pindah ke huruf kunci berikutnya.
   - Jika bukan huruf, tambahkan langsung tanpa perubahan.
  6. Tampilkan hasil enkripsi atau dekripsi.
  7. Selesai.


Langkah 3 - Implementasi transposisi Cipher Sederhana

  1. Mulai program transposisi.py.
  2. Minta pengguna memasukkan:
    - Teks yang akan dienkripsi atau didekripsi
    - Kunci (key)
    - Mode (e untuk enkripsi, d untuk dekripsi)
  3. Buat daftar kosong ciphertext dengan panjang sebanyak kunci.
  4. Untuk setiap kolom dari 0 hingga kunci - 1:
    - Ambil huruf dari plaintext mulai dari posisi kolom tersebut.
    - Lewati huruf setiap kunci langkah
      (misalnya setiap 3 huruf jika kunci = 3).
    - Simpan huruf-huruf tersebut ke dalam ciphertext[col].
  5. Gabungkan semua elemen ciphertext menjadi satu string.
  6. Hasilnya adalah teks terenkripsi (ciphertext).
  7. Tampilkan hasil enkripsi atau dekripsi.
  8. Selesai.

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
- Pertanyaan 1: Kelemahan utama Caesar Cipher adalah ruang kunci yang sangat terbatas hanya 26 kemungkinan, sehingga mudah sekali dipecahkan dengan serangan brute force. Vigenère Cipher, meskipun lebih kompleks dengan substitusi abjad-majemuk, memiliki kelemahan pada pengulangan kunci yang dapat dimanfaatkan untuk analisis kasiski dan memecahkan cipher.

- Pertanyaan 2: Cipher klasik rentan terhadap analisis frekuensi karena metode ini memanfaatkan pola kemunculan huruf dalam bahasa asli. Substitusi huruf yang konsisten menjaga distribusi frekuensi huruf asli, sehingga analisis statistik bisa mengungkap hubungan antara ciphertext dan plaintext, menjadikan cipher tersebut mudah diserang.

- Pertanyaan 3: Cipher substitusi menggantikan setiap huruf plaintext dengan huruf lain, mudah diimplementasikan namun rentan terhadap analisis frekuensi. Cipher transposisi mengacak urutan huruf tanpa mengubah huruf itu sendiri, lebih sulit dipecahkan dengan analisis frekuensi, namun jika pola pengacakan diketahui, cipher ini juga dapat dengan mudah dipecahkan. Keduanya memiliki kelebihan dan kelemahan yang dapat dikombinasikan untuk keamanan lebih baik.
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
commit week5-cipher-klasik
Author: Novi Ari Wardani <ewardani101103@gmail.com>
Date:   2025-11-12

    week2-cryptosystem: Cipher Klasik (Caesar , Vigenere, Transposisi) )
```
