# break와 continue — 반복 제어

# break: 반복을 즉시 종료
print("== break 예제 ==")
for i in range(1, 11):
    if i == 6:
        break
    print(i)
# 출력: 1 2 3 4 5

print("---")

# continue: 현재 회차를 건너뛰고 다음으로
print("== continue 예제 ==")
for i in range(1, 11):
    if i % 3 == 0:
        continue
    print(i)
# 출력: 1 2 4 5 7 8 10 (3의 배수 제외)
