# Laporan Praktikum Kriptografi
Minggu ke-: 12 
Topik: [Aplikasi TLS & E-commerce]  
Nama: [Novi Ari Wardani]  
NIM: [230320555]  
Kelas: [5DSRA]  

---

## 1. Tujuan
(Tuliskan tujuan pembelajaran praktikum sesuai modul.)

1. Menganalisis penggunaan kriptografi pada email dan SSL/TLS.
2. Menjelaskan enkripsi dalam transaksi e-commerce.
3. Mengevaluasi isu etika & privasi dalam penggunaan kriptografi di kehidupan sehari-hari.

## 2. Dasar Teori
(Ringkas teori relevan (cukup 2–3 paragraf).  

Kriptografi digunakan secara luas untuk mengamankan komunikasi digital, terutama pada email dan protokol SSL/TLS. Pada email, kriptografi berfungsi untuk menjaga kerahasiaan, keaslian, dan integritas pesan melalui teknik seperti enkripsi (misalnya PGP atau S/MIME) dan tanda tangan digital. Sementara itu, SSL/TLS digunakan untuk mengamankan komunikasi antara klien dan server di internet dengan mengenkripsi data yang dikirim, melakukan autentikasi server (dan kadang klien), serta mencegah penyadapan dan serangan man-in-the-middle.

Dalam transaksi e-commerce, enkripsi berperan penting untuk melindungi data sensitif seperti nomor kartu kredit, informasi akun, dan detail transaksi. Protokol SSL/TLS memastikan bahwa data yang dikirimkan antara pengguna dan platform e-commerce tidak dapat dibaca atau dimodifikasi oleh pihak yang tidak berwenang. Dengan adanya enkripsi kunci simetris dan asimetris, sistem e-commerce dapat menjamin keamanan transaksi, meningkatkan kepercayaan pengguna, serta mendukung proses pembayaran digital yang aman dan andal.

Meskipun kriptografi memberikan manfaat besar, penggunaannya juga menimbulkan isu etika dan privasi dalam kehidupan sehari-hari. Di satu sisi, kriptografi melindungi hak privasi individu dan kebebasan berkomunikasi, namun di sisi lain dapat disalahgunakan untuk menyembunyikan aktivitas ilegal. Selain itu, perdebatan muncul terkait akses pemerintah terhadap data terenkripsi dan perlindungan data pribadi oleh perusahaan teknologi, sehingga diperlukan keseimbangan antara keamanan, privasi, dan kepentingan hukum.

## 3. Alat dan Bahan
(- Python 3.x  
- Visual Studio Code / editor lain  
- Git dan akun GitHub  
- Library tambahan (misalnya pycryptodome, jika diperlukan)  )

---

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

Langkah 1 — Analisis SSL/TLS pada Email & Web

Berdasarkan hasil pemeriksaan sertifikat digital pada https://shopee.co.id
, website ini telah menggunakan HTTPS yang menandakan komunikasi diamankan dengan SSL/TLS. Sertifikat dikeluarkan oleh GlobalSign GCC R6 AlphaSSL CA 2023 sebagai Certificate Authority (CA), yang merupakan CA tepercaya secara internasional. Sertifikat berlaku dari 24 Maret 2025 hingga 25 April 2026, menunjukkan masa berlaku yang masih aktif dan aman. Sertifikat ini menggunakan SHA-256 sebagai algoritma hash, sementara mekanisme TLS umumnya memanfaatkan RSA atau ECDHE untuk pertukaran kunci dan AES untuk enkripsi data.

Perbedaan utama antara website HTTPS dan non-HTTPS adalah pada keamanan data. HTTPS mengenkripsi seluruh data yang dikirim (login, cookie, transaksi), sedangkan HTTP mengirim data dalam bentuk teks biasa (plaintext) sehingga mudah disadap. Tanpa HTTPS, pengguna rentan terhadap pencurian akun, pemalsuan halaman, dan manipulasi data.

Langkah 2 — Studi Kasus Enkripsi pada E-commerce

Dalam e-commerce seperti Shopee, enkripsi digunakan saat login, pencarian produk, checkout, dan pembayaran. TLS memastikan data sensitif (username, password, nomor kartu, OTP) tidak dapat dibaca oleh pihak ketiga. Proses ini melibatkan enkripsi kunci simetris (AES) untuk efisiensi dan kunci asimetris (RSA/ECC) untuk pertukaran kunci secara aman.

Jika TLS tidak digunakan, ancaman seperti Man-in-the-Middle (MITM) dapat terjadi, di mana penyerang menyadap atau mengubah data transaksi. Risiko lainnya meliputi pencurian identitas, pengambilalihan akun, dan kebocoran data finansial yang dapat merugikan pengguna maupun perusahaan.

Langkah 3 — Analisis Etika & Privasi

Penggunaan kriptografi dalam email terenkripsi seperti PGP dan S/MIME meningkatkan perlindungan privasi pengguna, namun juga memunculkan dilema etika. Salah satunya adalah apakah perusahaan berhak mendekripsi email karyawan demi kepentingan audit dan keamanan internal. Di satu sisi, ini penting untuk mencegah kebocoran data, tetapi di sisi lain dapat melanggar privasi individu.

Selain itu, terdapat perdebatan terkait pengawasan pemerintah terhadap komunikasi terenkripsi. Kriptografi melindungi kebebasan berkomunikasi masyarakat, namun juga dapat dimanfaatkan untuk aktivitas ilegal. Oleh karena itu, dibutuhkan keseimbangan antara keamanan nasional, kepentingan hukum, dan hak privasi pengguna agar penggunaan kriptografi tetap etis dan bertanggung jawab.

---

## 7. Jawaban Pertanyaan
(Jawab pertanyaan diskusi yang diberikan pada modul.  
- Pertanyaan 1: 
HTTP (Hypertext Transfer Protocol) mengirimkan data dalam bentuk teks biasa (plaintext) sehingga mudah disadap atau dimodifikasi oleh pihak tidak berwenang. Sebaliknya, HTTPS (HTTP Secure) menggunakan SSL/TLS untuk mengenkripsi data yang dikirim antara klien dan server, sehingga menjaga kerahasiaan, integritas, dan keaslian data. Dengan HTTPS, informasi sensitif seperti password dan data pembayaran menjadi lebih aman dari serangan seperti Man-in-the-Middle.

- Pertanyaan 2: 
Sertifikat digital berfungsi untuk memverifikasi identitas server agar pengguna yakin bahwa mereka terhubung ke situs yang benar, bukan situs palsu. Sertifikat ini dikeluarkan oleh Certificate Authority (CA) tepercaya dan berisi kunci publik server. Dalam TLS, sertifikat digital memungkinkan proses autentikasi dan pertukaran kunci yang aman, sehingga mencegah penyadapan dan pemalsuan komunikasi.

- Pertanyaa 3: 
Kriptografi melindungi privasi dengan mengenkripsi komunikasi digital sehingga hanya pihak berwenang yang dapat mengakses isi pesan. Namun, hal ini juga menimbulkan tantangan hukum dan etika karena enkripsi dapat menyulitkan penegakan hukum dalam mengakses data terkait kejahatan. Selain itu, muncul dilema antara hak privasi individu dan kepentingan keamanan serta pengawasan, baik oleh perusahaan maupun pemerintah, sehingga diperlukan regulasi yang seimbang dan bertanggung jawab.
)


## 8. Kesimpulan
(Tuliskan kesimpulan singkat (2–3 kalimat) berdasarkan percobaan.  )

Kriptografi berperan penting dalam mengamankan komunikasi digital melalui penerapan SSL/TLS, sertifikat digital, dan enkripsi data pada email serta e-commerce. Teknologi ini melindungi kerahasiaan, integritas, dan keaslian data pengguna dari berbagai ancaman keamanan siber. Namun, di sisi lain, kriptografi juga menimbulkan tantangan etika dan hukum terkait privasi, pengawasan, dan akses data, sehingga diperlukan pengaturan yang seimbang dan bertanggung jawab.

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
commit week 12 (Aplikasi TLS & E-commerce)
Author: Novi Ari Wardani <wardani101103@gmail.com>
Date:   2026-01-20

    week 12 (Aplikasi TLS & E-commerce)
