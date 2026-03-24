# 묵시적 형변환과 명시적 형변환

# --- 묵시적 형변환 (자동 변환) ---
# 정수와 실수를 연산하면 결과는 자동으로 실수가 된다
result = 3 + 2.0
print(result)       # 5.0
print(type(result))  # <class 'float'>

# --- 명시적 형변환 (직접 변환) ---
# 문자열과 숫자는 자동 변환되지 않는다
age = 20
# print("나이: " + age)  # 오류 발생!
print("나이: " + str(age))    # str()로 변환 필요

# 문자열 숫자를 계산하려면 int() 또는 float()로 변환
price = "1500"
count = "3"
total = int(price) * int(count)
print("총액: " + str(total))  # 총액: 4500
