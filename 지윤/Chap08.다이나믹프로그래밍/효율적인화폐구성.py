#단위가 작기 때문에 그리디터럼 큰 화폐단위부터 처리하는 방법으로는 해결할 수 없다. ->  DP 사용해야 한다.
#적은 금액부터 큰 금액까지 확인하며 차례대로 만들 수 있는 최소한의 화폐 개수를 찾아라
n, m = map(int, input().split())
array = []
for i in range(n):
    array.append(int(input()))
d = [10001] * (m+1)

d[0] = 0
for i in range(n):
    for j in range(array[i], m+1):
        if d[j-array[i]] != 10001: #만드는 방법이 존재
            d[j] = min(d[j], d[j-array[i]] + 1)
if d[m] == 10001:
    print(-1)
else:
    print(d[m])