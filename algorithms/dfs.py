def dfs(graph, vertex, used, girls_set, boys_set):
    used[vertex] = True
    if vertex % 2 == 1:
        boys_set.add(vertex)
    else:
        girls_set.add(vertex)
    for next_vertex in graph[vertex]:
        if used[next_vertex] is False:
            dfs(graph, next_vertex, used, girls_set, boys_set)