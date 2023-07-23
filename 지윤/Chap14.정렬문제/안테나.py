#정확히 중간값에 해당하는 위치의 집에 안테나를 설치 -> 안테나로부터 모든 집까지의 거리의 총합이 최소
n = int(input())
data = list(map(int, input().split()))
data.sort()

print(data[(n-1)//2])