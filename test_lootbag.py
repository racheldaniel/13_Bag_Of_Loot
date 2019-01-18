import unittest
import sys
from lootbag import Bag


class TestBag(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.bag = Bag()

    def test_get_null_child(self):
        null_result = len(self.bag.get_child('Merple'))
        self.assertEqual(null_result, 0)

    def test_get_null_toy(self):
        null_result = len(self.bag.get_toy('Flamethrower'))
        self.assertEqual(null_result, 0)

    def test_add_get_delete(self):

        """test add_toy, get_toy, get_child, remove_toy and remove_child

            -Create a new child 'Chudley'
            -Add 'Cannon' and 'Switchblade' as toys for Chudley
            -Check that child and both toys are added
            -Delete Switchblade, make sure it's gone
            -Delete Chudley, make sure both Chudley and Cannon are gone
        """

        self.bag.add_toy( 'Cannon', 'Chudley')
        self.bag.add_toy( 'Switchblade', 'Chudley')

        toy_result = len(self.bag.get_toy('Switchblade'))
        self.assertEqual(toy_result, 1)

        child_result = len(self.bag.get_child('Chudley'))
        toy_result = len(self.bag.get_toy('Cannon'))

        self.assertEqual(child_result, 1)
        self.assertEqual(toy_result, 1)

        self.bag.remove_toy('Chudley', 'Switchblade')

        null_toy_result = len(self.bag.get_toy('Switchblade'))
        self.assertEqual(null_toy_result, 0)

        self.bag.remove_child('Chudley')
        null_child_result = len(self.bag.get_child('Chudley'))
        null_toy_result = len(self.bag.get_toy('Cannon'))

        self.assertEqual(null_child_result, 0)
        self.assertEqual(null_toy_result, 0)


    def test_list_children_and_toys(self):

        starting_child = len(self.bag.list_children())
        expected_child = starting_child + 1

        self.bag.add_toy('Hand Grenade', 'Merple')
        result_child = len(self.bag.list_children())

        self.assertEqual(result_child, expected_child)

        toy_length = len(self.bag.list_child_toys('Merple'))
        self.assertEqual(toy_length, 1)

        self.bag.remove_child('Merple')


    def test_delivered(self):
        self.bag.add_toy('Loose Teeth', 'Derp')
        result = self.bag.get_child('Derp')[0][2]

        self.assertEqual(result, 0)

        self.bag.deliver_toys('Derp')
        result = self.bag.get_child('Derp')[0][2]

        self.assertEqual(result, 1)

        self.bag.remove_child('Derp')






if __name__ == '__main__':
    unittest.main()


