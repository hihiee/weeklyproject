# 조건

x, y = 2, 4 # 행렬이기 때문에
dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0] # 행렬 좌표값


# x, y + 상하좌우 확인하고(range 4), 숫자 1일 경우 count += 1
# 예외: 5 보다 클 때

def in_range(x, y):
    return x >= 0 and x < 5 and y >= 0 and y < 5

a = [[0, 0, 0, 1, 0],
     [0, 1, 1, 1, 0],
     [0, 0, 0, 0, 1],
     [1, 0, 1, 1, 1],
     [1, 0, 1, 1, 0]]


count = 0

for dx, dy in zip(dxs, dys): # 4쌍 = 4번 반복
    nx, ny = x + dx, y + dy
    # 이제 인접한 곳에 1이 있는지를 확인하기 전에, 먼저 (nx, ny)가 격자 안에 들어오는지를 확인
    if in_range(nx, ny) and a[nx][ny] == 1:  # in_range(x, y) 가 true 이고, 1일 경우 ##
        count += 1

print(count)
# 변수 선언 및 입력
n = int(input())
arr = [
    list(map(int, input().split()))
    for _ in range(n)
]

dxs = [0, 1,  0, -1]
dys = [1, 0, -1,  0]


def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < n


def adjacent_cnt(x, y):
    cnt = 0
    for dx, dy in zip(dxs, dys):
        nx, ny = x + dx, y + dy
        if in_range(nx, ny) and arr[nx][ny] == 1:
            cnt += 1
    
    return cnt


# 각 칸을 탐색합니다.
ans = 0
for i in range(n):
    for j in range(n):
        if adjacent_cnt(i, j) >= 3:
            ans += 1
    
print(ans)
