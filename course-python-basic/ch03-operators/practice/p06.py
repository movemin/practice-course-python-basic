"""
실습 6: 시간 변환

초(seconds)를 입력받아 시, 분, 초로 변환하여 출력하세요.

힌트: //(몫)과 %(나머지)를 사용합니다.
      1시간 = 3600초, 1분 = 60초
"""

seconds = int(input("초를 입력하세요: "))

# 아래에 시, 분, 초로 변환하여 출력하세요
# 초를 시간으로 변환
hour = int(seconds/3600)
# 입력값을 시간으로 나눈 나머지를 분으로 변환
hour_seconds = int(seconds%3600)
minute = int(hour_seconds/60)
#초는 나머지를 활용하여 변수지정
seconds2 = int(hour_seconds%60)
# 시간, 분, 초를 출력.
print(seconds,"초")
print(f"{hour}시간 {minute}분 {seconds2}초")

"""
[실행 결과 예시] (입력: 3725)
3725초
= 1시간 2분 5초
"""
