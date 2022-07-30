n = int(input())
input_ = list(map(int, input().split()))
input_ = sorted(input_, reverse=True)

if(len(input_) != n): # 입력값의 크기가 n과 부합하는지 확인
    print('Input length is not correct')
    exit(0) #

print(input_)

answer = [-2 for i in range(len(input_))]

# for i in range(len(input_)):
#     for j in range(len(answer)):
#         if (answer[j]==-1):
#             answer[j] = answer
#         elif (answer[j] == 0):
#             answer[j] -= 1
#         elif (answer[j])

