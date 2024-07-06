def sum_of_primes(limit):
    primes = sieve_of_eratosthenes(limit)
    return sum(primes)

# 예제 사용법
print(sum_of_primes(10))  # Output: 17
