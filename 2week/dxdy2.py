# 북쪽을 향한 상태에서 움직이는 것을 시작!
# 총 n번 움직이고 (for _ in range(n):)
# 명령 L = 왼쪽 90도 전환, R = 오른쪽 90도 전환, **F = 바라보고 있는 방향으로 + 1 (if)

'''

direction = list(input())  # LF 출력

x, y = 0, 0
dir_num = 3

dx, dy = [1, 0, -1, 0], [0, -1, 0, 1]


for dir_ in direction:
    if dir_ == 'L':
        print("condition <L>")
        dir_num = (dir_num - 1) % 4
    elif dir_ == 'R':
        print("condition <R>")
        dir_num = (dir_num + 1) % 4
    elif dir_ == 'F'
        print("condition <F>")
        x += dx[dir_num]
        y += dy[dir_num]

print(x, y)
