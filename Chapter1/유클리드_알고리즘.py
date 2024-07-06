def euclidean_gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# 예제 사용법
print(euclidean_gcd(48, 18))  # Output: 6
