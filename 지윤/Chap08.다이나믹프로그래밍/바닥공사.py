#결과를 어떤 수로 나눈 결과를 출력하라
#점화식 ai = ai-1 + ai-2 + ai-2
n = int(input())
d = [0] * 1001
d[1] = 1
d[2] = 3
for i in range(3, n+1):
    d[i] = (d[i-1] + d[i-2] * 2) % 796796
print(d[n])

