"""
실습 2: 성적 등급

점수를 입력받아 등급을 출력하세요.
if/elif/else를 사용합니다.

[등급 기준]
90 이상: A
80 이상: B
70 이상: C
60 이상: D
60 미만: F
"""

score = int(input("점수를 입력하세요: "))

# 아래에 등급을 판정하여 출력하세요
# 점수 출력
print(f"점수: {score}")
# 만약 score >= 90 이면 A를 출력
if score >= 90 :
    print("등급: A")
# 만약 score >= 80 이면 B를 출력
elif score >= 80 :
    print("등급: B")
# 만약 score >= 60 이면 D를 출력
elif score >= 60 :
    print("등급: D")
# 그 외에는 F를 출력
else :
    print("등급: F")

## 조건이 여러 가지의 경우이면 아래가 우선순위인 것 같다.

"""
[실행 결과 예시] (입력: 85)
점수: 85
등급: B
"""
