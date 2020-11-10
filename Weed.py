def dfs(graph, vertex, used, girls_set, boys_set):
    used[vertex] = True
    if vertex % 2 == 1:
        boys_set.add(vertex)
    else:
        girls_set.add(vertex)
    for next_vertex in graph[vertex]:
        if used[next_vertex] is False:
            dfs(graph, next_vertex, used, girls_set, boys_set)


def is_all_used(used):
    for vertex in used:
        if vertex is False:
            return False
    return True


def adjacency_list_to_list_of_edges(adjacency_list, count_of_vertex):
    list_of_edges = [set() for i in range(count_of_vertex)]
    for pair in adjacency_list:
        list_of_edges[pair[0]].add(pair[1])
        list_of_edges[pair[1]].add(pair[0])
    return list_of_edges


def first_unused(used):
    for i in range(len(used)):
        if used[i] is False:
            return i


def wedd(file_name=None):
    adjacency_list = []
    count_of_vertex = 0
    if file_name == None:
        count_of_rows = int(input())
        for i in range(count_of_rows):
            a, b = input().split(" ")
            a = int(a) - 1
            b = int(b) - 1
            adjacency_list.append((a, b))
            count_of_vertex = max(max(a, b), count_of_vertex)
        count_of_vertex += 1
    else:
        with open(file_name, "r", encoding='utf-8') as file:
            count_of_rows = int(file.readline())
            for line in file:
                a, b = line.split(" ")
                a = int(a) - 1
                b = int(b) - 1
                adjacency_list.append((a, b))
                count_of_vertex = max(max(a, b), count_of_vertex)
            count_of_vertex += 1

    used = [False for i in range(count_of_vertex)]

    graph = adjacency_list_to_list_of_edges(adjacency_list, count_of_vertex)
    girls = []
    boys = []
    while not is_all_used(used):
        girls_set = set()
        boys_set = set()
        dfs(graph, first_unused(used), used, girls_set, boys_set)
        girls.append(len(girls_set))
        boys.append(len(boys_set))
    count = 0
    component_count = len(girls)
    for i in range(component_count):
        for j in range(component_count):
            if i != j:
                count += girls[i] * boys[j]
    return count


if __name__ == '__main__':
    print(wedd("one_component_input.txt"))
