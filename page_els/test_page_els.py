import requests
import pytest
from bs4 import BeautifulSoup

# PS I suspect use of global variables is not encouraged...
soup = None

# @pytest.mark.skip
def test_home_page_has_right_title():
    url = 'http://www.caat.org.uk/' 
    response = requests.get(url)
    global soup 
    soup = BeautifulSoup( response.text, 'html.parser' )

    ###############################################################################
    # DELIBERATE FAIL:
    # full_name = 'XXX Campaign Against the Arms Trade'

    full_name = 'Campaign Against the Arms Trade'
    assert full_name in soup.title, f'did not find "{full_name}" in home page title'
    ###############################################################################

# @pytest.mark.skip
def test_home_page_has_right_elements():
    url = 'http://www.caat.org.uk/' 
    response = requests.get(url)
    global soup 
    soup = BeautifulSoup( response.text, 'html.parser' )
    check_page_elements( soup.html.body, 'home page')

# @pytest.mark.skip
@pytest.mark.parametrize('page_name', [ 'about-caat', 'news', 'events', 'resources', ])         
def test_top_of_page_banner_pages_have_right_elements( page_name ):
    url = 'http://www.caat.org.uk/' + page_name
    response = requests.get(url)
    global soup 
    soup = BeautifulSoup( response.text, 'html.parser' )
    check_page_elements( soup.html.body, f'home/{page_name}')

# @pytest.mark.skip
@pytest.mark.parametrize('page_name', [ '', 'the-arms-trade', 'government-support', 
'who-buys-uk-arms', 'arms-companies', 'arms-fairs', 'militarism', 'policing', 'borders',])         
def test_challenges_pages( page_name ):
    url = 'http://www.caat.org.uk/challenges/' + page_name
    response = requests.get(url)
    global soup 
    soup = BeautifulSoup( response.text, 'html.parser' )
    check_page_elements( soup.html.body, f'home/challenges/{page_name}')


def check_page_elements( body, page_name ):
    assert body.header, f'page {page_name} has no header page element'
    assert body.footer, f'page {page_name} has no footer page element'
    assert body.nav, f'page {page_name} has no nav page element'
    assert body.main, f'page {page_name} has no main page element'
    assert body.section, f'page {page_name} has no section page element'

    ###############################################################################
    # DELIBERATE FAIL:
    # assert body.furtwangle, f'page {page_name} has no furtwangle page element'
    ###############################################################################

