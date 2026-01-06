from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad
import binascii

def enkripsi_des(plaintext, kunci):
    """Enkripsi teks menggunakan DES"""
    # Pastikan kunci 8 byte
    if len(kunci) != 8:
        kunci = kunci.ljust(8, '0')[:8]
    
    # Buat cipher DES
    cipher = DES.new(kunci.encode(), DES.MODE_ECB)
    
    # Padding plaintext ke kelipatan 8 byte
    plaintext_bytes = pad(plaintext.encode(), DES.block_size)
    
    # Enkripsi
    ciphertext = cipher.encrypt(plaintext_bytes)
    
    # Konversi ke hex untuk ditampilkan
    return binascii.hexlify(ciphertext).decode()

def dekripsi_des(ciphertext_hex, kunci):
    """Dekripsi teks menggunakan DES"""
    # Pastikan kunci 8 byte
    if len(kunci) != 8:
        kunci = kunci.ljust(8, '0')[:8]
    
    # Buat cipher DES
    cipher = DES.new(kunci.encode(), DES.MODE_ECB)
    
    # Konversi hex ke bytes
    ciphertext = binascii.unhexlify(ciphertext_hex)
    
    # Dekripsi
    plaintext_bytes = cipher.decrypt(ciphertext)
    
    # Unpad
    plaintext = unpad(plaintext_bytes, DES.block_size)
    
    return plaintext.decode()

# Contoh penggunaan
if __name__ == "__main__":
    print("=" * 50)
    print("PROGRAM ENKRIPSI DES")
    print("=" * 50)
    
    # Input dari user
    pesan = input("\nMasukkan teks yang ingin dienkripsi: ")
    kunci = input("Masukkan kunci (8 karakter): ")
    
    # Enkripsi
    print("\n" + "-" * 50)
    hasil_enkripsi = enkripsi_des(pesan, kunci)
    print(f"Teks Asli    : {pesan}")
    print(f"Kunci        : {kunci}")
    print(f"Hasil Enkripsi: {hasil_enkripsi}")
    
    # Dekripsi
    print("\n" + "-" * 50)
    hasil_dekripsi = dekripsi_des(hasil_enkripsi, kunci)
    print(f"Hasil Dekripsi: {hasil_dekripsi}")
    print("=" * 50)