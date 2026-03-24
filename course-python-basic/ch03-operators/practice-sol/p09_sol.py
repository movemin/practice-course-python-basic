"""
실습 9 풀이: 택시 요금 계산
"""

distance = int(input("이동 거리(m)를 입력하세요: "))

base_fare = 4800    # 기본요금
base_dist = 1600    # 기본요금에 포함된 거리

# 초과 거리 계산: 총 거리 - 기본 거리
# 예: 3500 - 1600 = 1900m 초과
extra_dist = distance - base_dist

# 초과 거리에 대해 131m마다 100원 추가
# 예: 1900 // 131 = 14 → 14 * 100 = 1400원 추가
extra_fare = (extra_dist // 131) * 100

fare = base_fare + extra_fare

print("이동 거리:", str(distance) + "m")
print("택시 요금:", str(fare) + "원")
