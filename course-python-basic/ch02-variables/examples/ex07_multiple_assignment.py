# 여러 변수에 값 할당

# 여러 변수에 동시에 다른 값 할당
name, age, major = "홍길동", 20, "글로벌시스템융합"
print(name)
print(age)
print(major)

# 여러 변수에 같은 값 할당
a = b = c = 0
print(a, b, c)

# 두 변수의 값 교환 (swap)
x = 10
y = 20
print("교환 전:", x, y)

x, y = y, x
print("교환 후:", x, y)
