import requests
from requests.auth import HTTPBasicAuth

file = open( '../../data.txt' )
user_line = file.readline()
user = user_line.split( ':' )[ 1 ].strip()
pwd_line = file.readline()
password = pwd_line.split( ':' )[ 1 ].strip()

def test_example():
    url = "https://2020.caat.org.uk/"
    r = requests.get( url, auth=HTTPBasicAuth(user, password))
    assert 200 == r.status_code
    
