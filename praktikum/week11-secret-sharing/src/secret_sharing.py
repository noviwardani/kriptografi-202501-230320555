import secrets
from typing import List, Tuple

PRIME = 2**521 - 1
Share = Tuple[int, int]


def _eval_poly(coeffs: List[int], x: int, p: int) -> int:
    y = 0
    for a in reversed(coeffs):
        y = (y * x + a) % p
    return y


def _encode_secret_to_int(secret: str) -> int:
    data = secret.encode("utf-8")
    return int.from_bytes(data, "big")


def _decode_int_to_secret(secret_int: int) -> str:
    if secret_int < 0:
        raise ValueError("Secret integer invalid")
    if secret_int == 0:
        return ""

    blen = (secret_int.bit_length() + 7) // 8
    data = secret_int.to_bytes(blen, "big")
    try:
        return data.decode("utf-8")
    except UnicodeDecodeError:
        raise ValueError("Decode gagal: shares kurang dari threshold atau data corrupt")


def split_secret(secret: str, k: int, n: int, p: int = PRIME) -> List[Share]:
    if not (2 <= k <= n):
        raise ValueError("Harus 2 <= k <= n")
    if n > 255:
        raise ValueError("n maksimal 255")

    a0 = _encode_secret_to_int(secret)
    if a0 >= p:
        raise ValueError("Secret terlalu besar untuk modulus p (secret kepanjangan)")

    coeffs = [a0] + [secrets.randbelow(p) for _ in range(k - 1)]

    shares: List[Share] = []
    for x in range(1, n + 1):
        y = _eval_poly(coeffs, x, p)
        shares.append((x, y))
    return shares


def _lagrange_interpolate_at_0(shares: List[Share], p: int) -> int:
    total = 0
    k = len(shares)

    for i in range(k):
        xi, yi = shares[i]
        num = 1
        den = 1

        for j in range(k):
            if i == j:
                continue
            xj, _ = shares[j]
            num = (num * (-xj)) % p
            den = (den * (xi - xj)) % p

        inv_den = pow(den, -1, p)
        total = (total + yi * num * inv_den) % p

    return total


def recover_secret(shares: List[Share], k: int, p: int = PRIME) -> str:
    if len(shares) < k:
        raise ValueError("Shares kurang dari threshold k")

    used = shares[:k]  # ambil k share yang kamu kasih (urutan input)
    secret_int = _lagrange_interpolate_at_0(used, p)
    return _decode_int_to_secret(secret_int)


def format_share(share: Share) -> str:
    x, y = share
    return f"{x}-{y:x}"


def parse_share(s: str) -> Share:
    s = s.strip()
    x_str, y_hex = s.split("-", 1)
    return int(x_str), int(y_hex, 16)


def input_int(prompt: str, min_val: int = None, max_val: int = None) -> int:
    while True:
        try:
            v = int(input(prompt))
            if min_val is not None and v < min_val:
                print(f"Minimal {min_val}.")
                continue
            if max_val is not None and v > max_val:
                print(f"Maksimal {max_val}.")
                continue
            return v
        except ValueError:
            print("Masukkan angka yang valid.")


def menu_split():
    secret = input("\nMasukkan secret: ")
    k = input_int("Masukkan k (threshold): ", 2)
    n = input_int("Masukkan n (jumlah shares): ", k, 255)

    shares = split_secret(secret, k, n)
    print("\n=== HASIL SHARES ===")
    print(f"Secret dibagi jadi {n} shares, butuh minimal {k} shares untuk rekonstruksi.\n")
    for i, sh in enumerate(shares, 1):
        print(f"Share {i}: {format_share(sh)}")

    print("\nTips: copy share (format x-yhex) buat nanti direkonstruksi.")


def menu_recover():
    k = input_int("\nMasukkan k (threshold yang dipakai waktu split): ", 2)
    m = input_int("Berapa share yang kamu punya (>= k): ", k, 255)

    print("\nMasukkan share satu per satu (format: x-yhex). Contoh: 2-1a2b3c...")
    shares: List[Share] = []
    seen_x = set()

    for i in range(m):
        while True:
            raw = input(f"Share {i+1}: ").strip()
            try:
                sh = parse_share(raw)
                x, _ = sh
                if x in seen_x:
                    print("x tidak boleh duplikat. Masukkan share lain.")
                    continue
                seen_x.add(x)
                shares.append(sh)
                break
            except Exception:
                print("Format salah. Harus 'x-yhex' (contoh: 2-1a2b3c...). Coba lagi.")

    # Pakai k share pertama dari yang kamu input
    recovered = recover_secret(shares, k)
    print("\n=== HASIL REKONSTRUKSI ===")
    print("Secret:", recovered)


def main():
    print("=" * 50)
    print("SHAMIR SECRET SHARING (SPLIT & RECOVER)")
    print("=" * 50)
    print("1) Buat shares (split secret)")
    print("2) Rekonstruksi dari shares (recover secret)")

    pilihan = input("\nPilih menu (1/2): ").strip()
    try:
        if pilihan == "1":
            menu_split()
        elif pilihan == "2":
            menu_recover()
        else:
            print("Pilihan tidak valid.")
    except Exception as e:
        print("\nError:", e)


if __name__ == "__main__":
    main()