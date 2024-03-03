# 탐색 방향 설정
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_types = ['L', 'R', 'U', 'D'] # index 맞춰주기

# 1, 1부터 이동 계획서에 맞게 탐색

for plan in plans:
    for i in range(len(move_types)):
        if plan == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i] # 얘까지는 plan 에 있는 각 원소랑 탐색 방향으로 나아가는 좌표 방향을 추가해주는 것 # 그러니까 위치를 옮기는 코드

    # NxN 공간을 벗어나는 움직임의 경우 예외처리
    if nx > n or ny > n or nx < 1 or ny < 1: # 0이 아닌 1보다 작을 경우를 말하는 이유는 시작 노드가 (1, 1) 이기 때문? ##
        continue

    x, y = nx, ny

print(x, y) # 최종적으로 도착할 지점의 좌표 (X, Y) 를 공백으루 구분하여 출력한다.
 
