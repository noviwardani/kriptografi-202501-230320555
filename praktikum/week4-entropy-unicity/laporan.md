# Laporan Praktikum Kriptografi
Minggu ke-: 4 
Topik:  Entropy & Unicity Distance  
Nama: Novi Ari Wardani 
NIM: 230320555 
Kelas: 5DSRA  

---

## 1. Tujuan
(Tuliskan tujuan pembelajaran praktikum sesuai modul.)

1. Menyelesaikan perhitungan sederhana terkait entropi kunci.
2. Menggunakan teorema Euler pada contoh perhitungan modular & invers.
3. Menghitung unicity distance untuk ciphertext tertentu.
4. Menganalisis kekuatan kunci berdasarkan entropi dan unicity distance.
5. Mengevaluasi potensi serangan brute force pada kriptosistem sederhana.



## 2. Dasar Teori
(Ringkas teori relevan (cukup 2–3 paragraf).  

Teori entropi dalam kriptografi menggambarkan tingkat ketidakpastian atau keacakan dari suatu sistem, khususnya dalam konteks informasi dan keamanan data. Entropi digunakan untuk mengukur jumlah informasi yang terkandung dalam pesan atau kunci, serta menentukan seberapa sulit sistem tersebut dapat dipecahkan oleh penyerang. Semakin tinggi entropi, semakin besar keragaman dan keacakan yang dimiliki, sehingga sistem menjadi lebih aman terhadap serangan kriptanalisis.​

Unicity distance adalah konsep yang dikembangkan oleh Claude Shannon untuk menentukan panjang minimum ciphertext yang diperlukan agar hanya ada satu kunci yang dapat menghasilkan plaintext yang bermakna. Dengan kata lain, unicity distance menunjukkan seberapa banyak ciphertext yang harus diketahui agar penyerang dapat memastikan bahwa kunci yang ditemukan adalah kunci yang benar, bukan sekadar kunci palsu yang menghasilkan plaintext acak. Nilai unicity distance bergantung pada entropi kunci dan redundansi pesan; semakin besar entropi kunci dan semakin kecil redundansi pesan, semakin besar unicity distance yang dibutuhkan untuk memecahkan sistem kriptografi.​


## 3. Alat dan Bahan
(- Python 3.x  
- Visual Studio Code   
- Git dan akun GitHub  



## 4. Langkah Percobaan
(Tuliskan langkah yang dilakukan sesuai instruksi.  
Contoh format: Langkah 1 — Perhitungan Entropi

  1. Masukkan ukuran ruang kunci (|K|).
  2. Hitung entropi menggunakan rumus: H(K)=log2​(∣K∣)
  3. Tampilkan hasil perhitungan.

Langkah 2 — Menghitung Unicity Distance

  1. Masukkan nilai:
    - Entropi kunci (H(K))
    - Redundansi bahasa (R) — misal 0.75
    - Ukuran alfabet (|A|) — misal 26
  2. Gunakan rumus: U = (H(K)) / R ⋅ log2 ∣A∣
  3. Tampilkan hasil perhitungan.

Langkah 3 — Analisis Brute Force

  1. Masukkan:
    - Ukuran ruang kunci (|K|)
    - Kecepatan komputer (percobaan per detik)
  2. Gunakan rumus: t = |K| / (percobaan per detik)
  3. Ubah hasil ke dalam satuan hari.
  4. Tampilkan hasil perhitungan.


## 5. Source Code
(Salin kode program utama yang dibuat atau dimodifikasi.  
Gunakan blok kode:

import math
def entropy(keyspace_size):
    return math.log2(keyspace_size)

print("=== PERHITUNGAN ENTROPI ===")
print("Entropy ruang kunci 26 =", entropy(26), "bit")
print("Entropy ruang kunci 2^128 =", entropy(2**128), "bit")

=== PERHITUNGAN ENTROPI ===
Entropy ruang kunci 26 = 4.700439718141092 bit
Entropy ruang kunci 2^128 = 128.0 bit

import math

def entropy(keyspace_size):
    return math.log2(keyspace_size)

def unicity_distance(HK, R=0.75, A=26):
    return HK / (R * math.log2(A))

HK = entropy(26)
U = unicity_distance(HK)

print("=== PERHITUNGAN UNICITY DISTANCE ===")
print("Entropi kunci (H(K)) =", HK, "bit")
print("Unicity Distance (U) =", U, "karakter")

=== === PERHITUNGAN UNICITY DISTANCE ===
Entropi kunci (H(K)) = 4.700439718141092 bit
Unicity Distance (U) = 1.3333333333333333 karakter

def brute_force_time(keyspace_size, attempts_per_second=1e6):
    seconds = keyspace_size / attempts_per_second
    days = seconds / (3600 * 24)
    return days

print("=== ANALISIS BRUTE FORCE ===")
print("Waktu brute force Caesar Cipher (26 kunci) =", brute_force_time(26), "hari")
print("Waktu brute force AES-128 =", brute_force_time(2**128), "hari")


=== ANALISIS BRUTE FORCE ===
Waktu brute force Caesar Cipher (26 kunci) = 3.0092592592592593e-10 hari
Waktu brute force AES-128 = 3.938453320844195e+27 hari

)



## 6. Hasil dan Pembahasan
(- Lampirkan screenshot hasil eksekusi program (taruh di folder `screenshots/`).  
 1. Algoritma klasik seperti Caesar Cipher terbukti memiliki entropi rendah dan mudah dipecahkan.
2. Algoritma modern seperti AES-128 memiliki entropi tinggi dan tidak realistis untuk diserang dengan brute force.

Hasil eksekusi program Caesar Cipher:

)

---

## 7. Jawaban Pertanyaan
(Jawab pertanyaan diskusi yang diberikan pada modul.  

1. Pertanyaan 1 : Entropi adalah ukuran ketidakpastian kunci enkripsi; semakin tinggi entropi, semakin kuat dan sulit ditebak kunci tersebut.

2. Pertanyaan 2 : Unicity distance menunjukkan jumlah minimum ciphertext yang diperlukan agar kunci enkripsi bisa ditemukan secara unik, penting untuk menilai keamanan cipher.

3. Pertanyaan 3 : Brute force tetap mengancam karena terus berkembangnya kemampuan komputasi sehingga bisa mencoba semua kemungkinan kunci meski algoritma kuat.

## 8. Kesimpulan
(Tuliskan kesimpulan singkat (2–3 kalimat) berdasarkan percobaan.  )

Algoritma sederhana seperti Caesar Cipher memiliki tingkat entropi rendah dan jarak unicity kecil, sehingga mudah dibobol menggunakan metode brute force karena ruang kunci yang terbatas. Sebaliknya, AES-128 menawarkan entropi yang jauh lebih tinggi dan unicity distance yang besar, membuatnya sangat sulit ditembus karena ruang kunci yang sangat luas. Dengan demikian, AES-128 memberikan perlindungan yang jauh lebih efektif terhadap serangan berbasis percobaan kunci secara sistematis dibandingkan dengan Caesar Cipher yang sederhana dan rentan.

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
commit week4-entropy-unicity
Author: Novi Ari Wardani <wardani101103@gmail.com>
Date:   2025-11-12

    week2-cryptosystem: Entropy & Unicity Distance (Evaluasi Kekuatan Kunci dan Brute Force )
```
