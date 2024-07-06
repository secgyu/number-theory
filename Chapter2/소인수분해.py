def prime_factors(n):
    factors = []
    # 2로 나누기
    while n % 2 == 0:
        factors.append(2)
        n //= 2
    # 3 이상 홀수로 나누기
    for i in range(3, int(n**0.5) + 1, 2):
        while n % i == 0:
            factors.append(i)
            n //= i
    # 나머지가 소수인 경우
    if n > 2:
        factors.append(n)
    return factors

# 예제 사용법
print(prime_factors(56))  # Output: [2, 2, 2, 7]
print(prime_factors(315))  # Output: [3, 3, 5, 7]
