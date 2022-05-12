# 개미전사 문제

# 창고의 개수
n = int(input())

# 창고 당 식량이 얼마나 들었는지
li = list(map(int, input().split()))

# 식량창고 N의 최대값이 100이므로 * 100
re = [0] * 100

re[0] = li[0]
re[1] = max(re[0], li[1])

# i번까지, 최대로 얻을 수 있는 식량의 수
for i in range(2, n):
    re[i] = max(re[i-1], re[i-2] + li[i])

print(max(re))