# Implementation of topological sort.

Input: 
-------
A graph of the form 

	{
		v1: [u1, u2, ..., un], 
		v2: [w1, w2, ..., wm], 
		...,
		...,
		vk: [x1, x2, ..., xj]
	}

where v1, v2, ..., vk are vertices of the graph and [u1,...,un], [w1,...,wm] and [x1, x2, ..., xj] are the vertices to which they are connected. 
In other words, there is an edge **FROM** v1 **TO EACH OF** u1, u2, ..., un; **FROM** v2 **TO EACH OF** w1, w2, ..., wm and so on.

Output: 
-------
Returns a list of vertices in the topological order.

Uses **source removal algorithm**. Source is defined as a vertex which has no incoming edges i.e. in degree = 0.

Algorithm:
-----------
	
	topological_order <- list
	
	while a source exists:
		
		add the source to topological_order
		
		remove the source and all its outgoing edges.
	
	return topological_order
