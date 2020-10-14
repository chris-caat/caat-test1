import requests
import pytest

def test_homepage_https():
    url = 'https://www.caat.org.uk/'
    response = requests.get(url)
    assert response.status_code == 200, f'home page called with https returned incorrect status code: {response.status_code}'

@pytest.mark.parametrize('page_name', [ '', 'about-caat', 'news', 'events', 'resources', ])         
def test_top_of_page_banner_pages( page_name ):
    check_response_code( '', page_name )

@pytest.mark.parametrize('page_name', [ '', 'the-arms-trade', 'government-support', 
        'who-buys-uk-arms', 'arms-companies', 'arms-fairs', 'militarism', 'policing',
        'borders', ])         
def test_challenges_pages( page_name ):
    check_response_code( 'challenges', page_name )

@pytest.mark.parametrize('page_name', [ '', 'jobs', 'rethinking-security', 
    'arms-to-renewables', 'mythbusting', ])         
def test_alternatives_pages( page_name ):
    check_response_code( 'alternatives', page_name )

@pytest.mark.parametrize('page_name', [ '', 'campaign-with-us', 'take-part-near-you', ])         
def test_take_action_pages( page_name ):
    check_response_code( 'take-action', page_name )

def check_response_code( section_name, page_name ):
    if section_name:
        url = f'http://www.caat.org.uk/{section_name}/{page_name}'
    else:
        url = f'http://www.caat.org.uk/{page_name}'
    response = requests.get(url)
    err_msg = f'http request to page {section_name}/{page_name} returned incorrect status code: {response.status_code}'
    assert response.status_code == 200, err_msg



# TODO other pages linking from home page


