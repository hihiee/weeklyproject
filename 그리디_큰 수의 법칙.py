
n, m, k = map(int, input().split())
numbers = list(map(int, input().split()))
numbers.sort(reverse = True) # 내림차순으로 변경

first = numbers[0]
second = numbers[1]

# 구현: m번 동안 가장 큰 수를 k번 더하고, 두 번째 큰 수를 1번 더하는 것을 m 이 0이 될 때까지 반복한다.

result = 0

while True:
    if m == 0:
        break
    for i in range(k):
        result += first
        m -= 1
        if m == 0:
            break

    if m == 0:
        break
    result += second
    m -= 1

print(result)
