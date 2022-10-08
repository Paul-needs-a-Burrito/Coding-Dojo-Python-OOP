# Assignment: Intro to TDD
# Objectives:
#     Practice writing and running tests on an algorithm
# For the purpose of this assignment, do all of these in a single Python file.

# 1) reverseList - Write a function that reverses the values in the list (without creating a temporary array).
#   Example: reverseList([1,3,5]) should return [5,3,1]
#   Example Test: assertEqual( reverseList([1,3,5]), [5,3,1] )
#   Add at least 3 other test cases

import unittest


def reverseList(some_list):
    for i in range(int( len(some_list) / 2 )):
        temp = some_list[i]
        some_list[i] = some_list[len(some_list) - (1 + i)]
        some_list[len(some_list) - (1 + i)] = temp
    return some_list


class ReverseListTests(unittest.TestCase):
    def testOne(self):
        self.assertEqual(reverseList([1,3,5]), [5,3,1])
    def testTwo(self):
        self.assertEqual(reverseList([-3,9,0,7,-20,6]), [6,-20,7,0,9,-3])
    def testThree(self):
        self.assertEqual(reverseList(["a","b","c","d"]), ["d","c","b","a"])
    def testFour(self):
        self.assertEqual(reverseList([True,False,False]), [False,False,True])


if __name__ == '__main__':
    unittest.main()

# 2) isPalindrome - Write a function that checks whether the given word is a palindrome (a word that spells the same backward).
#   Example: isPalindrome("racecar") should return True
#   Example Test: assertEqual( isPalindrome("racecar"), True ) or assertTrue( isPalindrome("racecar"))
#   Example Test: assertFalse( isPalindrome("rabcr") ).
#   Add at least 5 other test cases

import unittest


def isPalindrome(word):
    word = str(word)
    for i in range( int( len(word)/2 ) ):
        if(word[i] == word[len(word) - 1 - i] ):
            return True


class IsPalindromeTests(unittest.TestCase):
    def testOne(self):
        self.assertTrue(isPalindrome("racecar"))
    def testTwo(self):
        self.assertFalse(isPalindrome("racecars"))
    def testThree(self):
        self.assertTrue(isPalindrome("ra7e7ar"))
    def testFour(self):
        self.assertTrue(isPalindrome("ra e ar"))
    def testFive(self):
        self.assertTrue(isPalindrome("racecaR"))
    def testSix(self):
        self.assertTrue(isPalindrome(7777))
    def testSeven(self):
        self.assertFalse(isPalindrome(7689))


if __name__ == '__main__':
    unittest.main()

# 3) coins - Write a function that determines how many quarters, dimes, nickels, and pennies to give to a customer for a change where you minimize the number of coins you give out.
#   Example: given 87 cents, result should be 3 quarters, 1 dime, 0 nickel and 2 pennies
#   Example Test: assertEqual( coin(87), [3,1,0,2] )
#   Add at least 5 other test cases

import unittest


def coins(num):
    quarters = int(num / 25)
    dimes = int( (num % 25) / 10)
    nickels = int( ( (num % 25) % 10 ) / 5)
    pennies = ( ( (num % 25) % 10 ) % 5)
    change = [quarters, dimes, nickels, pennies]
    return change


class CoinsTests(unittest.TestCase):
    def testOne(self):
        self.assertEqual(coins(87), [3,1,0,2])
    def testTwo(self):
        self.assertEqual(coins(1), [0,0,0,1])
    def testThree(self):
        self.assertEqual(coins(99), [3,2,0,4])
    def testFour(self):
        self.assertEqual(coins(5), [0,0,1,0])
    def testFive(self):
        self.assertEqual(coins(10), [0,1,0,0])
    def testSix(self):
        self.assertEqual(coins(0), [0,0,0,0])


if __name__ == '__main__':
    unittest.main()

# 4) BONUS - factorial - Write a recursive function that returns the factorial of a given number. Remember that the factorial of a number is the product of all the numbers between 1 and the given number (eg. 4! = 4*3*2*1).
#   Example: factorial(5) should return 120.
#   Add at least 3 test cases

import unittest


def factorial(num):
    if num == 0:
        return 1
    else:
        return num * factorial(num-1)


class FactorialTests(unittest.TestCase):
    def testOne(self):
        self.assertEqual(factorial(5), 120)
    def testTwo(self):
        self.assertEqual(factorial(0), 1)
    def testThree(self):
        self.assertEqual(factorial(3), 6)


if __name__ == '__main__':
    unittest.main()

# 5) BONUS - fibonacci - Write a recursive function that accepts a number, n, and returns the nth Fibonacci number from the sequence. The first two Fibonacci numbers are 0 and 1. Every number after that is calculated by adding the previous 2 numbers from the sequence. (i.e. 0, 1, 1, 2, 3, 5, 8, 13, 21 ...)
#   Example: fibonacci(5) should return 3 (the 5th number in the sequence is 3).
#   Add at least 3 test cases
