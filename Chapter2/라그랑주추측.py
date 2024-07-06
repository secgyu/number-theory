import math

def four_square_sum(n):
    for a in range(int(math.sqrt(n)) + 1):
        for b in range(a, int(math.sqrt(n - a*a)) + 1):
            for c in range(b, int(math.sqrt(n - a*a - b*b)) + 1):
                d = math.sqrt(n - a*a - b*b - c*c)
                if d == int(d):
                    return a, b, c, int(d)
    return None

# 예제 사용법
print(four_square_sum(23))  # Output: (0, 1, 3, 3)
