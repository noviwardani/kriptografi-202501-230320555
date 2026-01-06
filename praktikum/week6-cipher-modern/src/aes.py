import secrets
import argparse

try:
    from Crypto.Cipher import AES
except Exception:
    AES = None


def pkcs7_pad(data, block_size=16):
    pad_len = block_size - (len(data) % block_size)
    return data + bytes([pad_len]) * pad_len


def pkcs7_unpad(data):
    if len(data) == 0:
        raise ValueError('Invalid padding (empty)')
    pad_len = data[-1]
    if pad_len < 1 or pad_len > 16:
        raise ValueError('Invalid padding length')
    if data[-pad_len:] != bytes([pad_len]) * pad_len:
        raise ValueError('Invalid padding bytes')
    return data[:-pad_len]


def aes_generate_key_128():
    return secrets.token_bytes(16)


def aes_encrypt_cbc(plaintext_bytes, key, iv=None):
    if AES is None:
        raise ImportError('PyCryptodome is required: pip install pycryptodome')
    if len(key) != 16:
        raise ValueError('AES-128 key must be 16 bytes')
    if iv is None:
        iv = secrets.token_bytes(16)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    ct = cipher.encrypt(pkcs7_pad(plaintext_bytes, 16))
    return iv + ct


def aes_decrypt_cbc(iv_and_ct, key):
    if AES is None:
        raise ImportError('PyCryptodome is required: pip install pycryptodome')
    if len(key) != 16:
        raise ValueError('AES-128 key must be 16 bytes')
    iv = iv_and_ct[:16]
    ct = iv_and_ct[16:]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    pt_padded = cipher.decrypt(ct)
    return pkcs7_unpad(pt_padded)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='AES-128 CBC demo: encrypt/decrypt teks')
    parser.add_argument('-t', '--text', type=str, help='teks yang akan dienkripsi (opsional)')
    parser.add_argument('--key-hex', type=str, help='kunci AES-128 hex (opsional)')
    args = parser.parse_args()

    if AES is None:
        print('PyCryptodome tidak ditemukan. Install: pip install pycryptodome')
        exit(1)

    if args.text:
        plaintext = args.text.encode('utf-8')
    else:
        plaintext = input('Masukkan teks yang akan dienkripsi: ').encode('utf-8')

    if args.key_hex:
        key = bytes.fromhex(args.key_hex)
        if len(key) != 16:
            print('Kunci hex tidak valid: harus 16 bytes (32 hex chars)')
            exit(1)
    else:
        key = aes_generate_key_128()

    iv_ct = aes_encrypt_cbc(plaintext, key)
    print('=== HASIL ===')
    print('Kunci AES-128 (hex):', key.hex())
    print('Ciphertext (hex):', iv_ct.hex())

    # contoh dekripsi
    recovered = aes_decrypt_cbc(iv_ct, key)
    print('Dekripsi (hasil):', recovered.decode('utf-8'))