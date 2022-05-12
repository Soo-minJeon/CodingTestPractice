n = int(input()) # 배열 len

arr = list(map(int, input().split())) # 입력 배열

arr = sorted(arr) # 오름차순 정렬

sumarr = []
result = 0

# 누적 합 계산
for i in range(0, len(arr)):
    result = (result + arr[i])
    sumarr.append(result)

result = 0
for i in range(0, len(sumarr)):
    result += sumarr[i]

print(result)