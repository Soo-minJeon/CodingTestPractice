n, m = map(int, input().split())
start = int(input())

m_list = [[-1 for j in range(n+1)] for i in range(n+1)]

# for i in range(m):
#     x, y, z = map(int, input().split())
#     m_list[x-1][y-1] = z
m_list = [[-1, -1, -1, -1, -1, -1, -1], [-1, -1, 2, 5, 1, -1, -1], [-1, -1, -1, 3, 2, -1, -1], [-1, -1, 3, -1, -1, -1, 5], [-1, -1, -1, 3, -1, 1, -1], [-1, -1, -1, 1, -1, -1, 2], [-1, -1, -1, -1, -1, -1, -1]]

visited = [0 for i in range(n+1)]
answer = [0 for i in range(n+1)]
for i in range(n):
    answer[i+1] = m_list[start][i+1]




def getMin():
    min = int(1e9)
    index = -1

    for i in range(1, n+1):
        if (answer[i] < min and visited[i] != 1 and answer[i] > 0):
            min = answer[i]
            index = i
    visited[index] = 1
    return index

def dynamic():
    for j in range(n-1):
        tmp = getMin()
        for i in range(n+1):
            if (visited[i]!=1 and m_list[tmp][i]!= -1):
                if (answer[i] > answer[tmp] + m_list[tmp][i] or answer[i] == -1):
                    answer[i] = answer[tmp] + m_list[tmp][i]
        print(tmp, ' : ', answer)


dynamic()
print('\n결과 : ', answer)
