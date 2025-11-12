# Program Vigenere Cipher sederhana (interaktif)

def vigenere_enkripsi(plaintext, kunci):
    ciphertext = ""
    kunci = kunci.upper()
    kunci_index = 0
    
    for char in plaintext:
        if 'A' <= char.upper() <= 'Z':
            shift = ord(kunci[kunci_index % len(kunci)]) - ord('A')
            base = ord('A') if char.isupper() else ord('a')
            enkripsi_char = chr((ord(char) - base + shift) % 26 + base)
            ciphertext += enkripsi_char
            kunci_index += 1
        else:
            ciphertext += char
    return ciphertext


def vigenere_dekripsi(ciphertext, kunci):
    plaintext = ""
    kunci = kunci.upper()
    kunci_index = 0
    
    for char in ciphertext:
        if 'A' <= char.upper() <= 'Z':
            shift = ord(kunci[kunci_index % len(kunci)]) - ord('A')
            base = ord('A') if char.isupper() else ord('a')
            dekripsi_char = chr((ord(char) - base - shift) % 26 + base)
            plaintext += dekripsi_char
            kunci_index += 1
        else:
            plaintext += char
    return plaintext


# === Mode interaktif ===
print("=== Program Vigenere Cipher ===")
teks = input("Masukkan teks: ")
kunci = input("Masukkan kunci: ")
mode = input("Mode (e = enkripsi, d = dekripsi): ").lower()

if mode == 'e':
    hasil = vigenere_enkripsi(teks, kunci)
    print("\nHasil Enkripsi:", hasil)
elif mode == 'd':
    hasil = vigenere_dekripsi(teks, kunci)
    print("\nHasil Dekripsi:", hasil)
else:
    print("\nMode tidak dikenal. Gunakan 'e' untuk enkripsi atau 'd' untuk dekripsi.")