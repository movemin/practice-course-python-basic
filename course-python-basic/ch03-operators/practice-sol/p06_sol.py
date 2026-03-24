"""
실습 6 풀이: 시간 변환
"""

seconds = int(input("초를 입력하세요: "))

# 거스름돈 계산과 같은 패턴: 큰 단위부터 // 와 % 로 분리
# 예: 3725초 → 3725 // 3600 = 1시간, 3725 % 3600 = 125초 남음
hours = seconds // 3600
remaining = seconds % 3600    # 시간을 빼고 남은 초

# 125초 → 125 // 60 = 2분, 125 % 60 = 5초 남음
minutes = remaining // 60
secs = remaining % 60         # 분을 빼고 남은 초

print(str(seconds) + "초")
print("=", str(hours) + "시간", str(minutes) + "분", str(secs) + "초")
