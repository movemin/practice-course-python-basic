"""
실습 7: 할인 가격 계산

아래 3개 상품의 원래 가격과 할인율이 주어져 있습니다.
각 상품의 할인 가격을 계산하고, 총 결제 금액을 구하세요.

힌트: 할인 가격 = 원래 가격 * (1 - 할인율)
      총액은 += 연산자로 누적합니다.
"""

total = 0

# 상품 1: 노트북 1200000원, 10% 할인
price1 = 1200000
discount1 = 0.1

# 상품 2: 마우스 35000원, 20% 할인
price2 = 35000
discount2 = 0.2

# 상품 3: 키보드 55000원, 15% 할인
price3 = 55000
discount3 = 0.15

# 아래에 각 상품의 할인 가격을 계산하고 총액을 구하세요
# 노트북 가격 * (1-0.1)을 정수의 변수로 지정
discount_notebook = int(price1 * (1-discount1))
# 마우스 가격 * (1-0.2)을 정수의 변수로 지정
discount_mouth = int(price2 * (1-discount2))
# 키보드 가격 * (1-0.15)을 정수의 변수로 지정
discount_keyboard = int(price3 * (1-discount3))
# 다 더한 값 변수로 지정
total_discount = int(discount_notebook + discount_mouth + discount_keyboard)
# 해당 변수 출력
print(f"노트북: {discount_notebook}원")
print(f"마우스: {discount_mouth}원")
print(f"키보드: {discount_keyboard}원")
print(f"총 결제 금액: {total_discount}원")

"""
[실행 결과 예시]
노트북: 1080000원
마우스: 28000원
키보드: 46750원
총 결제 금액: 1154750원
"""
