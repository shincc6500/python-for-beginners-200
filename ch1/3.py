"""
변수명 작성 실습
변수명의 첫 문자는 _ or 영문자로 시작되야 하며 대소문자를 구분함. 
또한 파이썬 예약어는 변수명으로 지정 불가능 
파이썬 예약어의 목록은 다음과 같음. - keyword package의 keyword.kwlist를 통해 확인 가능
['False', 'None', 'True', 'and', 'as', 'assert', 
'async', 'await', 'break', 'class', 'continue', 'def', 
'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 
'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 
'raise', 'return', 'try', 'while', 'with', 'yield']

또한 변수명을 파이썬 내장함수 명과 동일하게 작성할 시 해당 함수를 사용할 수 없는 문제가 발생함

"""


_myname = "samsung"
my_name = "홍길동"
My_name2 = "Hong gil_dong"
counter = 1
Counter = 2

print(_myname, "\n", my_name, "\n", My_name2, "\n", counter, "\n", Counter, sep="" )
