"""
자료형 및 자료형 출력
파이썬에는 5가지 기본 자료형이 있으며 자료형을 통해 여러 종류의 데이터를 구분하기 위한 분류임. 
1. 수치형 자료
    1) 정수형 상수 - 정수
    2) 실수형 상수 - 유리수와 무리수를 포함한 실수 
    3) 복소수형 상수 - 실수부 + 허수부 
2. 문자열 자료  
    - 한글자 이상의 문자나 숫자, 기호로 구성된 자료 
    이때 문자열 자료"1"과 수치형 자료 1은 다른 값임
3. 리스트 자료 (list)
    - [] 안에 임의의 객체를 순서 있게 나열한 자료형
4. 튜플 자료 (tuple)
    - ()를 사용하여 리스트와 유사하게 임의의 객체를 순서있게 나열한 자료형
    리스트와는 다르게 요소값 변경이 안됨. 
5. 사전 자료(dict)
    -{}를 사용하여 생성하는 키 : 값 쌍이 소요로 구성된 순서가 없는 자료형임.
    순서가 없어 인덱스 대신 키 값을 사용하여 접근 

"""

int_data =1
float_data = 3.14
comlplex_data = 1+5j

str_data1 = 'I love Python' # ''를 사용하여 문자열 자료형 생성
str_data2 = "안녕하세요 " # ""를 사용하여 문자열 자료형 생성

list_data = [1,2,3]
tuple_data = (1,2,3)
dict_data = {0:'False', 
             1:"True"} # key는 0,1 value는 'False', "True"

print(int_data) 
print(str_data1)

print(list_data) #리스트 전부를 출력
print(list_data[1]) #리스트 중 1번 위치의 값을 출력/ 리스트는 0번 부터 시작

print(dict_data) # dict data 전부를 출력
print(dict_data[1]) #dict_data에서 key 값이 1인 value를 출력

"""
출력값 
1
I love Python
[1, 2, 3]
2
{0: 'False', 1: 'True'}
True
"""