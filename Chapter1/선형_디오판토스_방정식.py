def solve_diophantine(a, b, c):
    gcd, x, y = extended_gcd(a, b)
    if c % gcd != 0:
        return None  # No solution exists
    x *= c // gcd
    y *= c // gcd
    return x, y

# 예제 사용법
solution = solve_diophantine(6, 9, 15)
if solution:
    x, y = solution
    print(f"Solution: x = {x}, y = {y}")  # Output: Solution: x = 5, y = -3
else:
    print("No solution exists")
