"""
myT = (50,40,30,20,10,0)
print(myT[5])
print(myT[:4])
print(myT[2:])
print(myT[3:5])

print(myT[-1])
print(myT[:-2])
print(myT[-4:])
print(myT[-3:-1])
"""
"""
myT = (2)
print(myT*5)

myT = ([2])
print(myT*5)
"""
"""
myTuple = (100,200,300)
del myTuple[0]
#튜플은 한 번 생성되면 요소값을 변경할 수 없는 자료형
"""

"""
myDict = {"scores": [100,90,80], "name":("Kim","Hong","Lee")}
scoresList = myDict['scores']
nameList = myDict['name']
print("name = ", nameList[1], "==>", "score = ", scoresList[1])
"""
"""

my_dict = {'name': 'John', 'age': 30}
print(my_dict['name'])
"""
"""
my_dict = {'name': 'John', 'age': 30}
my_dict['age'] = 31
print(my_dict)
"""
"""
my_dict = {'name': 'John', 'age': 30}
del my_dict['age']
print(my_dict)
"""

"""
my_dict = {'name': 'John', 'age': 30}
my_dict['location'] = 'Seoul'
print(my_dict)
"""

"""
my_dict = {'name': 'John', 'age': 30}
print(my_dict.keys())
"""
"""
my_dict = {'name': 'John', 'age': 30}
print(my_dict.values())
"""

my_dict = {'name': 'John', 'age': 30}
for key, value in my_dict.items():
    print(f"{key}: {value}")