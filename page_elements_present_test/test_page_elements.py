import requests
import pytest
from bs4 import BeautifulSoup

def test_home_page_has_right_title():
    url = 'http://www.caat.org.uk/' 
    response = requests.get(url)
    soup = BeautifulSoup( response.text, 'html.parser' )

    ###############################################################################
    # DELIBERATE FAIL:
    assert 'XXX Campaign Against the Arms Trade' in soup.title, 'did not find "XXX Campaign Against the Arms Trade" in home page title'
    ###############################################################################

def test_home_page_has_right_elements():
    url = 'http://www.caat.org.uk/' 
    response = requests.get(url)
    soup = BeautifulSoup( response.text, 'html.parser' )
    check_page_elements( soup.html.body, 'home page')


@pytest.mark.parametrize('page_name', [ 'about-caat', 'news', 'events', 'resources', ])         
def test_top_of_page_banner_pages_have_right_elements( page_name ):
    url = 'http://www.caat.org.uk/' + page_name
    response = requests.get(url)
    soup = BeautifulSoup( response.text, 'html.parser' )
    check_page_elements( soup.html.body, f'home/{page_name}')

def check_page_elements( body, page_name ):
    assert body.header, f'page {page_name} has no header page element'
    assert body.footer, f'page {page_name} has no footer page element'
    assert body.nav, f'page {page_name} has no nav page element'
    assert body.main, f'page {page_name} has no main page element'
    assert body.section, f'page {page_name} has no section page element'
    ###############################################################################
    # DELIBERATE FAIL:
    assert body.furtwangle, f'page {page_name} has no furtwangle page element'
    ###############################################################################
