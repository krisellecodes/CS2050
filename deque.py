import unittest

class Deque:
    """ a custom double-ended queue using a python list """

    def __init__(self):
        """ instantiate the single field/attribute for our deque """
        self.dequeList = []

    def __str__(self):
        """ override str funtion so that internal dequeList prints nicely """
        return str(self.dequeList)

    def isEmpty(self):
        """ return True if dequeList is empty, and False otherwise """
        return len(self.dequeList) == 0

    def addRear(self, new_item):
        """ add a new item to the back (left) of the deque """
        self.dequeList.insert(0, new_item)

    def addFront(self, new_item):
        """ add a new item to the front (right)) of the deque """
        self.dequeList.append(new_item)

    def removeRear(self):
        """ remove and return item from the back (left) of the deque """
        return self.dequeList.pop(0)

    def removeFront(self):
        """ remove and return item from the front (right) of the deque """
        return self.dequeList.pop()

    def peekRear(self):
        """ return (but don't remove) item from the back (left) of the deque """
        return self.dequeList[0]

    def peekFront(self):
        """ return (but don't remove ) item from the front (right) of the deque """
        return self.dequeList[-1]

    def size(self):
        """ return number of items in the deque """
        return len(self.dequeList)

class TestDeque(unittest.TestCase):

    def testAddFront(self):
        d = Deque()
        d.addRear(8)
        # ADD LINE(S) NEEDED HERE FOR THIS TEST TO PASS
        d.addRear(5)
        self.assertIn("[5, 8, 9]", str(d))

    def testRemoveFront(self):
        d = Deque()
        # ADD LINE(S) NEEDED HERE FOR THIS TEST TO PASS
        d.addRear(8)
        d.addRear(5)
        remove_front_item = d.removeFront()
        self.assertEqual(remove_front_item, 7)

if __name__ == '__main__':
    unittest.main()

