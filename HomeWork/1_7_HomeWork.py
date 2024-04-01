# # def fact(n):
# #     print(f'call fact{n}')
# #     if n ==0:
# #         return 1
# #     else:
# #         return n*fact(n-1)

# # a = fact(4)
# # print(a)
# # print(" \n")

# # def dumpfact(fnk,n):
# #     return fnk(n)
# # fn1 = fact
# # print(fn1(5))
# # print(dumpfact(fn1,4))

# fnum = 3
# def dumtest():
#     global fnum
#     fnum = 2
#     print(f'{fnum}')
# def dumtest2():
#     fnum = 10
#     print(f'{fnum}')
# dumtest()
# print(f'out {fnum}')
# dumtest2()
# print(f'out {fnum}')

# def print_n_times(n):
#     for _ in range(n):
#         print('Hi')
# print_n_times(10)


# def print_n_times2(n,*messages):
#     for _ in range(n):
#         for message in messages:
#             print(message, end = " ")

#         print()

# print_n_times2(5,"HI","Python", "Bye", ".")

# def print_n_times(n = 10):
#     for _ in range(n):
#         print("hi")

# print_n_times()

# def return_test():
#     print('A')
#     return
#     print('B')

# return_test()
# print('C')
#A C

# def return_test():
#     x = 100
#     return x

# print('A', return_test())

# value = return_test()
# print('B',value)
#A 100 B 100

# def mul(*values):
#     result = 1
#     for i in range(4):
#         result *= values[i]
#     return result
    
# print(mul(5,7,9,10))


# def odd(*values):
#     odd_list = []
#     for i in range(8):
#         if i % 2 != 0 :
#             odd_list[i] = i
#     return odd_list

# print(odd(4,5,7,9,10,11,12,16,19))


def print_n_times(n):
    for _ in range(n):
        print('Hi')