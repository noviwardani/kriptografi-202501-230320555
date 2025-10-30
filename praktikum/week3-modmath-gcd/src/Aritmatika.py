
def modular_add(a, b, m):
    return (a + b) % m

def modular_sub(a, b, m):
    return (a - b + m) % m

def modular_mul(a, b, m):
    return (a * b) % m

def modular_exp(base, exp, m):
    return pow(base, exp, m)

if __name__ == '__main__':
    a = 15
    b = 7
    m = 10

    print("--- Kasus Modular Arithmetic ---")
    print(f"a = {a}, b = {b}, m = {m}")
    print(f"({a} + {b}) mod {m} = {modular_add(a, b, m)}")
    print(f"({a} - {b}) mod {m} = {modular_sub(a, b, m)}")
    print(f"({a} * {b}) mod {m} = {modular_mul(a, b, m)}")
    print(f"({a}^{b}) mod {m} = {modular_exp(a, b, m)}")