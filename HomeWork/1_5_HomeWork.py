#for id, val in enumerate[1,2,3,4]: #enumerate는 index를 뽑아주는것
#    print(id,val)

#for val in [1,2,3,4]:
 #   print(val)

"""
a = [1,2,3,4]
b = [1,2,3,4]
c = list(zip(a,b))
print(c)
for v1,v in enumerate(zip(a,b,d)): #갯수가 같은 자료형을 묶어줌
    print(v1,v[0],v[1],v[2])
"""
"""
a = range(4,-10,-3)
print(list(a))
"""
"""
# 문제(1)
for i in range(10, 13):
    print("안녕")
"""
"""
#문제(2)
for i in range(0,10,3):
    print("안녕")
"""

"""
#문제(3)
for i in range(-10,-15,-2):
    print("안녕")
    
"""
"""
total = 0
for i in range(1,6,1):
    print("숫자를 입력하시오: ",i)
    num = i
    total += num
    avg = total/5
print("총합: ",total, "평균", avg)
"""
"""
N = int(input("N 정수를 입력하시오: "))
count = 0
for i in range(0,N):
    num = int(input("정수를 입력하시오: "))
    if num % 2 == 0:
        count = count + 1
print("짝수 정수의 총 갯수: ", count)
"""
"""
#문제(1)9
i = 1
while i < 10:
    print("안녕")
    i+=1
print(" ")
"""
"""
#문제(2)9
i = 1
while True:
    print("안녕")
    i += 1
    if i > 5: break
    

#문제(3)0
#문제(4)4
#문제(5)무한
"""
"""

#문제 1
a = 3
while a >0:
    print("안녕")
    a+=1
    if a > 5: break
"""
"""
a = 3
while (a<6):
    print("안녕")
    a +=1
    """
"""
a = 3
while True:
    print("안녕")
    a -= 1
    if a == 0: break

"""
"""
a = 100
while True:
    print("안녕")
    a-= 10
    if a == 70: break
"""
"""
total = 0
i = 0
while True:
    num = float(input("숫자를 입력하시오: "))
    total = total + num
    i += 1
    if i >4: break
avg = total / 5
print("총합: ", total, " 평균", avg)
"""

#문제1 9
#문제2 5
#문제3 12녕


"""
for a in range(6, 11):
    for b in range(2):
        print("안녕")


for a in range(2):
    for b in range(10,15):
        print("안녕")
"""