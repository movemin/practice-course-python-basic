# 변수 이름 규칙
# 변수 이름을 정할 때 지켜야 하는 규칙이 있습니다.

# [올바른 변수명]
student_name = "홍길동"     # 소문자와 언더스코어 조합 (권장)
studentName = "홍길동"      # 카멜 케이스
age1 = 20                   # 숫자를 포함할 수 있음 (단, 첫 글자 불가)
_score = 95                 # 언더스코어로 시작 가능

print(student_name)
print(studentName)
print(age1)
print(_score)

# [잘못된 변수명] - 아래 코드는 오류가 발생합니다
# 1age = 20          # 숫자로 시작 불가
# student-name = ""  # 하이픈(-) 사용 불가
# class = ""         # 예약어(파이썬 키워드) 사용 불가

# ----------------------------------------
# [권장 사항] 좋은 변수 이름 짓기
# 규칙은 아니지만, 변수 이름만 보고 어떤 값인지 알 수 있도록 짓는 것이 좋습니다.
# ----------------------------------------

# 나쁜 예 - 변수 이름만으로 의미를 알 수 없음
a = 20
b = "홍길동"
x = 95

# 좋은 예 - 변수 이름만으로 의미가 드러남
age = 20
user_name = "홍길동"
total_score = 95

# ----------------------------------------
# [권장 사항] 표기법 (Naming Convention)
# ----------------------------------------

# 스네이크 표기법 (snake_case) - 단어 사이를 언더스코어(_)로 연결
# 파이썬에서 권장하는 표기법입니다 (PEP 8 스타일 가이드)
student_name = "홍길동"
total_score = 95
is_logged_in = True

# 카멜 표기법 (camelCase) - 두 번째 단어부터 첫 글자를 대문자로
# Java, JavaScript 등 다른 언어에서 주로 사용합니다
studentName = "홍길동"
totalScore = 95
isLoggedIn = True

print("스네이크 표기법:", student_name, total_score, is_logged_in)
print("카멜 표기법:", studentName, totalScore, isLoggedIn)
