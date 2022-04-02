n, m = map(int, input().split());

inputs = []

count = n * m
visited = [False] * count;

for i in(0, n):
    arrays = list(map(int, input().split()));
    inputs.append(arrays);

#------- 여기까지는 완료 ---------#

def dfs( graph, v, visited ) :
    # 현재 노드를 방문처리
    visited[v] = True;
    print(v, end = " ")

    # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited);
