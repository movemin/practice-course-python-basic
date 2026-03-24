# 논리 연산자 (Logical Operators)
# 여러 조건을 조합할 때 사용한다

age = 20
has_id = True

# and: 둘 다 참이면 True
print(age >= 18 and has_id)  # True

# or: 하나라도 참이면 True
print(age >= 18 or has_id)   # True

# not: 반대로 뒤집기
print(not has_id)             # False

# 활용 예시: 놀이기구 탑승 조건
height = 140
weight = 50
can_ride = height >= 130 and weight <= 100
print("탑승 가능:", can_ride)  # 탑승 가능: True
