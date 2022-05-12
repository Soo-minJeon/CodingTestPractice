import time

start_time = time.time()

n, k = map(int, input().split())
# n = 배열의 개수
# k = 최대로 교환할 수 있는 횟수

arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))
# arr1 = 합이 최대가 되어야 하는 배열

arr1 = sorted(arr1) # 작은 수 부터
arr2 = sorted(arr2, reverse=True) # 큰 수 부터

for i in range(0, k):
    # k번 교환
    if (arr1[i] < arr2[i]):
        arr1[i], arr2[i] = arr2[i], arr1[i]

print('result = ', sum(arr1))

end_time = time.time()

print("time : ", end_time - start_time)