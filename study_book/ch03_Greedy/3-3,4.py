import time

start_time = time.time() # 시작시간

# 0) 입력 받기
N, M = map(int, input().split())

# 1) 필요 변수 선언
result = 0

for i in range(N):
    inputs = list(map(int, input().split()));

    # written by ME -> time : 9.06726598739624
    inputs.sort()
    tmp_min = inputs[0]
    if (tmp_min > result) : result = tmp_min

    # book code -> time : 13.44906210899353
    # tmp_min = min(inputs)
    # result = max(result, tmp_min)


print(result)


end_time = time.time() # 종료시간
print('time : ', end_time - start_time) # 소요 시간