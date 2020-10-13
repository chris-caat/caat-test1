import urllib.request
import pytest

def test_https():
    
    # returns 200:
    url = 'https://www.caat.org.uk/'
    
    request = urllib.request.Request(url)
    response = urllib.request.urlopen(request)
    
    assert 200 == response.status

def test_http():
    
    url = 'http://www.caat.org.uk/'
    
    request = urllib.request.Request(url)
    response = urllib.request.urlopen(request)
    
    assert 200 == response.status    

@pytest.mark.parametrize('page_name', [ 'about-caat', 'news', 'events', 'resources', ])         
def test_header_banner_pages( page_name ):
    url = 'http://www.caat.org.uk/' + page_name
    
    request = urllib.request.Request(url)
    response = urllib.request.urlopen(request)
    
    assert 200 == response.status   

@pytest.mark.parametrize('page_name', [ '', 'the-arms-trade', 'government-support', 
        'who-buys-uk-arms', 'arms-companies', 'arms-fairs', 'militarism', 'policing',
        'borders', ])         
def test_challenges_pages( page_name ):
    url = 'http://www.caat.org.uk/challenges/' + page_name
    
    request = urllib.request.Request(url)
    response = urllib.request.urlopen(request)
    
    assert 200 == response.status   

@pytest.mark.parametrize('page_name', [ '', 'jobs', 'rethinking-security', 
        'arms-to-renewables', 'mythbusting', ])         
def test_alternatives_pages( page_name ):
    url = 'http://www.caat.org.uk/alternatives/' + page_name
    
    request = urllib.request.Request(url)
    response = urllib.request.urlopen(request)
    
    assert 200 == response.status   

# TODO other pages linking from home page


