import unittest
# 求和
def add(x, y):
    return x + y
class TestAdd(unittest.TestCase):
    def test_add_01(self):
        result = add(1, 1)
        self.assertEqual(result, 2)
    def test_add_02(self):
        result = add(1, 0)
        self.assertEqual(result, 1)
    def test_add_03(self):
        result = add(0, 0)
        self.assertEqual(result, 0)
    def test_add(self):
        test_data = [(1, 1, 2), (1, 0, 1), (0, 0, 0)]
        for x, y, expect in test_data:
            print("x={} y={} expect={}".format(x, y, expect))
            result = add(x, y)
            self.assertEqual(result, expect)
