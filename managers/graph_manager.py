def adjacency_list_to_list_of_edges(adjacency_list, vertexes):
    list_of_edges = {vertex: set() for vertex in vertexes}
    for adjacency in adjacency_list:
        list_of_edges[adjacency[0]].add(adjacency[1])
        list_of_edges[adjacency[1]].add(adjacency[0])
    return list_of_edges


def read_graph_from_console(adjacency_list, vertexes):
    count_of_rows = int(input())
    for i in range(count_of_rows):
        a, b = input().split(" ")
        a = int(a)
        b = int(b)
        vertexes.add(a)
        vertexes.add(b)
        adjacency_list.append((a, b))
    pass


def read_graph_from_file(file_name, adjacency_list, vertexes):
    with open(file_name, "r", encoding='utf-8') as file:
        count_of_rows = int(file.readline())
        for line in file:
            a, b = line.split(" ")
            a = int(a)
            b = int(b)
            vertexes.add(a)
            vertexes.add(b)
            adjacency_list.append((a, b))
