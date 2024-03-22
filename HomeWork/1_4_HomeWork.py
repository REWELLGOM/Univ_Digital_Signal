"""
x= 4
y = 0
p1 = (x + y) ** 2
p2 = (x - 1) == y + 3
p3 = x > 2 and y != 1
print(p1,p2,p3)
"""
"""
a = 5
b = -2
c = 1
d = 10
p1 = (2 * a + b / 2 - c * b > 20) and (d != 0)
p2 = (a * b - d / 10 + c * 2 == 10) or (a >= 5)
print(p1,p2)
"""
"""
x = int(input("정수를 입력하시오: "))

if x > 0:
    print("양수")
    print("입니다")
"""

"""
x = int(input("정숫값을 입력하시오: "))

if x % 5 == 0 :
    print(x, "은/는 5의 배수입니다.")
else:
    print(x, "은/는 5의 배수가 아닙니다")
"""
"""
seoul = int(input("서울의 온도를 입력하시오: "))
daegu = int(input("대구의 온도를 입력하시오: "))

avg = (seoul+daegu)/2
if avg>=33:
    print("폭염주의보입니다")
else:
    print("폭염주의보가 아닙니다")
"""
"""

grade = int(input("점수를 입력하시오: "))

if grade>=90:
    score = 'A'
elif grade >= 80 and grade <= 89 :
    score = 'B'
elif grade >= 70 and grade <= 79:
    scroe = 'C'
elif grade >= 60 and grade <=69:
    score = 'D'
else:
    score = 'F'

print(score)
"""

"""
x = int(input())
y = int(input())
if x < 20:
    if y == 1:
        x = x % 3
        y = 3
    elif y ==2:
        x = x * 2
        y = 2
    elif y ==3:
        x = x + 3
        y = 2
    else:
        x -= 5
        y +=1
else:
    y = y + 10
print(x,",",y)
"""
"""
a = float(input("첫번째 실수값을 입력하시오: "))
b = float(input("두번째 실수값을 입력하시오: "))
c = float(input("세번째 실수값을 입력하시오: "))

if a > 3 and b < 1000 and c == 100:
    result = (a+b+c)/3
    print("결과: ", result)
else:
    print("결과를 산출할 수 없습니다")
"""
"""
a = int(input())
b = int(input())

if a > 0:
    c = b*2*a
else:
    c = b*3*a+1
print(a,b)
print(c)
"""
"""

food = input("좋아하는 음식은 무엇인가요? ")

if food == "김치찌개":
    print("주재료: 김치")
elif food == "콩나물국박":
    print("주재료: 콩나물")
elif food == "된장찌개":
    print("주재료: 된장")
"""

num = int(input("숫자 입력: "))
if num > 0:
    print("양수")
elif num <0:
    print("음수")
else:
    print("0")


