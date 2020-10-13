import requests
import pytest

def test_homepage_https():
    url = 'https://www.caat.org.uk/'
    response = requests.get(url)
    assert response.status_code == 200, f'CAAT home page called with https returned incorrect status code: {response.status_code}'

def test_homepage_http():
    url = 'http://www.caat.org.uk/'
    response = requests.get(url)
    assert response.status_code == 200, f'CAAT home page called with http returned incorrect status code: {response.status_code}'

@pytest.mark.parametrize('page_name', [ 'about-caat', 'news', 'events', 'resources', ])         
def test_top_of_page_banner_pages( page_name ):
    url = 'http://www.caat.org.uk/' + page_name
    response = requests.get(url)
    assert response.status_code == 200, f'CAAT page/{page_name} called with http returned incorrect status code: {response.status_code}'

@pytest.mark.parametrize('page_name', [ '', 'the-arms-trade', 'government-support', 
        'who-buys-uk-arms', 'arms-companies', 'arms-fairs', 'militarism', 'policing',
        'borders', ])         
def test_challenges_pages( page_name ):
    url = 'http://www.caat.org.uk/challenges/' + page_name
    response = requests.get(url)
    assert response.status_code == 200, f'CAAT page challenges/{page_name} called returned incorrect status code: {response.status_code}'

@pytest.mark.parametrize('page_name', [ '', 'jobs', 'rethinking-security', 
    'arms-to-renewables', 'mythbusting', ])         
def test_alternatives_pages( page_name ):
    url = 'http://www.caat.org.uk/alternatives/' + page_name
    response = requests.get(url)
    assert response.status_code == 200, f'CAAT page alternatives/{page_name} called returned incorrect status code: {response.status_code}'

# TODO other pages linking from home page


