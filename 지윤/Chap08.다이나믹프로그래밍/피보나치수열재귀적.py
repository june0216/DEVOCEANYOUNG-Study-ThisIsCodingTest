d = [0] * 100
def fibo(x):
    if x == 1 or x == 2: # 종료조건
        return 1
    if d[x] != 0: #이미 계산한 적 있는 문제라면
        return d[x]
    d[x] = fibo(x-1) + fibo(x-2)
    return d[x]
print(fibo(99))