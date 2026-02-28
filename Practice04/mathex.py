import math

# 1. Degree to radian
degree = float(input("Input degree: "))
print(f"Output radian: {math.radians(degree):.6f}")

# 2. Area of trapezoid
h = float(input("Height: "))
b1 = float(input("Base, first value: "))
b2 = float(input("Base, second value: "))
print(h * (b1 + b2) / 2)

# 3. Area of regular polygon
n = int(input("Input number of sides: "))
s = float(input("Input the length of a side: "))
area = (n * s**2) / (4 * math.tan(math.pi / n))
print(f"The area of the polygon is: {area:.0f}")

# 4. Area of parallelogram
base = float(input("Length of base: "))
height = float(input("Height of parallelogram: "))
print(float(base * height))