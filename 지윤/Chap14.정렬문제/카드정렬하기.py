#항상 가장 작은 크기의 두 카드 묶음을 합쳤을 때 최적의 해를 보장
N = int(input())
table = [[] for _ in range(N)]
for i in range(N):
    table[i] = int(input())
table.sort()
result = table[0] + table[1]
for i in range(2, N):
    result += (result+ table[i])

print(result)

#답안  -> 우선순위 큐는 원소를 넣었다 빼는 것만으로도 정렬된 결과를 얻을 수 있다. heapq
# 넣고 또 정렬하는 거보다 효과적
import heapq
n = int(input())

#힙에 초기 카드 묶음을 모두 삽입
heap = []
for i in range(n):
    data = int(input())
    heapq.heappush(heap, data)

result = 0

while len(heap) != 1:
    one = heapq.heappop(heap)
    two = heapq.heappop(heap)

    sum_value = one+two
    result +=sum_value
    heapq.heappush(heap, sum_value)
print(result)
