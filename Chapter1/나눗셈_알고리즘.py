def division_algorithm(dividend, divisor):
    quotient = dividend // divisor
    remainder = dividend % divisor
    return quotient, remainder

# 예제 사용법
quotient, remainder = division_algorithm(20, 3)
print(f"Quotient: {quotient}, Remainder: {remainder}")  # Output: Quotient: 6, Remainder: 2
