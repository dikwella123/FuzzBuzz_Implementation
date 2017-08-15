import unittest

from fuzzbuzzsolution import fizzbuzz 
class FizzBuzzAcceptanceTestCase(unittest.TestCase):
    '''
    Test that fizzbuzz(int) returns int
    unless multiple of 3 (then returns 'fizz')
           multiple of 5 (then returns 'buzz')
           multiple of both (then returns 'fizzbuzz')
    '''
    def test_business_as_usual(self):
        '''
        test that an integer greater or equal to 0 not evenly divisible
        by three or five returns the same
        '''
        self.assertEqual(fizzbuzz(1), 1, msg='Invalid number.')
        self.assertEqual(fizzbuzz(2), 2, msg='Invalid number.')
        self.assertEqual(fizzbuzz(4), 4, msg='Invalid number.')
        self.assertEqual(fizzbuzz(7), 7, msg='Invalid number.')
        self.assertEqual(fizzbuzz(998), 998, msg='Invalid number.')
    def test_fizz(self):
        '''evenly divisible by 3 returns fizz'''
        self.assertEqual(fizzbuzz(3), 'fizz', msg='Invalid number.')
        self.assertEqual(fizzbuzz(6), 'fizz', msg='Invalid number.')
        self.assertEqual(fizzbuzz(111), 'fizz', msg='Invalid number.')
        self.assertEqual(fizzbuzz(999), 'fizz', msg='Invalid number.')
    def test_buzz(self):
        '''evenly divisible by 5 returns buzz'''
        self.assertEqual(fizzbuzz(5), 'buzz', msg='Invalid number.')
        self.assertEqual(fizzbuzz(10), 'buzz', msg='Invalid number.')
        self.assertEqual(fizzbuzz(20), 'buzz', msg='Invalid number.')
        self.assertEqual(fizzbuzz(500), 'buzz', msg='Invalid number.')
    
    def test_fizz_buzz(self):
        '''evenly divisible by 3 and 5 returns fizzbuzz'''
        self.assertEqual(fizzbuzz(15), 'fizzbuzz', msg='Invalid number sorry.')
        self.assertEqual(fizzbuzz(30), 'fizzbuzz', msg='Invalid number sorry.')
        self.assertEqual(fizzbuzz(45), 'fizzbuzz', msg='Invalid number sorry.')
        self.assertEqual(fizzbuzz(600), 'fizzbuzz', msg='Invalid number sorry.')
        
    def test_zero(self):
        self.assertEqual(fizzbuzz(0), 'fizzbuzz', msg='Invalid number sorry.') 

def main():
    unittest.main()

if __name__ == '__main__':
    main()