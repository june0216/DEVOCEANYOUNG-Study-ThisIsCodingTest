board_size = int(input())
apple = int(input())

table = [[0 for _ in range(board_size)] for _ in range(board_size)]
for i in range(apple):
    r, c = map(int, input().split())
    table[r][c] = 1
bam = []
direction_limit = int(input())
for j in range(direction_limit):
    sec, d = input().split()
    bam.append((int(sec), d))
def turn(direction, d):
    if d == "D":
        direction = (direction +1 )% 4
    else:
        direction = (direction -1 )% 4
    return direction

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
cnt = 0
x , y = 0, 0
b =0
direction = 0
q = [(x, y)]
while True:
    nx = x + dx[direction]
    ny = y + dy[direction]

    if nx < 0 or ny < 0 or ny >= board_size or nx >= board_size:
        cnt +=1
        break
    elif table[nx][ny] == 2:
        cnt +=1
        break

    else:
        if table[nx][ny] == 0:
            table[nx][ny] = 2
            q.append((nx, ny))
            lx, ly = q.pop()
            table[lx][ly] = 0
        if table[nx][ny] == 1:
            table[nx][ny] = 2
            q.append((nx, ny))
    x, y = nx, ny
    cnt +=1
    if b < 1 and cnt == bam[b][0]:
        direction = turn(direction, bam[b][1])
        b +=1
print(cnt)


