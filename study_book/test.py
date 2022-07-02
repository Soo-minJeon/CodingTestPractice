def solution(grid, k):
    answer = -1

    dx = [0, 1]
    dy = [1, 0]
    move = ['R', 'D']

    x, y = 0, 0
    count = 0

    while(True):
        for i in range(len(move)):
            tx = x + dx[i]
            ty = y + dy[i]

            if (tx>=0 and ty>=0 and tx < len(grid) and ty < len(grid[0]) and grid[tx][ty] != '#'):
                x,y = tx,ty #이동
                count += 1

            print(i, ' : ', grid[x][y], '(', x, ', ', y, ')')
            print(count)

        if (x == len(grid)-1):
            print('그만')
            answer = count // k
            print(answer)
            break


    return answer

if __name__ == '__main__':
    grid, k = ["..FF", "###F", "###."], 5
    solution(grid, k)