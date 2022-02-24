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
        self.new_account = Account("James","Muri123",) # create account object
    
    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_account.user_name,"James")
        self.assertEqual(self.new_account.password,"Muri123")

    def test_save_account(self):
        '''
        test_save_account test case to test if the account object is saved into
         the account list
        '''
        self.new_account.save_account() # saving the new account
        self.assertEqual(len(Account.account_list),1)

# setup and class creation up here
    def tearDown(self):
            '''
            tearDown method that does clean up after each test case has run.
            '''
            Account.account_list = []

    def test_save_multiple_account(self):
            '''
            test_save_multiple_contact to check if we can save multiple contact
            objects to our contact_list
            '''
            self.new_account.save_account()
            test_account = Account("Test","user") # new account
            test_account.save_account()
            self.assertEqual(len(Account.account_list),2)

    def test_delete_account(self):
            '''
            test_delete_account to test if we can remove a account from our account list
            '''
            self.new_account.save_account()
            test_account = Account("Test","user",) # new account
            test_account.save_account()

            self.new_account.delete_account()# Deleting a account object
            self.assertEqual(len(Account.account_list),1)


    def test_display_all_contacts(self):
            '''
            method that returns a list of all contacts saved
            '''
            self.assertEqual(Account.display_accounts(),Account.account_list)


if __name__ ==  '__main__':
    unittest.main()
