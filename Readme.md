Implementation of topological sort order for a graph.

Input: A graph of the form {v1: [u1, u2, ..., un], v2: [w1, w2, ..., wm]}
where v1, v2, ..., vk are vertices of the graph and ui1,...,un and w1,...,wm are the vertices to which they are connected. 
In other words, there is an edge connecting v1 to each of u1, u2, ..., un; v2 to each of w1, w2, ..., wm and so on.

Output: Returns a list of vertices in the topological order.

Uses source removal algorithm. Source is defined as a vertex which has no incoming edges i.e. in degree = 0.

Algorithm:
	topological_order <- list
	while a source exists:
		add the source to topological_order
		remove the source and all its outgoing edges.
	return topological_order
