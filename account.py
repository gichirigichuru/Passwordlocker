class Account:
  '''
  class that generates new instance of an account
  '''
  account_list = []

  def __init__(self, user_name, password):
    self.user_name = user_name
    self.password = password
  
    Account_list =[] #Empty account list
   # Init method up here
  def save_account(self):
    '''
    save_contact method saves contact objects into contact_list
    '''

    Account.account_list.append(self)

  def delete_account(self):

        '''
        delete_contact method deletes a saved contact from the contact_list
        '''

        Account.account_list.remove(self)  

  @classmethod
  def display_accounts(cls):
    '''
    method that returns the account list
    '''
    return cls.account_list
  
  
