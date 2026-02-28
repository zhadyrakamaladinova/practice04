# 1. Squares up to N
def squares_up_to(N):
    for i in range(N + 1):
        yield i * i

print(list(squares_up_to(5)))


# 2. Even numbers between 0 and n 
def evens(n):
    for i in range(0, n + 1, 2):
        yield i

n = int(input("Enter n: "))
print(",".join(str(x) for x in evens(n)))


# 3. Divisible by both 3 and 4 between 0 and n
def div_3_and_4(n):
    for i in range(n + 1):
        if i % 3 == 0 and i % 4 == 0:
            yield i

n = int(input("Enter n: "))
print(list(div_3_and_4(n)))


# 4. squares(a, b) generator
def squares(a, b):
    for i in range(a, b + 1):
        yield i * i

for val in squares(3, 7):
    print(val)


# 5. Countdown from n to 0
def countdown(n):
    while n >= 0:
        yield n
        n -= 1

n = int(input("Enter n: "))
for val in countdown(n):
    print(val)