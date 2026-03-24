"""
실습 6 풀이: 자료형 변환 활용하기
"""

# [1] 총 금액 계산
# 문자열 "4500"과 "3"은 곱셈이 안 된다 → int()로 정수 변환
price = "4500"
quantity = "3"

print(int(price) * int(quantity))  # 13500

# [2] 문자열 연결
# 숫자 95를 문자열과 이어붙이려면 str()로 변환해야 한다
name = "홍길동"
score = 95

print(name + "님의 점수는 " + str(score) + "점입니다.")

# [3] 두 숫자 입력받아 합계 출력
# input()은 항상 문자열을 반환하므로 int()로 변환해야 계산이 된다
num1 = int(input("첫 번째 숫자: "))
num2 = int(input("두 번째 숫자: "))

print("합계:", num1 + num2)
