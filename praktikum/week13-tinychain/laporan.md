# Laporan Praktikum Kriptografi
Minggu ke-: 13 
Topik: [TinyChain – Proof of Work (PoW)]  
Nama: [Novi Ari Wardani]  
NIM: [230320555]  
Kelas: [5DSRA]  

---

## 1. Tujuan
(Tuliskan tujuan pembelajaran praktikum sesuai modul.)

1. Menjelaskan peran hash function dalam blockchain.
2. Melakukan simulasi sederhana Proof of Work (PoW).
3. Menganalisis keamanan cryptocurrency berbasis kriptografi.

## 2. Dasar Teori
(Ringkas teori relevan (cukup 2–3 paragraf).  

Hash function memiliki peran yang sangat penting dalam teknologi blockchain. Fungsi hash adalah algoritma kriptografi yang mengubah data dengan ukuran apa pun menjadi keluaran dengan panjang tetap (hash value). Dalam blockchain, hash digunakan untuk menjaga integritas data, menghubungkan satu blok dengan blok sebelumnya, serta memastikan bahwa data yang tersimpan tidak dapat diubah tanpa terdeteksi. Sifat utama hash function seperti deterministik, sulit dibalik (one-way), dan sensitif terhadap perubahan input menjadikan blockchain aman dan transparan.

Proof of Work (PoW) merupakan mekanisme konsensus yang digunakan dalam beberapa blockchain, seperti Bitcoin, untuk memvalidasi transaksi dan menambahkan blok baru ke dalam rantai. Dalam PoW, penambang (miner) harus menyelesaikan teka-teki kriptografi dengan cara mencari nilai nonce yang menghasilkan hash sesuai dengan tingkat kesulitan tertentu. Proses ini membutuhkan daya komputasi yang besar dan waktu, sehingga mencegah serangan manipulasi data. Simulasi sederhana PoW biasanya dilakukan dengan mencoba berbagai nilai nonce hingga ditemukan hash yang memenuhi syarat, sehingga membantu memahami cara kerja konsensus blockchain.

Keamanan cryptocurrency sangat bergantung pada penerapan kriptografi yang kuat. Selain hash function dan PoW, blockchain juga menggunakan kriptografi kunci publik dan kunci privat untuk mengamankan transaksi. Setiap pengguna memiliki kunci privat untuk menandatangani transaksi secara digital, sehingga hanya pemilik sah yang dapat mengakses dan memindahkan asetnya. Kombinasi antara hash function, mekanisme konsensus, dan tanda tangan digital menjadikan cryptocurrency tahan terhadap pemalsuan, perubahan data, dan serangan pihak yang tidak berwenang.

## 3. Alat dan Bahan
(- Python 3.x  
- Visual Studio Code / editor lain  
- Git dan akun GitHub  
- Library tambahan (misalnya pycryptodome, jika diperlukan)  )

---

## 4. Langkah Percobaan
(Tuliskan langkah yang dilakukan sesuai instruksi.  

Langkah 1 - Membuat Strukture Blok

1. Program mengimpor library hashlib dan time.
2. Class Block dibuat sebagai struktur blok blockchain.
3. Saat blok dibuat, data dan hash awal dihitung.
4. Fungsi calculate_hash() membuat hash SHA-256 dari data blok.
5. Fungsi mine_block() menjalankan Proof of Work.
6. Nilai nonce terus diubah sampai hash sesuai tingkat kesulitan.
7. Jika hash valid ditemukan, blok berhasil ditambang dan ditampilkan.

Langkah 2 - Membuat Blokchain

1. Class Blockchain dibuat untuk mengelola kumpulan blok (chain).
2. Saat blockchain dibuat, sistem otomatis membuat genesis block sebagai blok pertama.
3. Nilai difficulty ditentukan untuk mengatur tingkat kesulitan Proof of Work.
4. Fungsi create_genesis_block() membuat blok awal dengan index 0.
5. Fungsi get_latest_block() mengambil blok terakhir dalam blockchain.
6. Fungsi add_block() digunakan untuk menambahkan blok baru ke blockchain.
7. Hash blok sebelumnya disimpan ke previous_hash blok baru.
8. Blok baru ditambang menggunakan fungsi mine_block().
9. Setelah mining berhasil, blok ditambahkan ke dalam chain.
10. Program menguji blockchain dengan menambahkan dua blok transaksi dan menampilkan proses mining.

Langkah 3 - Analisis Proof of Work

1. Mengamati bahwa penambangan mengulang perhitungan hash berkali-kali sampai memenuhi syarat awalan nol.
2. Mencoba mengubah nilai difficulty (misalnya 2, 4, 5) dan membandingkan waktu/iterasi mining.
3. Menyimpulkan bahwa PoW meningkatkan keamanan karena perubahan isi blok mengubah hash, sehingga rantai menjadi tidak valid dan perlu penambangan ulang untuk menyamakan kembali hash.



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


## 7. Jawaban Pertanyaan
(Jawab pertanyaan diskusi yang diberikan pada modul.  
- Pertanyaan 1:
Fungsi hash penting karena menjaga integritas dan keamanan data dalam blockchain. Setiap perubahan kecil pada data akan menghasilkan hash yang berbeda, sehingga manipulasi data dapat langsung terdeteksi. Hash juga menghubungkan satu blok dengan blok sebelumnya, membentuk rantai yang sulit diubah.

- Pertanyaan 2: 
Proof of Work mencegah double spending dengan memastikan bahwa setiap transaksi hanya dapat dicatat dalam satu blok yang valid melalui proses penambangan yang memerlukan waktu dan daya komputasi. Setelah transaksi dikonfirmasi dan masuk ke blockchain, mengubah atau menggandakan transaksi tersebut membutuhkan kekuatan komputasi yang sangat besar, sehingga tidak praktis dilakukan.

- Pertanyaan 3: 
Kelemahan utama PoW adalah konsumsi energi yang sangat tinggi, karena proses mining memerlukan perhitungan hash berulang-ulang. Banyaknya perangkat komputasi yang bekerja secara bersamaan menyebabkan pemborosan energi dan berdampak negatif terhadap lingkungan.
)


## 8. Kesimpulan
(Tuliskan kesimpulan singkat (2–3 kalimat) berdasarkan percobaan.  )

Blockchain memanfaatkan fungsi hash untuk menjaga integritas data dan menghubungkan setiap blok secara aman. Mekanisme Proof of Work digunakan untuk memvalidasi transaksi dan mencegah kecurangan seperti double spending melalui proses komputasi yang sulit. Meskipun efektif dari sisi keamanan, Proof of Work memiliki kelemahan utama berupa konsumsi energi yang tinggi sehingga kurang efisien.

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
commit week 13 TinyChain – Proof of Work (PoW)
Author: Novi Ari Wardani <wardani101103@gmail.com>
Date:   2026-01-25

    commit week 13 TinyChain – Proof of Work (PoW)
```
