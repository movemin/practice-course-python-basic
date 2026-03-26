"""
실습 12: 복합 조건식

점수와 출석률을 입력받아
점수가 80점 이상이고 출석률이 90 초과이면 수료 가능,
그렇지 않으면 수료 불가를 출력하세요.
비교 연산자, 논리 연산자(and), if-else문을 활용합니다.
"""

score = int(input("점수 입력: "))
attendance = int(input("출석률 입력: "))

# 아래에 코드를 작성하세요

# 커트라인을 변수선언한다.
# score_cutline = int(80)
# attendance_cutline = int(90)
score_cutline = int(80)
attendance_cutline = int(90)

# 조건문으로 80 '이상' and 출석률 90 '초과'이면 "수료 가능"으로 출력되게끔 한다.
# if score >= score_cutline and attendance > attendance_cutline :
# print("수료 가능")
if score >= score_cutline and attendance > attendance_cutline :
    print("수료 가능")

# else로 그 외에는 불합격하게 한다
# else :
# print("수료 불가")
else :
    print("수료 불가")


"""
[실행 결과 예시] (입력: 85, 95)
수료 가능

[실행 결과 예시] (입력: 85, 80)
수료 불가
"""
