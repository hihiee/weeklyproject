vertices_num = 7
edges_num = 6

graph = [
	[0 for _ in range(vertices_num + 1)]
	for _ in range(vertices_num + 1)
]

visited = [False for _ in range(vertices_num + 1)]

print(f"처음: {visited}")

def dfs(vertex):
	# curr_v = 1, 2, 3, 4, 5, 6, 7 까지
	for curr_v in range(1, vertices_num + 1):
		print(f"* current vertex: [{vertex}][{curr_v}]")
		if graph[vertex][curr_v] and not visited[curr_v]:
			print(f"if 그래프 행렬의 정점 [{vertex}]와 [{curr_v}]가 간선으로 연결되어 {graph[vertex][curr_v]}이고 방문 여부가 {visited[curr_v]} 일 때")
		#	print(curr_v)
			visited[curr_v] = True
			print(visited)
			# 여기에서, graph[vertex] 의 정점과 이어진 curr_v 로 다시 시작하는 거니까 dfs(curr_v) 가 되는 거잖아
			dfs(curr_v)
		# 여긴 디버깅용, 지우자
		else:
			print("조건 불충족")

# 여기에서 인접 행렬을 입력해주었음
start_points = [1, 1, 1, 2, 4, 6]
end_points = [2, 3, 4, 5, 6, 7]

#
for start, end in zip(start_points, end_points):
	graph[start][end] = 1
	graph[end][start] = 1

print(f"입력한 그래프의 행렬: \n{graph}")

root_vertex = 1 # root 에서 탐색 시작
print(root_vertex)
visited[root_vertex] = True # 방문했으니 True 이때 graph[1][1] = True
dfs(root_vertex)
