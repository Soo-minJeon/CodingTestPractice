# 문제 링크 : https://programmers.co.kr/learn/courses/30/lessons/42888

def solution(record):
    answer = []  # 정답으로 반환할 배열

    # 대치어 딕셔너리
    activity = {'Leave': '님이 나갔습니다.',
                'Enter': '님이 들어왔습니다.',
                'Change': ''}

    id_name = {}

    # 입력으로 들어온 기록의 수만큼 for문을 돌려
    # 키(사용자 아이디) : 값(최종적으로 변경된 닉네임) 형태의 딕셔너리 생성
    for i in range(len(record)):

        splited = record[i].split()

        if (splited[0] == 'Enter'):
            id_name[splited[1]] = splited[2]

        elif (splited[0] == 'Change'):
            id_name[splited[1]] = splited[2]

        # Leave에서는 새로운 유저의 등장이나 닉네임 변경이 없기에 고려하지 않는다.

    for i in range(len(record)):
        splited = record[i].split()

        if (splited[0] != 'Change'):  # Change는 결과 배열에 넣지 않으므로
            answer.append(id_name[splited[1]] + activity[splited[0]])

    return answer

if __name__ == "__main__":
    input = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]
    print(solution(input))