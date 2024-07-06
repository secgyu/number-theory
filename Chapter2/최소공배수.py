def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return abs(a * b) // gcd(a, b)

# 예제 사용법
print(lcm(12, 15))  # Output: 60
