"""
실습 5 풀이: BMI 계산기
"""

height = int(input("키(cm)를 입력하세요: "))
weight = int(input("몸무게(kg)를 입력하세요: "))

# cm를 m로 변환: 175cm → 1.75m
height_m = height / 100

# BMI = 몸무게 / 키의 제곱
# ** 연산자: 거듭제곱 (1.75 ** 2 = 3.0625)
bmi = weight / height_m ** 2

print("키:", str(height) + "cm")
print("몸무게:", str(weight) + "kg")
print("BMI:", bmi)
