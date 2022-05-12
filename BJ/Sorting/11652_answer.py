n = int(input())  # 카드의 수

card_dict = dict() # 카드 딕테이션 생성
# 특정 카드가 몇번 입력되었는지

for i in range(0, n):
    card = int(input()) # 입력한 카드
    if card in card_dict:
        card_dict[card] += 1 # 카드 딕테이션 키 값에 입력한 카드가 있다면 +1
    else:
        card_dict[card] = 1 # 카드 딕테이션 키 값에 입력한 카드가 없다면 = 1

print('sorted(card_dict) : ', sorted(card_dict))
print('sorted(card_dict.items()) : ', sorted(card_dict.items()))
print('sorted(card_dict.items())[0][0] : ', sorted(card_dict.items())[0][0])
