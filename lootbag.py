"""
App allows Santa's Workshop to add, remove and list toys in Santa's lootbag, as well as specify when a toy has been delivered-- using the CLI.

Commands:
python lootbag.py add {toy} {child_name}
python lootbag.py remove {child_name} {toy}
python lootbag.py ls    -- lists children receiving presents
python lootbag.py ls {child_name}   -- lists toys in bag for specific child
python lootbag.py delivered {child_name} -- specify when toys are delivered
"""

import sys
for x in sys.argv:
     print("Argument: ", x)


class Bag():

    def __init__(self):
        self.bag = []

    def add_toy(self):
        for self.bag