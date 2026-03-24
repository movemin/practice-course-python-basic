"""
실습 2 풀이: 거스름돈 계산
"""

price = int(input("물건 가격: "))
paid = int(input("지불 금액: "))

change = paid - price
print("거스름돈:", str(change) + "원")

# // (몫): 큰 단위부터 몇 개인지 구한다
# %  (나머지): 큰 단위로 거슬러 준 뒤 남은 금액을 구한다

# 예: 2700원 → 2700 // 1000 = 2개, 2700 % 1000 = 700원 남음
bill_1000 = change // 1000
change = change % 1000    # 1000원으로 거슬러 준 뒤 남은 금액

# 700원 → 700 // 500 = 1개, 700 % 500 = 200원 남음
coin_500 = change // 500
change = change % 500     # 500원으로 거슬러 준 뒤 남은 금액

# 200원 → 200 // 100 = 2개
coin_100 = change // 100

print("1000원:", str(bill_1000) + "개")
print("500원:", str(coin_500) + "개")
print("100원:", str(coin_100) + "개")
