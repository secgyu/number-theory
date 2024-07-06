def extended_gcd(a, b):
    if a == 0:
        return b, 0, 1
    gcd, x1, y1 = extended_gcd(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return gcd, x, y

# 예제 사용법
gcd, x, y = extended_gcd(48, 18)
print(f"GCD: {gcd}, x: {x}, y: {y}")  # Output: GCD: 6, x: -1, y: 3
