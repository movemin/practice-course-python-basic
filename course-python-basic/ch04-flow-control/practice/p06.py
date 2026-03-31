"""
실습 6: 가위바위보

사용자가 가위, 바위, 보 중 하나를 입력하면
컴퓨터(바위 고정)와 비교하여 결과를 출력하세요.

힌트: if/elif/else를 사용합니다.
"""

computer = "바위"
user = input("가위, 바위, 보 중 하나를 입력하세요: ")

# 아래에 승패를 판정하여 출력하세요

# 가위, 바위, 보 변수선언한다
scissors = "가위"
rock = "바위"
paper = "보"
# 이길 때까지 반복(while)하도록 항상 조건은 True로 설정해준다.
while True:
# 계속 입력할 수 있게끔 한다.
    user = input("가위, 바위, 보 중 하나를 입력하세요: ")
# 조건문을 활용하여 가위를 낼 경우 졌다고 한다.
    if user == scissors:
        print("졌습니다")
# 다른 조건문을 사용하여 묵을 낼 경우 비겼다고 한다.   
    elif user == rock:
        print("비겼습니다")
# 이기면 끝나게끔 보를 내면 이겼다고 출력한 후 break로 마무리한다.
    elif user != paper and user != scissors and user != rock:
        print("다시 입력하세요")
    else:
        print("이겼습니다")
        break


"""
[실행 결과 예시] (입력: 가위)
컴퓨터: 바위
나: 가위
결과: 졌습니다

[실행 결과 예시] (입력: 보)
컴퓨터: 바위
나: 보
결과: 이겼습니다
"""
