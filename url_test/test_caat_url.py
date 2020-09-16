import urllib.request

def test_example():
    
    # returns 401:
    url = "https://2020.caat.org.uk/"
    
    # returns 200:
    # url = "https://www.caat.org.uk/"
    
    request = urllib.request.Request(url)
    response = urllib.request.urlopen(request)
    
    assert 200 == response.status