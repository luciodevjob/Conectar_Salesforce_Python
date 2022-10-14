import json
from turtle import update
import pandas as pd
from simple_salesforce import Salesforce, SalesforceLogin, SFType

loginInfo = json.load(open('login.json'))
username =   loginInfo['username'] 
password =  loginInfo['password']
security_token = loginInfo['security_token']
domain = 'login'

#sf = Salesforce(username=username, password=passowrd, security_token=security_token, domain=domain)
session_id, instance = SalesforceLogin(username=username, password=password, security_token=security_token, domain=domain)
sf = Salesforce(instance=instance, session_id=session_id)
print(sf)
Account = SFType('Account', session_id, instance)

data = {
    'Name': 'O Lucio criou com python',
    'CustomerPriority__c': 'High'
}

response = Account.create(data)
print(response)
