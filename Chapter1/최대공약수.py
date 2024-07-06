def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# 예제 사용법
print(gcd(48, 18))  # Output: 6
