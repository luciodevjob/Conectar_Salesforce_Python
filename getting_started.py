import json
import pandas as pd
import io
import numpy as np
from simple_salesforce import Salesforce, SalesforceLogin, SFType

loginInfo = json.load(open('login.json'))
username =   loginInfo['username'] #"luciolco02@gmail.com"   loginInfo['username']
password =  loginInfo['password']
security_token = loginInfo['security_token']
domain = 'login'

#sf = Salesforce(username=username, password=passowrd, security_token=security_token, domain=domain)
session_id, instance = SalesforceLogin(username=username, password=password, security_token=security_token, domain=domain)
sf = Salesforce(instance=instance, session_id=session_id)

# Values = ['Energy', 'Banking']
# WHERE Industry IN('{0}')""".format("','".join(Values))
querySOQL = """SELECT Id, Name, StageName, Account.Name, Account.Type, Account.Industry FROM Opportunity"""


response = sf.query(querySOQL)
lstRecords = response.get('records')
nextRecordsUrl = response.get('nextRecordsUrl')

while not response.get('done'):
    response = sf.query_more(nextRecordsUrl, identifier_is_url=True)
    lstRecords.extend(response.get('records'))
    nextRecordsUrl = response.get('nextRecordsUrl')

df_records = pd.DataFrame(lstRecords)
dfAccount = df_records['Account'].apply(pd.Series).drop(labels='attributes', axis=1, inplace=False)
dfAccount.columns = ('Account.{0}'.format(name) for name in dfAccount.columns)

df_records.drop(labels=['Account', 'attributes'], axis=1, inplace=True)

dfOpptyAcct = pd.concat([df_records, dfAccount], axis=1)
#dfOpptyAcct.to_csv('Opp2', index=False)
final = pd.ExcelWriter('dfOpptyAcct.xlsx')

dfOpptyAcct.to_excel(final, index=False)
final.save()
print(dfOpptyAcct)
