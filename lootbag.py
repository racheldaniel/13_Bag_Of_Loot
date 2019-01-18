"""
App allows Santa's Workshop to add, remove and list toys in Santa's lootbag, as well as specify when a toy has been delivered-- using the CLI.

Commands:
python lootbag.py add {toy} {child_name}
python lootbag.py remove {child_name} {toy}
python lootbag.py ls    -- lists children receiving presents
python lootbag.py ls {child_name}   -- lists toys in bag for specific child
python lootbag.py delivered {child_name} -- specify when toys are delivered
"""
import sqlite3
import sys
for x in sys.argv:
     print("Argument: ", x)


class Bag():

    __lootbag = '/Users/rachel/workspace/python/exercises/13_bag_of_loot/lootbag.db'


    def get_child(self, child_name):
        with sqlite3.connect(self.__lootbag) as conn:
                cursor = conn.cursor()
                cursor.execute(
                    f"SELECT * FROM Child WHERE Child.Name = '{child_name}'")
                child = cursor.fetchall()
                return child

    def get_toy(self, toy_name):
        with sqlite3.connect(self.__lootbag) as conn:
                cursor = conn.cursor()

                cursor.execute(f"SELECT * FROM Toy WHERE Name = '{toy_name}'")
                toy = cursor.fetchall()
                return toy

    def call_funct(self, args):
        """ Call the correct function based on sys.args
            Takes one argument -- set of sys.args"""
        if args[1] == "add" and len(args) == 4:
            self.add_toy(args[2], args[3])
        elif args[1] == "remove" and len(args) == 4:
            self.remove_toy(args[2], args[3])
        elif args[1] == "ls" and len(args) == 2:
            self.list_children()
        elif args[1] == "ls" and len(args) == 3:
            self.list_child_toys(args[2])

    def add_toy(self, child_name, toy_name):
        """ Add toy to bag-- first check to see if child exists. If not, add both a child and toy to the db

            Takes two arguments:

            child_name -- String
            toy_name -- String
        """
        child_id = ""
        child = self.get_child(child_name)
        if len(child) == 1:
            child_id = child[0][0]
            with sqlite3.connect(self.__lootbag) as conn:
                cursor = conn.cursor()
                try:
                    cursor.execute(
                        '''
                        INSERT INTO Toy
                        VALUES(?,?,?)
                        ''', (None, toy_name, child_id)
                    )
                except sqlite3.OperationalError as err:
                    print("oops", err)
        else:
            with sqlite3.connect(self.__lootbag) as conn:
                cursor = conn.cursor()
                try:
                    cursor.execute(
                        '''
                        INSERT INTO Child
                        VALUES(?,?,?)
                        ''', (None, child_name, False)
                    )
                    child_id = cursor.lastrowid
                except sqlite3.OperationalError as err:
                    print("oops", err)

            with sqlite3.connect(self.__lootbag) as conn:
                cursor = conn.cursor()
                try:
                    cursor.execute(
                        '''
                        INSERT INTO Toy
                        VALUES(?,?,?)
                        ''', (None, toy_name, child_id)
                    )
                except sqlite3.OperationalError as err:
                    print("oops", err)

    def remove_toy(self, toy_name, child_name):
        """ Remove toy from bag-- first check to see if child exists. If not, add both a child and toy to the db

            Takes two arguments:

            child_name -- String
            toy_name -- String
        """
        child = self.get_child(child_name)
        if len(child) == 1:
            child_id = child[0][0]
            with sqlite3.connect(self.__lootbag) as conn:
                cursor = conn.cursor()
                try:
                    cursor.execute(
                        f'''
                        DELETE FROM Toy
                        WHERE Toy.ChildId = '{child_id}'
                        AND Toy.Name = '{toy_name}'
                        '''
                    )
                except sqlite3.OperationalError as err:
                    print("oops", err)
        else:
            raise ValueError("Oops, I can't find that child")

    def remove_child(self, child_name):
        child = self.get_child(child_name)
        if len(child) == 1:
            child_id = child[0][0]
            with sqlite3.connect(self.__lootbag) as conn:
                cursor = conn.cursor()
                try:
                    cursor.execute(
                        f'''
                        DELETE FROM Child
                        WHERE Child.Name = '{child_name}'
                        '''
                    )
                except sqlite3.OperationalError as err:
                    print("oops", err)
            #TODO: This should be cascading but currently isn't
            with sqlite3.connect(self.__lootbag) as conn:
                cursor = conn.cursor()
                try:
                    cursor.execute(
                        f'''
                        DELETE FROM Toy
                        WHERE Toy.ChildId = '{child_id}'
                        '''
                    )
                except sqlite3.OperationalError as err:
                    print("oops", err)
        else:
            raise ValueError("That child doesn't seem to have any toys")

    def list_children(self):
        with sqlite3.connect(self.__lootbag) as conn:
            cursor = conn.cursor()
            try:
                cursor.execute("SELECT Child.Name FROM Child")
                children = cursor.fetchall()
                print(children)
            except sqlite3.OperationalError as err:
                print("oops", err)

    def list_child_toys(self, child_name):
        child = self.get_child(child_name)
        if len(child) == 1:
            child_id = child[0][0]
            with sqlite3.connect(self.__lootbag) as conn:
                cursor = conn.cursor()
                try:
                    cursor.execute(f"SELECT Toy.Name FROM Toy WHERE Toy.ChildId = '{child_id}'")
                    child_toys = cursor.fetchall()
                    print(child_toys)
                except sqlite3.OperationalError as err:
                    print("oops", err)
        else:
            raise ValueError("I can't find that child")

if __name__ == '__main__':
    bag = Bag()
    bag.call_funct(sys.argv)
    print(bag.__dict__)

