# Name:CHE-HAN HSU
# OSU Email:hsuche@oregonstate.edu
# Course: CS261 - Data Structures
# Assignment:assignment 2
# Due Date:29,04,2024
# Description:a Bag class that uses a DynamicArray under the hood.


from dynamic_array import *


class Bag:
    def __init__(self, start_bag=None):
        """
        Init new bag based on Dynamic Array
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self._da = DynamicArray()

        # populate bag with initial values (if provided)
        # before using this feature, implement add() method
        if start_bag is not None:
            for value in start_bag:
                self.add(value)

    def __str__(self) -> str:
        """
        Return content of stack in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = "BAG: " + str(self._da.length()) + " elements. ["
        out += ', '.join([str(self._da.get_at_index(_))
                          for _ in range(self._da.length())])
        return out + ']'

    def size(self) -> int:
        """
        Return total number of items currently in the bag
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self._da.length()

    # -----------------------------------------------------------------------

    def add(self, value: object) -> None:

        self.dynamic_array.append(value)  # Append the value to the dynamic array

        if len(self.dynamic_array) == self.dynamic_array.capacity:  # If the dynamic array has reached its capacity, resize it (e.g., double its size)
            self.dynamic_array.resize(2 * self.dynamic_array.capacity)

        """
        TODO: Write this implementation
        """
        pass

    def remove(self, value: object) -> bool:

        for i in range(self.size):   # Search for the value

            if self.data[i] == value:
                for j in range(i, self.size - 1):  # Shift subsequent elements to the left
                    self.data[j] = self.data[j + 1]
                self.size -= 1
                return True

        return False   # Value not found

        """
        TODO: Write this implementation
        """
        pass

    def count(self, value: object) -> int:

        count = 0
        for item in self.elements:
            if item == value:
                count += 1
        return count

        """
        TODO: Write this implementation
        """
        pass

    def clear(self) -> None:

        self.elements = []   # Reset the internal data structure
        """
        TODO: Write this implementation
        """
        pass

    def equal(self, second_bag: "Bag") -> bool:

        if len(self.elements) != len(second_bag.elements):  # Check if the number of elements is the same
            return False

        for elem in self.elements:  # Verify that all elements exist in the second bag
            if elem not in second_bag.elements:
                return False

        return True  # All checks passed; the bags are equal


        """
        TODO: Write this implementation
        """
        pass

    def __iter__(self):

        self._index = 0

        return self

        """
        TODO: Write this implementation
        """
        pass

    def __next__(self):

        try:
            while True:
                item = next(bag_iterator)
                print(item)
      except StopIteration:

        """
        TODO: Write this implementation
        """
        pass


# ------------------- BASIC TESTING -----------------------------------------


if __name__ == "__main__":

    print("\n# add example 1")
    bag = Bag()
    print(bag)
    values = [10, 20, 30, 10, 20, 30]
    for value in values:
        bag.add(value)
    print(bag)

    print("\n# remove example 1")
    bag = Bag([1, 2, 3, 1, 2, 3, 1, 2, 3])
    print(bag)
    print(bag.remove(7), bag)
    print(bag.remove(3), bag)
    print(bag.remove(3), bag)
    print(bag.remove(3), bag)
    print(bag.remove(3), bag)

    print("\n# count example 1")
    bag = Bag([1, 2, 3, 1, 2, 2])
    print(bag, bag.count(1), bag.count(2), bag.count(3), bag.count(4))

    print("\n# clear example 1")
    bag = Bag([1, 2, 3, 1, 2, 3])
    print(bag)
    bag.clear()
    print(bag)

    print("\n# equal example 1")
    bag1 = Bag([10, 20, 30, 40, 50, 60])
    bag2 = Bag([60, 50, 40, 30, 20, 10])
    bag3 = Bag([10, 20, 30, 40, 50])
    bag_empty = Bag()

    print(bag1, bag2, bag3, bag_empty, sep="\n")
    print(bag1.equal(bag2), bag2.equal(bag1))
    print(bag1.equal(bag3), bag3.equal(bag1))
    print(bag2.equal(bag3), bag3.equal(bag2))
    print(bag1.equal(bag_empty), bag_empty.equal(bag1))
    print(bag_empty.equal(bag_empty))
    print(bag1, bag2, bag3, bag_empty, sep="\n")

    bag1 = Bag([100, 200, 300, 200])
    bag2 = Bag([100, 200, 30, 100])
    print(bag1.equal(bag2))

    print("\n# __iter__(), __next__() example 1")
    bag = Bag([5, 4, -8, 7, 10])
    print(bag)
    for item in bag:
        print(item)

    print("\n# __iter__(), __next__() example 2")
    bag = Bag(["orange", "apple", "pizza", "ice cream"])
    print(bag)
    for item in bag:
        print(item)
