# 0- 빈칸 1-벽 2- 바이러스
#모든 경우의 수를 다 계산해야한다
N, M = map(int, input().split())
table = [[0] * M for _ in range(N)]
data = []
for _ in range(M):
    data.append(list(map(int, input().split())))

dx= [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

result = 0

def virus(x, y):
    for i in range(4):
        nx = dx[i] + x
        ny = dy[i] + y
        if nx >=0 and nx < N and ny >= 0 and ny < N:
            if table[nx][ny] == 0:
                table[nx][ny] = 2
                virus(nx, ny)
def get_score(): #안전점수 계산
    score = 0
    for i in range(N):
        for j in range(N):
            if table[i][j] == 0:
                score +=1
    return score

def dfs(count):
    global result
    if count == 3: # 울타리 3개라면 바이러스 다 전파하고 안전점수 계산
        for i in range(N):
            for j in range(N):
                table[i][j] = data[i][j]
        for i in range(N):
            for j in range(N):
                if table[i][j] == 2:
                    virus(i, j)
        result = max(result, get_score())
        return
    for i in range(N):
        for j in range(N):
            if data[i][j] == 0:
                data[i][j] = 1
                count +=1
                dfs(count)
                count -=1
                data[i][j] = 0
dfs(0)
print(result)

