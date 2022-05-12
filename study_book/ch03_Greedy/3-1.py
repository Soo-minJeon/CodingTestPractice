# 거슬러 줄 돈 입력받기
n = int(input())

# 손님이 받을 동전의 수
count = 0

# 거슬러줄 수 있는 화폐의 단위를 담은 리스트
exchange = [500, 100, 50, 10]

for i in range(len(exchange)): # 리스트를 돌면서
    if (n >= exchange[i]): # 남은 거스름돈이 해당 화폐단위보다 큰지 확인
        count += n // exchange[i]
        n = n % exchange[i];

print(count)
