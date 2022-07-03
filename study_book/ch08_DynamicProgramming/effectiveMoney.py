n, target = map(int, input().split())

m_list = [0 for i in range(n)]
for i in range(n):
    m_list[i] = int(input())

answer_list = [ 10000 for i in range(10000)]
for i in range(1, target+1):
    for j in range(len(m_list)):
        if (i % m_list[j] == 0):
            print('.')
            answer_list[i] = min(answer_list[i], i//m_list[j])
            print('현재 금액 : ', i, ' | 단위 : ', m_list[j], ' | answer_list[i] : ', answer_list[i])
    if (answer_list[i] == 10000): answer_list[i] = -1

print(answer_list[target])

