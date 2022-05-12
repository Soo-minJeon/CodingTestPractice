n = int(input())
arr = []

for i in range(0, n):
    arr.append(int(input()))

range_arr = [0] * (max(arr) + 1) # 0 ~ max(arr)

for i in range(0, len(arr)):
    range_arr[arr[i]] += 1
range_arr2 = sorted(range_arr, reverse=True)

for i in range(0, len(range_arr)):
    if range_arr[i] == range_arr2[0]:
        print(i)
        break;
