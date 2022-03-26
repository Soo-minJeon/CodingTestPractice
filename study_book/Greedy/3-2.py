import time

start_time = time.time()

# input
N, M, K = map(int, input().split());
inputs = list(map(int, input().split()));

# 0) 필요 변수 선언
result = 0;

# 1) 내림차순 정렬
inputs.sort(reverse = True)

# 2) inputs[0]과 inputs[1]이 같은가?
if (inputs[0] == inputs[1]):
  result = inputs[0] * M
else :
  c = M // (K+1)
  l = M % (K+1)
  result = inputs[0]*3*c + inputs[1]*c + inputs[0]*l

print(result)

end_time = time.time()

print("time : ", end_time - start_time)