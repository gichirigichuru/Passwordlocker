import unittest # Importing the unittest module
from account import Account #importing the account class
class TestAccount(unittest.TestCase):
    '''
    Test class that defines test cases for the account class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
  '''
      # Items up here .......

    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_account = Account("James","Muri123",) # create contact object
    
    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_account.user_name,"James")
        self.assertEqual(self.new_account.password,"Muri123")
if __name__ == '__main__':
    unittest.main()