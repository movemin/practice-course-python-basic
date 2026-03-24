"""
실습 2 풀이: 변수의 자료형 확인하기
"""

# 파이썬의 4가지 기본 자료형
a = "파이썬"   # str: 문자열 (따옴표로 감싼다)
b = 2026       # int: 정수 (소수점 없는 숫자)
c = 3.14       # float: 실수 (소수점 있는 숫자)
d = False      # bool: 참/거짓 (True 또는 False)

# type()은 변수의 자료형을 알려주는 함수
print(a, type(a))  # 파이썬 <class 'str'>
print(b, type(b))  # 2026 <class 'int'>
print(c, type(c))  # 3.14 <class 'float'>
print(d, type(d))  # False <class 'bool'>
