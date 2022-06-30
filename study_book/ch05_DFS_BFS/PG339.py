def BFS(min_route, route_list, start):

    for i in route_list[start]:
        # print('i : ', i)
        if (len(route_list[i])>0):
            for j in route_list[i]:
                # print(j)
                if (min_route[i]+1 < min_route[j] or min_route[j] == 0):
                    min_route[j] = min_route[i] + 1
                BFS(min_route, route_list, j)



input1 = list(map(int, input().split()))

city_n = input1[0]
route_n = input1[1]
target = input1[2]
start = input1[3]

route_list = [[] for i in range(city_n+1)]
for i in range(route_n):
    ins = list(map(int, input().split()))
    route_list[ins[0]].append(ins[1])
    print(route_list)

min_route = [0 for i in range(city_n + 1)]

for i in range(len(route_list[start])):
    min_route[route_list[start][i]] += 1

BFS(min_route, route_list, start)

# print(min_route)

answer_list = []
for i in range(len(min_route)):
    if (min_route[i] == target):
        answer_list.append(i)

if (len(answer_list) == 0): print('-1')
else :
    for i in answer_list:
        print(i)







