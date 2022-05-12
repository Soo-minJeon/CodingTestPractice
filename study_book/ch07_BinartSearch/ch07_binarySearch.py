# 순차 탐색
def sequential_search(n, target, array):
    for i in range(n):
        if i == target :
            return i + 1

print("생성할 원소 개수를 입력한 다음 한 칸 띄고 찾을 문자열을 입력하세요. ")
input_data = input().split()
n = int(input_data[0])
target = input_data[1]

print("앞서 적은 수 만큼 단어를 입력하고 찾을 문자열 입력하세요")