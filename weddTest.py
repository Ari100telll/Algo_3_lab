import unittest

from managers.used_dic_manager import is_all_used_in_used_dic, first_unused_from_used_dic
from wedd import wedd, adjacency_list_to_list_of_edges


class WeedTest(unittest.TestCase):
    def test_condition(self):
        self.assertEqual(wedd("input_files/condition_input.txt"), 4)

    def test_one_component(self):
        self.assertEqual(wedd("input_files/one_component_input.txt"), 0)

    def test_skipped_vertex(self):
        self.assertEqual(wedd("input_files/skipped_vertex.txt"), 8)

    def test_is_all_used(self):
        self.assertEqual(is_all_used_in_used_dic({1: False, 2: False, 3: False, 4: True, 5: False}), False)

    def test_first_unused(self):
        self.assertEqual(first_unused_from_used_dic({1: True, 2: True, 3: True, 4: False, 5: False}), 4)

    def test_adjacency_list_to_list_of_edges(self):
        self.assertEqual(adjacency_list_to_list_of_edges([(0, 1), (1, 2), (0, 2)], {0, 1, 2}),
                         {0: {1, 2}, 1: {0, 2}, 2: {0, 1}})
