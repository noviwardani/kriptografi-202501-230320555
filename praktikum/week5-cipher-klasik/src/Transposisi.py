def transposisi_enkripsi(plaintext, kunci):
    ciphertext = [''] * kunci
    for col in range(kunci):
        pointer = col
        while pointer < len(plaintext):
            ciphertext[col] += plaintext[pointer]
            pointer += kunci
    return ''.join(ciphertext)


def transposisi_dekripsi(ciphertext, kunci):
    num_of_columns = int(len(ciphertext) / kunci + 0.9999)  # pembulatan ke atas
    num_of_rows = kunci
    num_of_shaded_boxes = (num_of_columns * num_of_rows) - len(ciphertext)

    plaintext = [''] * num_of_columns
    col = 0
    row = 0

    for symbol in ciphertext:
        plaintext[col] += symbol
        col += 1

        if (col == num_of_columns) or (col == num_of_columns - 1 and row >= num_of_rows - num_of_shaded_boxes):
            col = 0
            row += 1

    return ''.join(plaintext)


# === Mode interaktif ===
print("=== Program Transposisi Cipher ===")
teks = input("Masukkan teks: ").replace(" ", "")
kunci = int(input("Masukkan kunci (angka): "))
mode = input("Mode (e = enkripsi, d = dekripsi): ").lower()

if mode == 'e':
    hasil = transposisi_enkripsi(teks, kunci)
    print("\nHasil Enkripsi:", hasil)
elif mode == 'd':
    hasil = transposisi_dekripsi(teks, kunci)
    print("\nHasil Dekripsi:", hasil)
else:
    print("\nMode tidak dikenal. Gunakan 'e' untuk enkripsi atau 'd' untuk dekripsi.")