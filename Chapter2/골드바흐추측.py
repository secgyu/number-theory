def goldbach_conjecture(n):
    primes = sieve_of_eratosthenes(n)
    for prime in primes:
        if (n - prime) in primes:
            return prime, n - prime
    return None

# 예제 사용법
print(goldbach_conjecture(28))  # Output: (5, 23) 또는 다른 소수 쌍
