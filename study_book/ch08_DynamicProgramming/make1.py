x = int(input())

answer = [0 for i in range(3002)]

for i in range(2, x+1):
    answer[i] = answer[i-1]+1
    if (i % 2 == 0 ) : # 2의 배수라면
        answer[i] = min(answer[i], answer[i//2] + 1)
    if (i % 3 == 0):  # 3의 배수라면
        answer[i] = min(answer[i], answer[i // 3] + 1)
    if (i % 5 == 0 ) : # 2의 배수라면
        answer[i] = min(answer[i], answer[i//5] + 1)

print(answer[x])