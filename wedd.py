from algorithms.dfs import dfs
from managers.graph_manager import read_graph_from_console, read_graph_from_file, adjacency_list_to_list_of_edges
from managers.used_dic_manager import is_all_used_in_used_dic, first_unused_from_used_dic, create_used_dic_from_vertexes


def wedd(file_name=None):
    adjacency_list = []
    vertexes = set()

    if file_name is None:
        read_graph_from_console(adjacency_list, vertexes)
    else:
        read_graph_from_file(file_name, adjacency_list, vertexes)

    used = create_used_dic_from_vertexes(vertexes)

    graph = adjacency_list_to_list_of_edges(adjacency_list, vertexes)

    girls = []
    boys = []

    while not is_all_used_in_used_dic(used):
        girls_set = set()
        boys_set = set()
        dfs(graph, first_unused_from_used_dic(used), used, girls_set, boys_set)
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
    print(wedd("input_files/condition_input.txt"))
