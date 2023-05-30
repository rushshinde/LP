from queue import Queue

adj_list = {
	'A':['B','C'],
	'B':['A'],
	'C':['A']
}
#declare data types requred for code
queue = Queue()
visited = {}
level = {}
parent = {}
bfs_traversal_output = []

for node in adj_list.keys():
	visited[node] = False
	parent[node] = None
	level[node] = -1

source = 'A'
visited[source] = True
level[source] = 0
queue.put(source)


while not queue.empty():
	u = queue.get()
	bfs_traversal_output.append(u)
	for v in adj_list[u]:
		if not visited[v]:
			visited[v] = True
			level[v] = level[u]+1
			parent[v] = u
			queue.put(v)

print(bfs_traversal_output)