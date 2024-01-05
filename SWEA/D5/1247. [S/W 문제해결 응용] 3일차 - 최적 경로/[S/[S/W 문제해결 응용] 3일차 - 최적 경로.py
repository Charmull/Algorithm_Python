# 1. n개의 집을 방문하는 순서 구하기
# 2. 모든 가능한 순서의 이동경로 구하기
# 3. 가장 효율적인 이동경로 출력

# n개의 집을 방문하는 순서(순열) 구하고, 그에 따른 이동경과 구하기
def find_result(n, visited, order):
    if len(order) == n:
        result[0] = min(result[0], count(order, company, home, users))
        return

    for i in range(n):
        if visited[i]:
            continue
        order.append(i)
        visited[i] = 1
        find_result(n, visited, order)
        order.pop()
        visited[i] = 0

# 이동경로 수 구하기


def count(order, company, home, users):
    result = 0
    current = company
    for i in order:
        result += abs(users[i][0] - current[0]) + abs(users[i][1] - current[1])
        current = users[i]
    result += abs(home[0] - current[0]) + abs(home[1] - current[1])
    return result


T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    tmp = list(map(int, input().split()))
    company = tmp[:2]
    home = tmp[2:4]
    users = []
    for i in range(4, n * 2 + 4, 2):
        users.append([tmp[i], tmp[i + 1]])

    visited = [0] * n
    order = []
    result = [200 * (n + 2)]
    find_result(n, visited, order)

    print(f'#{test_case} {result[0]}')
