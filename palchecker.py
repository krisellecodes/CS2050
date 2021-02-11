import unittest
from deque import Deque

def palCheck(input_string):
    """
    a function to check whether or not the input string is a palindrome
    (i.e. a string that is the same backwards as it is forwards)
    """

    # ADD NECESSARY LINES OF CODE SO THAT ALL UNITTESTS PASS

    d = Deque()
    for char in input_string:
        d.addFront(char)

    while d.size() > 1:
        firstChar = d.removeRear()
        lastChar = d.removeFront()
        if firstChar != lastChar:
            print("No, '" + input_string + "', is not a palindrom")
            return False

    print("Yes, '" + input_string + "', is a palindrom!!")
    return True


class TestPalChecker(unittest.TestCase):

    def testBasicTest(self):
        self.assertTrue(palCheck("racecar"))

    def testCapitlization(self):
        self.assertTrue(palCheck("Racecar"))

    def testSpace(self):
        self.assertTrue(palCheck("race car"))

    def testSentence(self):
        self.assertTrue(palCheck("A man a plan a canal Panama."))

if __name__ == "__main__":
    unittest.main()
