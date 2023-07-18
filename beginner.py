# 스칼라곱
import sys

N = int(sys.stdin.readline())
firstScaler = list(map(int, (sys.stdin.readline()).split()))
secondScaler = list(map(int, (sys.stdin.readline()).split()))

print(sum([firstScaler[i] * secondScaler[i]  for i in range(N)]))

##################### 
# 리그   
import sys

N = 4
team = []
for i in range(N):
    oneTeam = list(map(int, (sys.stdin.readline()).split()))
    team.append(oneTeam)

score = [0] * 4
for i in range(N):
    for j in range(N):
        if i == j:
            continue
        elif team[i][j] > team[j][i]:
            score[i] += 3
        elif team[i][j] == team[j][i]:
            score[i] += 1

for i in score:
    print(i, end = ' ')

##################
#책상수리
import sys

temp = list(map(int, (sys.stdin.readline()).split()))
length = list(map(int, (sys.stdin.readline()).split()))

min_length = 1000000001
for l in length:
    if temp[1] <= l and l < min_length:
        min_length = l

print(min_length)

################
# 종이 자르기
import sys

temp = list(map(int, (sys.stdin.readline()).split()))
first = list(map(int, (sys.stdin.readline()).split()))
second = list(map(int, (sys.stdin.readline()).split()))

if first[0] == second[0] and (first[0] == 0 or first[0] == temp[1]):
    print('NO')
elif first[1] == second[1] and (first[1] == 0 or first[1] == temp[0]):
    print('NO')
else:
    print('YES')

###################
#간단한 수학문제
import sys

N, K = map(int, (sys.stdin.readline()).split())
print((K//N) * N)

################
# 디스플레이 제작
import sys

N = int(sys.stdin.readline())
a = 0
b = 0

for i in range(1,N+1):
    if i == b:
        break
    elif N % i == 0:
        a = i
        b = N//i
        if a == b:
            break
print(a, b)
#################
# 암호해독
import sys

word = sys.stdin.readline().strip()
start = 0
i = 1
answer = ''
while(start != len(word)):
    answer += word[start]
    start += i
    i += 1
print(answer)
#################
# DNA
import sys

N = int(sys.stdin.readline())
word = sys.stdin.readline().strip()

dna = {'A': 'T', 'T' : 'A', 'G' : 'C', 'C': 'G'}

for w in word:
    print(dna[w], end='')

#################
# 배열 평준화
import sys

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))

A.sort()
print(min(A[-1] - A[0], A[-2] - A[0], A[-1] - A[1]))

#################
# 위치 추적
import sys

N = int(sys.stdin.readline())
distance = [0]*2

for i in range(N):
    D, L = map(int, sys.stdin.readline().split())
    if D == 1:
        distance[0] += L
    elif D == 3:
        distance[0] -= L
    elif D == 2:
        distance[1] += L
    elif D == 4:
        distance[1] -= L
print(distance[0], distance[1])

#################
# 팀나누기
import sys
from itertools import combinations


score = list(map(int, (sys.stdin.readline().split())))
com = list(combinations(score, 3))

for i in range(10):
    temp = score.copy()
    for j in com[i]:
        temp.remove(j)
    if sum(com[i]) == sum(temp):
        print('possible')
        break
    if i == 9:
        print('impossible')

#################
# 가장 많이 등장하는 수
import sys

N = int(sys.stdin.readline())
A = list(map(int, (sys.stdin.readline().split())))

temp = {}
maxScore = 0
score = 1000000001
for a in A:
    if temp.get(a) == None:
        temp[a] = 1
    else:
        temp[a] += 1
    if maxScore < temp[a] or (maxScore == temp[a] and score > a):
        maxScore = temp[a]
        score = a
print(score)

#################
# 색 반전
import sys

hex = (sys.stdin.readline())
change10 = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, 
          '9': 9, 'A': 10 , 'B': 11,'C': 12,'D': 13,'E': 14,'F': 15}

change16 = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 
          9: '9', 10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}
result = ['#']

for i in range(1, 6, 2):
    decimal = change10[hex[i]] * 16 + change10[hex[i+1]]
    decimal = 255- decimal
    result.append(change16[decimal // 16])
    result.append(change16[decimal % 16])
print("".join(result))

#################
# 나무
import sys

N = int(sys.stdin.readline())
tree = list(map(int, (sys.stdin.readline().split())))

height = tree[0]
count = 1
for i in range(1, N):
    if height < tree[i]:
        height = tree[i] 
        count += 1
print(count)

#################
# 반도
import sys

N = int(sys.stdin.readline())
map = []

for i in range(N):
    map.append(sys.stdin.readline().split())
    
start = 1
end = N-1
count = 0
sea = 0
for i in range(N):
    for j in range(start, end):
        if map[i][j] == 'X':
            continue
        if j-1 >=0 and map[i][j-1] == 'X':
            sea += 1
        if j+1 <=N-1 and map[i][j+1] == 'X':
            sea += 1
        if i-1 >= 0 and map[i-1][j] == 'X':
            sea += 1
        if i+1 <=N-1 and map[i+1][j] == 'X':
            sea += 1
        if sea == 3:
            count += 1       
        sea = 0
    if map[i][0] == 'O':
        start = 1
    else:
        start = 0
    if map[i][N-1] == 'O':
        end = N-1
    else:
        end = N
print(count)

#################
# 비밀번호
import sys
import re

hint = sys.stdin.readline()
change = re.sub('[a-z]', ' ', hint)

print(sum(map(int, change.split())))

#################
# 세포AB
import sys

N = int(sys.stdin.readline())
cell = [1,1]

for i in range(N):
    tempA = cell[0]
    cell[0] -= tempA
    cell[0] += cell[1]
    cell[1] += tempA
print(cell[0], cell[1])

#################
# 소수점 이진비트
import sys

N = float(sys.stdin.readline())
binary = ['0.']

while(len(binary) != 11):
    N *= 2
    integer = int(N)
    binary.append(str(integer))
    N -= integer
    if N == 0:
        break
print(''.join(binary))

#################
# 구독형 서비스
import sys

N = int(sys.stdin.readline())
buy = list(map(int, sys.stdin.readline().split()))

buy.sort()
maxTotal = 0

for i in range(N):
    if i-1 >= 0 and buy[i] == buy[i-1]:
        continue
    if maxTotal < buy[i] * (N-i):
        maxTotal = buy[i] * (N-i)
print(maxTotal)

#################
# over_underflow
import sys

A, B = map(int, sys.stdin.readline().split())
bit = A + B
if bit < -8:
    print(bit + 16)
elif bit > 7:
    print(bit - 16)
else:
    print(bit)

#################
# 수 계단
import sys

N = int(sys.stdin.readline())
check = 1

for i in range(1, N*(N+1) //2+1):
    print(i, end="")
    if check * (check+1) // 2 == i:
        print()
        check += 1
    else:
        print(end=" ")

#################
# 블럭 쌓기 수열


#################
# 계승진법
import sys
from collections import deque

N = int(sys.stdin.readline())

dlist = deque()

number = 1
while(N != 0):
    dlist.appendleft(str(N % number))
    N = N // number
    number += 1

print("".join(dlist))

#################
# 피보나치 피보나치 수열
import sys

space = list(map(int, (sys.stdin.readline().split())))

p = [0,1,1]
pp = [0,1,1]

break_point = False
for i in range(3,max(space)):
    repeat = p[i-2] + p[i-1]
    p.append(repeat)
    
    for i in range(repeat):
        pp.append(repeat)
        
        if len(pp) -1 >= max(space):
            break_point = True
            break
        
    if break_point == True:
        break

print(sum(pp[   space[0] : space[1]+1  ]))


#################
# 사내 복지


#################
# 문서 통계
import sys

origin = sys.stdin.readline().strip()
no_space = origin.split()

print(len(origin))
print(len("".join(no_space)))
print(len(no_space))

#################
# 팰린드롬의 날
import sys

date = list(map(int, sys.stdin.readline().split()))

end_date = [0,31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

result = ""
while(True):
    # 만약 달의 마지막 날인데 12월 일때와 아닐 때를 구별해서 월과 일을 증가시킨다
    if end_date[date[0]] == date[1]:
        if date[0] == 12:
            date[0] = 1
        else:
            date[0] += 1
        date[1] = 1
    else:
        date[1] += 1    
    
    # 일이 9이하이면 1글자이므로 0을 삽입하고 아니면 그냥 string으로 변환
    if(date[1] <= 9):
        result = str(date[0]) + "0" + str(date[1])
    else:
        result = str(date[0]) + str(date[1])
    
    if  result == "".join(reversed(result)):
        break
    
for d in date:
    print(d, end=" ")

#################
# 난수 생성
import sys

ran = list(map(int, sys.stdin.readline().split()))

X = ran[0]
N = ran[4]

for i in range(N):
    X = (X * ran[1] + ran[2]) % ran[3]

print(X)

#################
# 직각 삼각형
import sys

triangle = list(map(int, sys.stdin.readline().split()))

a = triangle[0] * triangle[0]
b = triangle[1] * triangle[1]
c = triangle[2] * triangle[2]

if a == b + c or b == a + c or c == a + b:
    print("YES")
else:
    print('NO')
