"""
들여쓰기
파이썬에는 제어문이나 함수 및 클레스에서 실행 코드 부분을 구분해주는 괄호가 없음. 
이를 대신하여 들여쓰기 indentation으로 괄호를 대신함. 
제어문이나 함수이름, 클래스 이름과 실행 코드 부분을 콜론(:)으로 구분함. 
"""

list_data = ["a", "b", "c"]
if "a" in list_data:
    print("a가 list_data에 있습니다")
    print(list_data)
else:
    print("a가 list_data에 없습니다")

"""
다음과 같이 들여쓰기 위치가 맞지 않는 경우 오류가 발생함. 
list_data = ["a", "b", "c"]
if "a" in list_data:
    print("a가 list_data에 있습니다")
        print(list_data)
else:
    print("a가 list_data에 없습니다")"""