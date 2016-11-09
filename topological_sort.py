import queue

def topological_sort(graph):
	topological_order = list()
	in_degree = {vertex:0 for vertex in graph}
	#print(in_degree)
	
	for from_vertex in graph:
		for to_vertex in graph[from_vertex]:
			in_degree[to_vertex] += 1
	#print(in_degree)
	
	pq = queue.PriorityQueue()
	for vertex in in_degree:
		if in_degree[vertex] == 0:
			pq.put(vertex)
    
	while not pq.empty():
		vertex = pq.get()
		#print(vertex)
		topological_order.append(vertex)
		for to_vertex in graph[vertex]:
			in_degree[to_vertex] -= 1
			if in_degree[to_vertex] == 0:
				pq.put(to_vertex)
    
	if len(topological_order) == len(graph):
		return topological_order
	else:
		return []

d = {1: [3], 2: [3], 3: [4], 4: [], 6:[5], 5:[]}
print(topological_sort(d))