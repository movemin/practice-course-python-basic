# 중첩 조건문 — if 안의 if

age = int(input("나이를 입력하세요: "))
has_ticket = input("티켓이 있나요? (y/n): ")

if age >= 18:
    if has_ticket == "y":
        print("입장 가능합니다")
    else:
        print("티켓을 구매해주세요")
else:
    print("18세 이상만 입장 가능합니다")
