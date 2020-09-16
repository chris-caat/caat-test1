import requests

def test_example():
    
    url = "https://2020.caat.org.uk/"
   
    login_data = dict(login='xxxx', password='xxxx')
    
    session = requests.session()
    r = session.get(url, data=login_data)
    
    assert 200 == r.status_code
    
