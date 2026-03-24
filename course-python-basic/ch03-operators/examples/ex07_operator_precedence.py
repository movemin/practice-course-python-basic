# 연산자 우선순위 (Operator Precedence)
# 수학과 동일하게 곱셈/나눗셈이 덧셈/뺄셈보다 먼저 계산된다

# 괄호 없이
result1 = 2 + 3 * 4
print(result1)  # 14 (3 * 4 먼저)

# 괄호로 순서 변경
result2 = (2 + 3) * 4
print(result2)  # 20 (2 + 3 먼저)

# 헷갈리면 괄호를 쓰자!
# 괄호는 가독성도 높여준다
price = 10000
discount = 0.2
count = 3
total = (price * (1 - discount)) * count
print("총액:", int(total))  # 총액: 24000
