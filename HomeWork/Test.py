# a = list(range(10))
# print(a)

# b = list(filter(lambda x:x%2==0,a))
# print(b)

# c = tuple(map(lambda x:x+2,a))
# print(c)

fid = open('basic.txt','w')
fid.write('haha \n')
print('babo',file = fid)
fid.close()

fid = open('basic.txt', 'r')
lines = fid.readlines()
for line in lines:
    print(line,end = ' ')
fid.close()

with open('basic.txt','r') as fid:  #with쓰면 close없어도 된다
    lines = fid.readlines()
    for line in lines:
        print(line)

try:
    with open('basic2.txt','r') as fid:
        lines = fid.readlines()
        for line in lines:
            print(line)
except FileNotFoundError:
    print('File Not Exist!')


# info.csv 파일을 읽기 모드로 열기
with open('info.csv', 'r') as data_file:
    for line in data_file:
        name, weight, height = line.strip().split(',')
        # 데이터가 누락되었을 경우를 대비한 에러 처리
        if (not name) or (not weight) or (not height):
            continue  # 누락된 데이터가 있는 경우 다음 라인으로 넘어감

        bmi = float(weight) / ((float(height)/100) ** 2)  # BMI 계산
        result = '정상 체중'
        
        # BMI 지수에 따른 체중 분류
        if bmi >= 25:
            result = '과체중'
        elif bmi < 18.5:
            result = '저체중'

        # 결과 출력을 위한 문자열 포매팅
        output = "\n".join([f'이름: {name}', f'몸무게: {weight}', f'키: {height}', f'BMI: {bmi:.1f}', f'결과: {result}'])
        print('-' * 40, '\n', output)
    