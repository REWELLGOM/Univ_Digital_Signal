"""
mylist=[10,0,-12,"list","char","100",50]
mylist[-1]
print(mylist[6])
print(mylist[:4])
print(mylist[5:6])
print(mylist[3:6])
"""

"""

mylist=[10,0,-12,"list","char","100",50]
print(mylist[-1])
print(mylist[-7:-3])
print(mylist[-2:])
print(mylist[-4:-1])
"""



"""
myList = [["aaa", "bbb", "ccc", "ddd"], [40,30,20,10]]
print(myList[0][1])
print(myList[1][3])
print(myList[0][1:3])
print(myList[1][1:4])

"""
"""

myList = [["aaa", "bbb", "ccc", "ddd"], [40,30,20,10]]
print(myList[-2][-3])
print(myList[-1][-1])
print(myList[-2][-3:-1])
print(myList[-1][-3:])
"""

"""

MyList=[[200,100,["AAA","BBB","CCC","DDD"]],"C++"]
print(MyList[0][2][1])
print(MyList[0][2][3])

print(MyList[-2][-1][-3])
print(MyList[-2][-1][-1])
"""
"""

myList = [100,200,300]
myList[1] = 2
print(myList)
"""

myList = [100,200,300,400,500]
"""
del myList[-1]
print(myList)
"""
"""
del myList[2:4]
print(myList)

"""
"""
del myList[1:]
print(myList)
"""
"""
del myList[:3]
print(myList)
"""
"""
del myList[:]
print(myList)
"""

myList = []
myList.append(0)
myList.append(10)
myList.append(20)
myList.append(50)
myList.append(30)
myList.append(40)
myList.insert(2,-100)
print(myList)
