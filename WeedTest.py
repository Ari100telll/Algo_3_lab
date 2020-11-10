import unittest

from Weed import wedd


class WeedTest(unittest.TestCase):
    def test_condition(self):
        self.assertEqual(wedd("condition_input.txt"), 4)

    def test_one_component(self):
        self.assertEqual(wedd("one_component_input.txt"), 0)

    def test_skipped_vertex(self):
        self.assertEqual(wedd("skipped_vertex.txt"), 2)