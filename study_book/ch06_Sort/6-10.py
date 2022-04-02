# 입력받기
n = int(input())

arr = []
for i in range(0, n):
    arr.append(int(input()))

# 내장 라이브러리
print('내장 라이브러리 => ', sorted(arr, reverse=True))

# 선택정렬
arr2 = arr.copy()
for i in range(0, n-1):
    max = arr2[i]
    for j in range(i+1, n):
        if (max<arr2[j]):
            max = arr2[j]
            arr2[i], arr2[j] = arr2[j], arr2[i]

print('선택정렬 => ', arr2)

# 삽입정렬
arr3 = arr.copy()
for i in range(1, n):
    for j in range(i, 0, -1):
        if arr3[j-1]>arr3[j]:
            break;

        elif arr3[j-1]<arr3[j]:
            arr3[j-1], arr3[j] = arr3[j], arr3[j-1]

print('삽입정렬 => ', arr3);

# 퀵 정렬
arr4 = arr.copy()

def quick(array):
    if len(array) <= 1:
        return array

    pivot = array[0]
    tail = array[1:]

    left_s = [x for x in tail if x > pivot]
    right_s = [x for x in tail if x <= pivot]

    return quick(left_s) + [pivot] + quick(right_s)
print('퀵정렬 => ', quick(arr4))






