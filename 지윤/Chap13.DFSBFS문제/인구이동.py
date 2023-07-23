from collections import deque
n, l, r = map(int, input().split())
people = []
for _ in range(n):
    people.append(list(map(int, input().split())))


dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y, index):
    #(x, y)와 연결된 나라(연합) 정보를 담는 리스트
    united = []
    united.append((x, y))
    qu = deque()
    qu.append((x, y))
    union[x][y] = index #현재 연합의 번호 할당
    summary = people[x][y]
    count = 1
    while qu:
        x, y = qu.popleft()
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue
            if union[nx][ny] == -1 and abs(people[nx][ny] - people[x][y]) >= l and abs(people[nx][ny] - people[x][y]) <= r:
                union[nx][ny] = index
                summary += people[nx][ny]
                count +=1
                united.append((nx, ny))
    for i, j in united:
        people[i][j] = summary // count
    return count

total_count = 0
# 더 이상 인구 이동을 할 수 없을 때까지 반복
while True:
    union = [[-1] * n for _ in range(n)]
    index = 0
    for i in range(n):
        for j in range(n):
            if union[i][j] == -1: # 해당 나라가 아직 처리되지 않았다면
                bfs(i, j, index)
            index+=1
    if index == n*n:
            break
    total_count +=1
print(total_count)



