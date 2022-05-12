import time

start_time = time.time()

a = int(input()) # 공간 크기

move = input().split() # 움직임

# U, D, R, L
dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]
dic_dxy = {'U' : (dx[0], dy[0]),
           'D' : (dx[1], dy[1]),
           'R' : (dx[2], dy[2]),
           'L' : (dx[3], dy[3])}
# dic_dxy = ['U', 'D', 'R', 'L']

# start location
x = 1 # row
y = 1 # column

for i in range(len(move)):
    # U, D, R, L 이동
    tx = x + dic_dxy[move[i]][0]
    ty = y + dic_dxy[move[i]][1]

    if (1 <= tx <= 5) and ( 1 <= ty <= 5):
        x, y = tx, ty


end_time = time.time()
print('time : ', end_time - start_time)