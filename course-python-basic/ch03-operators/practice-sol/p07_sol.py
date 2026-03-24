"""
실습 7 풀이: 할인 가격 계산
"""

total = 0

price1 = 1200000
discount1 = 0.1

price2 = 35000
discount2 = 0.2

price3 = 55000
discount3 = 0.15

# 할인 가격 = 원래 가격 * (1 - 할인율)
# 예: 1200000 * (1 - 0.1) = 1200000 * 0.9 = 1080000
sale1 = int(price1 * (1 - discount1))
sale2 = int(price2 * (1 - discount2))
sale3 = int(price3 * (1 - discount3))

# += 연산자로 총액에 누적
total += sale1
total += sale2
total += sale3

print("노트북:", str(sale1) + "원")
print("마우스:", str(sale2) + "원")
print("키보드:", str(sale3) + "원")
print("총 결제 금액:", str(total) + "원")
