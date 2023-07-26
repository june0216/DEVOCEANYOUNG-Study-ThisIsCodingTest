# 연산을 사용하는 횟수의 최솟값
# 상향식

x = int(input())
d = [0] * 30001

for i in range(2, x+1):
    d[i] = d[i-1]+1 # 먼저 모든 수가 할 수 있는 연산인 "-1"을 해준다. (그리고 -1을 해줬기 때문에 연산 횟수 1을 추가한다)
    if i % 2 == 0: # 하지만 그 수가 만약에 2로 나누어떨어진다면
        d[i] == min(d[i] , d[i//2] + 1) # 2로 나누는 연산을 한 횟수가 더 작은지 앞에서 -1을 한 연산횟수가 작은지 비교해서 선택
    if i % 3 == 0:
        d[i] = min(d[i], d[i//3] + 1)
    if i%5 == 0:
        d[i] = min(d[i], d[i//5] + 1)
print(d[x])
