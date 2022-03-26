import time

start_time = time.time()

# 0) 입력
N, K = map(int, input().split());

# 1) 필요한 변수 선언
count = 0 # result

# 2) 알고리즘
while(N != 1 and K!=0):
    tmp = N % K
    if (tmp != 0):
        N -= tmp
    count += tmp

    N = int(N/K)
    count += 1

print(count)

end_time = time.time()
print('time : ', end_time - start_time)