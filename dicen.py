import random
import matplotlib.pyplot as plt

print(random.randint)

dice = [] #dice 정의
for i in range(5) :
    dice.append(random.randint(1,6))
print(dice)

plt.hist(dice, bins=6) #bins 란 가로축 구간 개수를 설정
plt.show()


#밑에서부턴 기온을 히스토그램으로 표현하기
f = open('hong.csv')
data = csv.reader(f)
next(data)
result = []

for row in data:
    if row[-1] != '':
        result.append(float(row[-1]))

plt.hist(result, bins=100, color='r')
plt.show() # 이렇게 하면 뭘 알고싶은지 알 수 없는 그래프가 나와버림

#같은 날짜의 데이터만 모아서 히스토그램으로 만들어보자
f = open('hong.csv')
data = csv.reader(f)
next(data)
aug = []

for row in data:
    month = row[0].split('-')[1] # 데이터에서 month 값을 찾고
    if row[-1] != '':
        if month == '08':
            aug.append(float(row[-1]))

plt.hist(aug, bins=100, color='r')
plt.show
