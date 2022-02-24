#!/usr/bin/env python3.8
from account import Account
def create_account(uname,password):
    '''
    Function to create a new account
    '''
    new_account = Account(uname,password)
    return new_account

def save_accounts(account):
    '''
    Function to save account
    '''
    account.save_account()
    
def delete_account(account):
  '''
  Function to delete account
  '''
  account.delete_account()

def display_accounts():
  '''
  Function to return all saved accounts
  '''
  return Account.display_accounts()

def check_existing_accounts(username):
  '''
  Function that check if an account exists with that username and return a Boolean
  '''
  return Account.account_exist(username)



