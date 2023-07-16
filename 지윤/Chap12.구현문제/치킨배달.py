#1 - 집, 2 - 치킨집
import sys
from itertools import combinations
N, M = map(int, input().split())
MAX = sys.maxsize
chicken =[]
house = []
for r in range(N):
    table = list(map(int, input().split()))
    for k in range(N):
        if table[k] == 2:
            chicken.append((r, k))
        elif table[k] == 1:
            house.append((r, k))

chicken_new= list(combinations(chicken, M))

def get_sum(com):
    result = 0
    for hx, hy in house:
        temp = MAX
        for cx, cy in com:
            temp = min(temp, abs(hx - cx) + abs(hy - cy))
        result += temp
    return result

result = MAX
for com in chicken_new:
    result = min(result, get_sum(com))
print(result)
 #5 3
#0 0 1 0 0
#0 0 2 0 1
#0 1 2 0 0
#0 0 1 0 0
#0 0 0 0 2