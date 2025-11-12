# Program Caesar Cipher sederhana

# Input teks dan jumlah pergeseran
text = input("Masukkan teks: ")
shift = int(input("Masukkan jumlah shift: "))

# Pilih mode
mode = input("Mode (e = enkripsi, d = dekripsi): ")

# Jika dekripsi, ubah arah shift
if mode.lower() == 'd':
    shift = -shift

hasil = ""

for char in text:
    if char.isalpha():  # hanya geser huruf
        start = ord('A') if char.isupper() else ord('a')
        hasil += chr((ord(char) - start + shift) % 26 + start)
    else:
        hasil += char  # biarkan karakter non-huruf
print("Hasil:", hasil)
