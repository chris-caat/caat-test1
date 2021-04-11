import requests
from requests.auth import HTTPBasicAuth

import os
print( "here" )
print( os.getcwd() )


# NB this directory is called "third_post" to make it look uninteresting
# D:\My Documents\sysadmin\Resources\third_post\data.txt
creds_path = os.path.expandvars(r'$SYSADMIN\Resources\third_post\data.txt')
print(f'creds_path |{creds_path}|')
file = open(creds_path)


user_line = file.readline()
user = user_line.split( ':' )[ 1 ].strip()
pwd_line = file.readline()
password = pwd_line.split( ':' )[ 1 ].strip()

print( f'user_line |{user_line}|, pwd_line |{pwd_line}|')

def test_example():
    print('running test...')
    url = "https://2020.caat.org.uk/"
    r = requests.get( url, auth=HTTPBasicAuth(user, password))
    assert 200 == r.status_code
    

test_example()
    
