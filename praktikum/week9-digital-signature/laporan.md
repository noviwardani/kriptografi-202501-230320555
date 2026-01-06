# Laporan Praktikum Kriptografi
Minggu ke-: 9  
Topik: [Digital Signature (RSA/DSA)]  
Nama: [Novi Ari Wardani]  
NIM: [230320555]  
Kelas: [5DSRA]  

---

## 1. Tujuan
(Tuliskan tujuan pembelajaran praktikum sesuai modul.)

1. Mengimplementasikan tanda tangan digital menggunakan algoritma RSA/DSA.
2. Memverifikasi keaslian tanda tangan digital.
3. Menjelaskan manfaat tanda tangan digital dalam otentikasi pesan dan integritas data

## 2. Dasar Teori
(Ringkas teori relevan (cukup 2–3 paragraf).  
Contoh: definisi cipher klasik, konsep modular aritmetika, dll.  )

Tanda tangan digital adalah mekanisme keamanan yang menggunakan algoritma kriptografi kunci publik seperti RSA atau DSA untuk menjamin keaslian dan integritas pesan. Prosesnya dilakukan dengan membuat nilai hash dari pesan, kemudian mengenkripsi hash tersebut menggunakan kunci privat pengirim sehingga menghasilkan tanda tangan digital, yang selanjutnya dapat diverifikasi oleh penerima menggunakan kunci publik.

Verifikasi tanda tangan digital dilakukan dengan membandingkan hasil dekripsi tanda tangan dengan nilai hash pesan yang dihitung ulang. Jika hasilnya sama, maka pesan dipastikan berasal dari pengirim yang sah dan tidak mengalami perubahan selama pengiriman, sedangkan perbedaan nilai menunjukkan adanya manipulasi atau pemalsuan pesan.

Manfaat tanda tangan digital meliputi autentikasi pengirim, integritas data, dan non-repudiation, sehingga pengirim tidak dapat menyangkal keabsahan pesan yang dikirim. Oleh karena itu, tanda tangan digital sangat penting dalam menjamin keamanan komunikasi dan transaksi digital di lingkungan jaringan terbuka.

## 3. Alat dan Bahan
(- Python 3.x  
- Visual Studio Code / editor lain  
- Git dan akun GitHub  
- Library tambahan (misalnya pycryptodome, jika diperlukan)  )

---

## 4. Langkah Percobaan
(Tuliskan langkah yang dilakukan sesuai instruksi.  
Contoh format:

Langkah 1 : Generate Key dan Buat Tanda Tangan

1. Menentukan dua bilangan prima p = 61 dan q =53
2. Membuat kunci publik dan kunci privat menggunakan algoritma RSA.
3. Menentukan pesan yang akan dikirim, yaitu "Transfer Gaji".
4. Mengubah pesan menjadi nilai hash menggunakan SHA-256.
5. Mengenkripsi hash pesan menggunakan kunci privat untuk menghasilkan tanda tangan digital.

Langkah 2 : Verifikasi Tanda Tangan

1. Penerima menerima pesan dan tanda tangan digital.
2. Mengubah pesan menjadi nilai hash.
3. Membuka tanda tangan digital menggunakan kunci publik.
4. Membandingkan hash pesan dengan hash hasil verifikasi.
5. Menyimpulkan bahwa tanda tangan VALID jika nilainya sama.

Langkah 3 : Uji Modifikasi Pesan

1. Mengubah isi pesan menjadi "Transfer Gaji (Ditambah Bonus)".
2. Menggunakan tanda tangan lama tanpa membuat tanda tangan baru.
3. Melakukan proses verifikasi kembali.
4. Membandingkan hash pesan baru dengan hash dari tanda tangan lama.
5. Menyimpulkan bahwa tanda tangan TIDAK VALID karena nilai hash berbeda.

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
- Pertanyaan 1: Perbedaan utama antara enkripsi RSA dan tanda tangan digital RSA terletak pada tujuan dan penggunaan kuncinya. Enkripsi RSA digunakan untuk menjaga kerahasiaan pesan, di mana pesan dienkripsi menggunakan kunci publik penerima dan hanya dapat didekripsi dengan kunci privat penerima. Sebaliknya, tanda tangan digital RSA digunakan untuk menjamin keaslian dan integritas pesan, di mana pengirim membuat tanda tangan dengan kunci privatnya, dan penerima memverifikasinya menggunakan kunci publik pengirim.

- Pertanyaan 2: Tanda tangan digital menjamin integritas karena pesan terlebih dahulu diubah menjadi nilai hash, sehingga perubahan sekecil apa pun pada pesan akan menghasilkan hash yang berbeda dan menyebabkan verifikasi gagal. Selain itu, tanda tangan digital menjamin otentikasi karena hanya pemilik kunci privat yang sah yang dapat membuat tanda tangan tersebut, sehingga penerima dapat memastikan bahwa pesan benar-benar berasal dari pengirim yang asli.

- Pertanyaan 3 : 

Certificate Authority (CA) berperan sebagai pihak tepercaya yang memverifikasi identitas pemilik kunci publik dan menerbitkan sertifikat digital. Sertifikat ini mengaitkan identitas seseorang atau organisasi dengan kunci publiknya, sehingga penerima dapat mempercayai bahwa kunci publik yang digunakan untuk verifikasi tanda tangan digital benar-benar milik pengirim yang sah dan bukan hasil pemalsuan.
)


## 8. Kesimpulan
(Tuliskan kesimpulan singkat (2–3 kalimat) berdasarkan percobaan.  )

Berdasarkan seluruh rangkaian percobaan dan pembahasan, dapat disimpulkan bahwa kriptografi kunci publik memungkinkan pengamanan komunikasi melalui mekanisme pertukaran kunci dan tanda tangan digital tanpa memerlukan saluran rahasia. Implementasi Diffie–Hellman menunjukkan bagaimana kunci rahasia dapat dibentuk secara aman, namun juga mengungkap kelemahan terhadap serangan Man-in-the-Middle jika tidak disertai autentikasi. Sementara itu, penerapan tanda tangan digital berbasis RSA membuktikan bahwa integritas, otentikasi, dan keabsahan pesan dapat dijamin secara kuat, terutama ketika dikombinasikan dengan Certificate Authority dalam sistem keamanan modern.

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
commit week9 Digital Signature (RSA/DSA)
Author: Novi Ari Wardani <emawardani101103@gmail.com>
Date:   2025-10-2025

    week9-Digital Signature (RSA/DSA) )
```
