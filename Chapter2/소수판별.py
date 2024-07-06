def is_prime_basic(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# 예제 사용법
print(is_prime_basic(17))  # Output: True
