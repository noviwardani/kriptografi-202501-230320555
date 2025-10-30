def extended_euclidean(a, b):
    """
    Menghitung Extended Euclidean Algorithm untuk menemukan x, y sehingga ax + by = gcd(a, b).
    Juga mengembalikan modular inverse dari a mod b jika gcd(a, b) = 1.
    """
    if a == 0:
        return b, 0, 1
    
    gcd, x1, y1 = extended_euclidean(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return gcd, x, y

def modular_inverse(a, m):
    """Menghitung modular inverse dari a mod m"""
    gcd, x, y = extended_euclidean(a, m)
    if gcd != 1:
        raise Exception('Modular inverse tidak ada')
    else:
        return (x % m + m) % m

if __name__ == '__main__':
    a = 7
    m = 26

    print("--- Kasus Extended Euclidean & Modular Inverse ---")
    print(f"a = {a}, m = {m}")
    try:
        inverse = modular_inverse(a, m)
        print(f"Modular inverse dari {a} mod {m} adalah {inverse}")
        print(f"Verifikasi: ({a} * {inverse}) mod {m} = {(a * inverse) % m}")
    except Exception as e:
        print(e)