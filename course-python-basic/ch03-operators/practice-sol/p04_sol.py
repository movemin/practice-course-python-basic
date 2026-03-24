"""
실습 4 풀이: 합격 판정
"""

score = int(input("시험 점수: "))

print("점수:", score)

# 비교 연산자는 결과로 True 또는 False를 반환한다
print("60점 이상인가?", score >= 60)
print("100점 이하인가?", score <= 100)

# and: 두 조건이 모두 참일 때만 True
# 60점 이상 "그리고" 100점 이하 → 둘 다 만족해야 합격
print("합격 조건 충족:", score >= 60 and score <= 100)
