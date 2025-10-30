
def euclidean_gcd(a, b):
    while b:
        a, b = b, a % b
    return a

if __name__ == '__main__':
    a = 48
    b = 18

    print("--- Kasus GCD & Euclidean Algorithm ---")
    print(f"a = {a}, b = {b}")
    print(f"GCD({a}, {b}) = {euclidean_gcd(a, b)}")