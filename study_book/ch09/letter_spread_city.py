def floyd() :
    for i in range(1, n+1):
        for j in range(1, n+1):
            for k in range(1, n+1):
                if (r[j][i] + r[i][k] < r[j][k] and j!=k) : r[j][k] = r[j][i] + r[i][k]

n, m, c = map(int, input().split())
r = [[(1e9) for i in range(n+1)] for j in range(n+1)]
for i in range(m) :
    x, y, z = map(int, input().split())
    r[x][y] = z
    r[y][x] = z

floyd()

count = 0
time = 0
for i in range(1, n+1):
    if (r[c][i] < 100) :
        count += 1
        if (time < r[c][i]) : time = r[c][i]


print(count, '', time)

