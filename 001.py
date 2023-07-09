# n개의 숫자를 입력받고 오름차순으로 정렬하면 된다. 2750
n = int(input())
l = []
for i in range(n):
    l.append(int(input()))
    
l.sort()

for j in range(n):
    print(l[j])
    

# 수가 주어지면, 그 수의 각 자리수를 내림차순으로 정렬해보자. 1427
n = int(input())

li = []
for i in str(n):
    li.append(int(i))

    
li.sort(reverse=True) 

for i in li:
    print(i,end='')


# 알파벳 소문자로 이루어진 N개의 단어가 들어오면 아래와 같은 조건에 따라 정렬하는 프로그램을 작성하시오.

# 길이가 짧은 것부터
# 길이가 같으면 사전 순으로
# 단, 중복된 단어는 하나만 남기고 제거해야 한다. 1181

n = int(input())
li = []

for i in range(n):
    li.append(input())
setLi = set(li)	
li2 = list(setLi)	
li2.sort()
li2.sort(key = len)

for i in li2:
    print(i)


# 온라인 저지에 가입한 사람들의 나이와 이름이 가입한 순서대로 주어진다. 이때, 회원들을 나이가 증가하는 순으로, 나이가 같으면 먼저 가입한 사람이 앞에 오는 순서로 정렬하는 프로그램을 작성하시오. 10814

n = int(input())

li = []
for _ in range(n):
    age, name = input().split()
    li.append([int(age),name])

li.sort(key=lambda x:int(x[0]))

for i in li:
    print(i[0],i[1])
    


# 2차원 평면 위에 점 N개가 주어진다. 좌표를 x좌표가 증가하는 순으로, x좌표가 같으면 y좌표가 증가하는 순서로 정렬한 다음 출력하는 프로그램을 구하시오. 11650

import sys
n = int(sys.stdin.readline())

li = []

for i in range(n) :
    [x,y] = map(int, sys.stdin.readline().split())
    li.append([x,y])
    
li.sort(key = lambda k : (k[0],k[1]))

for i in range(n) :
    print(li[i][0],li[i][1])
    
    
# 정수 N이 입력되면 00시 00분 00초부터 N시 59분 59초까지의 모든 시작 중에서

# 3이 하나라도 포함되는 모든 경우의 수를 구하는 프로그램을 작성하세요.

# 예를 들어, 1을 입력했을 때 다음은 3이 하나라도 포함되어 있으므로 세어야 하는 시각입니다.

# 00시 00분 03초
# 00시 13분 30초
# 반면에, 다음은 3이 하나도 포함되어 있지 않으므로 세면 안 되는 시각입니다.

# 00시 02분 55초
# 01시 27분 45초

def solution(N):
    answer = 0

    for i in range(N + 1):
        for j in range(60):
            for k in range(60):
                if '3' in str(i) + str(j) + str(k):
                    answer += 1

    return answer


# 알파벳 대문자와 숫자로만 구성된 문자열이 입력으로 주어집니다.

# 이때, 모든 알파벳을 오름차순으로 정렬하여 이어서 출력한 뒤에, 그 뒤에 모든 숫자를 더한 값을 이어서 출력합니다.

# 예를 들어 K1KA5CB7이라는 값이 들어오면 ABCKK13을 출력합니다.


def solution(S):
    number = 0
    alphabet = []

    for c in S:
        if c >= '0' and c <= '9':
            number += int(c)
        else:
            alphabet.append(c)

    alphabet = ''.join(sorted(alphabet))
    return alphabet + str(number)
