def vigenere_enkripsi(plaintext, kunci):
    ciphertext = ""
    kunci = kunci.upper()
    kunci_index = 0
    
    for char in plaintext:
        if 'A' <= char.upper() <= 'Z':
            # Tentukan pergeseran
            shift = ord(kunci[kunci_index % len(kunci)]) - ord('A')
            
            # Tentukan base (A=0 atau a=0)
            base = ord('A') if char.isupper() else ord('a')
            
            # Enkripsi: (char_index + shift) mod 26
            enkripsi_char = chr((ord(char) - base + shift) % 26 + base)
            ciphertext += enkripsi_char
            
            # Pindah ke huruf kunci berikutnya
            kunci_index += 1
        else:
            # Karakter non-alfabet (spasi, tanda baca) tidak diubah
            ciphertext += char
            
    return ciphertext

def vigenere_dekripsi(ciphertext, kunci):
    plaintext = ""
    kunci = kunci.upper()
    kunci_index = 0
    
    for char in ciphertext:
        if 'A' <= char.upper() <= 'Z':
            # Tentukan pergeseran
            shift = ord(kunci[kunci_index % len(kunci)]) - ord('A')
            
            # Tentukan base (A=0 atau a=0)
            base = ord('A') if char.isupper() else ord('a')
            
            # Dekripsi: (char_index - shift) mod 26
            dekripsi_char = chr((ord(char) - base - shift) % 26 + base)
            plaintext += dekripsi_char
            
            # Pindah ke huruf kunci berikutnya
            kunci_index += 1
        else:
            # Karakter non-alfabet (spasi, tanda baca) tidak diubah
            plaintext += char
            
    return plaintext

# Contoh Penggunaan
teks_asli = "pesan"
kunci_vigenere = "kunci"
teks_terenkripsi = vigenere_enkripsi(teks_asli, kunci_vigenere)
teks_terdekripsi = vigenere_dekripsi(teks_terenkripsi, kunci_vigenere)

print(f"Plaintext: {teks_asli}")
print(f"Kunci: {kunci_vigenere}")
print(f"Ciphertext (Vigenere): {teks_terenkripsi}")
print(f"Decrypted Text: {teks_terdekripsi}")
