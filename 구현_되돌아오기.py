n = int(input())

x, y = 0, 0
count = 0


# E, W, S, N
dxs = [1, -1, 0, 0]
dys = [0, 0, -1, 1]

bool_ = False

for _ in range(n):
    direction, walks = input().split()
    walks = int(walks)

    if direction == 'N':
        dir_num = 3
    elif direction == 'E':
        dir_num = 0
    elif direction == 'W':
        dir_num = 1
    else:
        dir_num = 2

    for _ in range(walks):
        print(f"지금의 dir_num은 {dir_num}, walks는 {walks}, count는 {count}, 좌표는 {x}, {y}, bool_은 {bool_}")
        x += dxs[dir_num]
        y += dys[dir_num]
        count += 1

        if x == 0 and y == 0:
            bool_ = True
            print(f"x, y 가 0, 0일 경우 현재 횟수는 {count}, bool_은 {bool_}")
            print(count)
            break
 #      break  여기에 break 를 집어넣으면 walks 에 대한  for문이 완전히 종료되고, input의 다음 줄인 'E 2' 가 실행됨

 #      if bool_ == True:
 #          break
        # 이걸 또 여기에 하면, 조건을 이미 만족했음에도 불구하고 다시 for _ in range(n) 의 첫 loop 로 나가서 또 input 의 다음 줄이 실행됨
        # 이때 bool_ 은 계속 True 이기 때문에 한 번만 walk 한 다음에 바로 break 됨.

    if bool_ == True:
        break

if bool_ == False:
    print(-1)
    
