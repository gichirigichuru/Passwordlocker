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
