# if/elif/else — 여러 조건 분기

score = int(input("점수를 입력하세요: "))

if score >= 90:
    print("A 등급")
elif score >= 80:
    print("B 등급")
elif score >= 70:
    print("C 등급")
elif score >= 60:
    print("D 등급")
else:
    print("F 등급")
