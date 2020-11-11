def is_all_used_in_used_dic(used):
    for vertex in used:
        if used[vertex] is False:
            return False
    return True


def first_unused_from_used_dic(used):
    for vertex in used:
        if used[vertex] is False:
            return vertex


def create_used_dic_from_vertexes(vertexes):
    return {vertex: False for vertex in vertexes}
