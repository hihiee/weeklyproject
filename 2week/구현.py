n = 4

answer = [
    [0] * n
    for _ in range(n)
]

dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]

x, y = 0, 0 # 시작은 (0, 0), 여기에서 x 관련 애들은 다 좌표값
dir_num = 0 # 오른쪽부터 시작

answer[x][y] = 1 # 초기값


def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < n

# n & n 번 진행
for i in range(2, n * n + 1):
    # 현재 방향 dir 기준으로 그 다음 위치 값 계산
    nx, ny = x + dxs[dir_num], y + dys[dir_num]
    # 더 이상 나갈 수 없다면 시계 방향으로 90도 회전
    if not in_range(nx, ny) or answer[nx][ny] != 0:
        print(i, "번째 진행", ":", "범위를 넘는 nx, ny 확인:", nx, ny, "|", "혹은 0이 아닌 경우일 수도")
        dir_num = (dir_num + 1) % 4
        print("Condition*. IF NOT", "새롭게 지정된 dir_num", dir_num, "|", i, "번째 진행", "|", "dir_num방향:", dir_num, "|", "x, y:", x, y, "|", "새로운 nx, ny:", nx, ny)

    print(i, "번째 진행", ":", "dir_num방향:", dir_num, "/", "x, y:", x, y, "/", "새로운 nx, ny:", nx, ny)
    x, y = x + dxs[dir_num], y + dys[dir_num]
    answer[x][y] = i
    print(i, "번째 진행", ":", "dir_num방향:", dir_num, "/", "x, y:", x, y, "/", "새로운 nx, ny:", nx, ny)

    print(answer)
