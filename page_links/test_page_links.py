import requests
import pytest
from bs4 import BeautifulSoup

def get_all_links_from_home_page():
    url = 'http://www.caat.org.uk/' 
    response = requests.get(url)
    soup = BeautifulSoup( response.text, 'html.parser' )
    return list( soup.html.body.select( 'a' ))

def pytest_generate_tests(metafunc):
    metafunc.parametrize( 'a_link', get_all_links_from_home_page() )

def test_all_links_200(a_link):
    assert a_link.has_attr( 'href' ), f'link without href: {a_link}'
    url = a_link[ 'href' ]
    # NB found with various links e.g. in home page... raises Exception in requests.get
    if url == '/' or url == '#':
        return
    try:
        response = requests.get( url )
    except Exception as e:
        print( 'requests.get() raised Exception: ', e )
        err_msg = f'a-link |{a_link}| with URL |{url}| rejected as invalid: examine URL'
        print( err_msg )
        raise Exception( err_msg )
    err_msg = f'on page home page: http request to page {url} returned incorrect status code: {response.status_code}. Expected: 200'
    assert response.status_code == 200, err_msg



# # @pytest.mark.skip
# @pytest.mark.parametrize('page_name', [ 'about-caat', 'news', 'events', 'resources', ])         
# def test_top_of_page_banner_pages_a_links( page_name ):
#     url = 'http://www.caat.org.uk/' + page_name
#     response = requests.get(url)
#     global soup 
#     soup = BeautifulSoup( response.text, 'html.parser' )
#     check_page_links( soup.html.body, f'home/{page_name}')


