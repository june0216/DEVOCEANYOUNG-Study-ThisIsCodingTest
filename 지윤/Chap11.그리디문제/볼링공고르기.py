from itertools import combinations
N,M = map(int, input().split())
data = list(map(int, input().split()))

result = 0
ball = [0 for _ in range(M)]
for i in range(len(data)):
    ball[data[i]-1] +=1

for j in range(len(ball)-1):
    for k in range(j+1, len(ball)):
        result += ball[j] * ball[k]

print(result)