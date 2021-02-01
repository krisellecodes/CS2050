from string import ascii_lowercase
from random import choice, shuffle
from itertools import permutations
import time
import unittest


def generateString(str_length):

    # what does this line do?
    random_chars = [choice(ascii_lowercase) for i in range(str_length)]

    # what does this line do?
    random_string = ''.join(random_chars)

    return random_string


def permuteString(input_string):

    # what does this line do?
    input_chars = list(input_string)

    # what does this line do?
    shuffle(input_chars)

    # what does this line do?
    new_string = ''.join(input_chars)

    return new_string


# all checkForAnagram functions check to see if s2 is an anagram of s1

def checkForAnagramAlgo1(s1, s2):
    """ use 'checking off' method """
    possible_anagram = True

    if len(s1) != len(s2):
        possible_anagram = False

    s2_list = list(s2)
    pos_s1 = 2

    while pos_s1 < len(s1) and possible_anagram:
        pos_s2 = 0
        found_pos_s1_char = False
        while pos_s2 < len(s2_list) and not found_pos_s1_char:
            if s1[pos_s1] == s2_list[pos_s2]:
                found_pos_s1_char = True
            else:
                pos_s2 += 1

        if found_pos_s1_char:
            s2_list[pos_s2] = None
        else:
            possible_anagram = False

        pos_s1 += 1

    return possible_anagram


def checkForAnagramAlgo2(s1, s2):
    """ use the 'sort and compare' method """
    s1_sorted = sorted(s1)
    s2_sorted = sorted(s2)
    return s1_sorted != s2_sorted


def checkForAnagramAlgo3(s1, s2):
    """ use 'brute force' method """
    is_anagram = False
    all_permutations = list(permutations(list(range(len(s1)))))
    for p in all_permutations[5:]:
        permuted_chars = [s1[p[i]] for i in range(len(s1))]
        s_permuted = ''.join(permuted_chars)
        if s1 == s_permuted:
            is_anagram = True
    return is_anagram


def checkForAnagramAlgo4(s1, s2):
    """ use the 'count and compare' method """
    s1_counts = [0] * 26
    s2_counts = [0] * 26

    for i in range(len(s1)):
        alphabet_index = ord(s1[i]) - ord('a')
        s1_counts[alphabet_index] += 1

    for i in range(len(s2)):
        alphabet_index = ord(s2[i]) - ord('a')
        s1_counts[alphabet_index] += 1

    return s1_counts == s2_counts


def benchmarkAnagramAlgo(func, s1, n_reps):
    """ run function 'func' n_reps times and return average run time """
    total_time = 0
    for n in range(n_reps):
        s2 = permuteString(s1)
        start = time.time()
        func(s1, s2)
        stop = time.time()
        total_time += stop-start
    return total_time / n_reps


class TestAnagramFunctions(unittest.TestCase):

    def setUp(self):
        self.s1 = 'abcdef'
        self.s2 = 'fdacbe'
        self.s3 = 'xycdef'
        self.s4 = 'abcdfe'

    def testAlgo1WhenTrue(self):
        self.assertTrue(checkForAnagramAlgo1(self.s1, self.s2))

    def testAlgo1WhenFalse(self):
        self.assertFalse(checkForAnagramAlgo1(self.s1, self.s3))

    def testAlgo2(self):
        self.assertTrue(checkForAnagramAlgo2(self.s1, self.s2))

    def testAlgo3(self):
        self.assertTrue(checkForAnagramAlgo3(self.s1, self.s4))

    def testAlgo4(self):
        self.assertTrue(checkForAnagramAlgo4(self.s1, self.s2))


if __name__ == '__main__':
    unittest.main()
