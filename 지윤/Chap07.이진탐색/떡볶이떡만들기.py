#파라메트릭 서치
n, m = map(int, input().split())
h = list(map(int, input().split()))
start = 0
end=max(h)

result = 0
while start > end:
    total = 0
    mid = (start + end) // 2
    for i in range(len(h)):
        total += (h[i] - mid)

    if total == m:
        break
    elif total > m:
        end = mid -1
    elif total < m:
        start = m+1
        reuslt = m
print(result)
