import unittest
import sys
from lootbag import Bag


class TestBag(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.bag = Bag()

    def test_get_child(self):
        result = len(self.bag.get_child('Lucy'))
        null_result = len(self.bag.get_child('Merple'))
        self.assertEqual(result, 1)
        self.assertEqual(null_result, 0)

    def test_get_toy(self):
        result = len(self.bag.get_toy('Doll'))
        null_result = len(self.bag.get_toy('Flamethrower'))
        self.assertEqual(result, 1)
        self.assertEqual(null_result, 0)

    def test_add_and_delete(self):
        self.bag.add_toy('Chudley', 'Cannon')


        child_result = len(self.bag.get_child('Chudley'))
        toy_result = len(self.bag.get_toy('Cannon'))

        self.assertEqual(child_result, 1)
        self.assertEqual(toy_result, 1)

        self.bag.remove_child('Chudley')
        null_child_result = len(self.bag.get_child('Chudley'))
        null_toy_result = len(self.bag.get_toy('Cannon'))

        self.assertEqual(null_child_result, 0)
        self.assertEqual(null_toy_result, 0)

        self.bag.add_toy('Lucy', 'Switchblade')

        toy_result = len(self.bag.get_toy('Switchblade'))
        self.assertEqual(toy_result, 1)

        self.bag.remove_toy('Switchblade', 'Lucy')

        null_toy_result = len(self.bag.get_toy('Switchblade'))
        self.assertEqual(null_toy_result, 0)

if __name__ == '__main__':
    unittest.main()


