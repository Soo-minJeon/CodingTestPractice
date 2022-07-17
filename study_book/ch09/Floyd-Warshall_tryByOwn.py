n, m = map(int, input().split())
r = [[1e9*n for i in range(n+1)] for j in range(n+1)]


def floyd():
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            for k in range(1, n+1):
                if (r[j][i] + r[i][k] < r[j][k]) :
                    r[j][k] = r[j][i] + r[i][k]


for i in range(m):
    s, e = map(int, input().split())
    r[s][e] = 1
    r[e][s] = 1
x, k = map(int, input().split())


floyd()

answer = r[1][k] + r[k][x]
print(answer)
if (answer >= 100) : print(-1)
else: print(answer)
print(r)





