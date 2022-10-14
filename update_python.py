import json
from turtle import update
import pandas as pd
from simple_salesforce import Salesforce, SalesforceLogin, SFType

loginInfo = json.load(open('login.json'))
username =   loginInfo['username'] #"luciolco02@gmail.com"   loginInfo['username']
password =  loginInfo['password']
security_token = loginInfo['security_token']
domain = 'login'

#sf = Salesforce(username=username, password=passowrd, security_token=security_token, domain=domain)
session_id, instance = SalesforceLogin(username=username, password=password, security_token=security_token, domain=domain)
sf = Salesforce(instance=instance, session_id=session_id)
print(sf)
Account = SFType('Account', session_id, instance)

data = {
    'Id': '0018a00001wjWaxAAE'
    
}

update_data = {}
update_data['Name'] = 'Lucio Mudou com o python'

Account.update(data['Id'], update_data)