#a = [1,2,3,4]
#print(*tuple(a)) # *은 언팩킹하라는 소리임

#b,c,d,e = tuple(a)

#for i in range(1,10):
#    a = [f'{i:2d}*{j:2d} = {i*j:2d}' for j in range(1,10)]
#   print(*tuple(a))

#a = [j for j in range(1,100) if j%2 == 0] # 1부터 100에서 2로 나누어떨어지는걸 j에 넣어라
#print(a)

#def print_star3(mark, *numbers):
#    for number in numbers:
#        for _ in range(number):
#            print(mark, end='')
#        print()
#print_star3('*',1,2,5,7)


a = [4,5,62,1,3,4]
b = sorted(a,reverse=False)
print(b)

# static int a 할때 static은 프로그램이 종료되도 유지됨 그 코드 블럭 {} 이거 안에서만 사용가능