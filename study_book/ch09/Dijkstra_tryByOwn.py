n, m = map(int, input().split())
start = int(input())

m_list = [[-1 for j in range(n)] for i in range(n)]

for i in range(m):
    x, y, z = map(int, input().split())
    m_list[x-1][y-1] = z
# m_list = [[-1, 2, 5, 1, -1, -1], [-1, -1, 3, 2, -1, -1], [-1, 3, -1, -1, -1, 5], [-1, -1, 3, -1, 1, -1], [-1, -1, 1, -1, -1, 2], [-1, -1, -1, -1, -1, -1]]

answer = m_list[0]

for i in range(n):
    print(i+1, ' : ')
    for j in range(n):
        print('\t', j, " : ")
        if ( m_list[i][j] > 0 ):

            if (answer[i] < 0) : tmp = 0
            else : tmp = answer[i]

            if (answer[j] > tmp + m_list[i][j] or answer[j] < 0):
                print('현재 : ', answer[j], ' | ', i+1, '를 거쳐간다면  : ', tmp,  '+',  m_list[i][j])
                answer[j] = tmp + m_list[i][j]
    print(answer)


print(answer)