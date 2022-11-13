'''
파일명 : main.py
목적 : 코드업 기초 100제 100번째 문제
'''

d = []

for i in range(10):
    d.append([])
    for j in range(10):
        d[i].append(0)

for i in range(10):
    n = input().split()
    for j in range(10):
        d[i][j] = int(n[j])

r=1
c=1

while True:
    if d[r][c+1]==0 or d[r][c+1]==2:
        d[r][c]=9
        c+=1
    elif d[r+1][c] ==0 or d[r+1][c]==2:
        d[r][c]=9
        r+=1
    
    if (d[r][c]==2):
        d[r][c]=9
        break
    elif (d[r+1][c]==1 and d[r][c+1]==1) or (r==9 and c==9):
        break
    
for i in range(10):
    for j in range(10):
        print(d[i][j], end=' ')
    print()
