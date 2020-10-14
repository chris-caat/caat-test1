import requests
import pytest
from bs4 import BeautifulSoup

def get_all_links_from_pages():
    # NB this now produces some 550 links from the home page + 4 "top banner" pages - 
    # the test took 3 1/2 minutes the first time it was run... but will normally 
    # probably take longer

    page_names =  [ '', 'about-caat', 'news', 'events', 'resources', ]
    a_links = []
    for page_name in page_names:
        url = 'http://www.caat.org.uk/' + page_name
        response = requests.get(url)
        soup = BeautifulSoup( response.text, 'html.parser' )
        a_links.extend( [ ( x, page_name ) for x in soup.html.body.select( 'a' )] )
    return a_links

def pytest_generate_tests(metafunc):
    metafunc.parametrize( 'link_tuple', get_all_links_from_pages() )

def test_all_links_200(link_tuple):
    a_link = link_tuple[ 0 ]
    page_name = link_tuple[ 1 ]

    assert a_link.has_attr( 'href' ), f'page /{page_name}: link without href: {a_link}'
    url = a_link[ 'href' ]
    # NB found with various links e.g. in home page... raises Exception in requests.get
    if url == '/' or url == '#':
        return
    try:
        response = requests.get( url )
    except Exception as e:
        print( 'requests.get() raised Exception: ', e )
        err_msg = f'page /{page_name}: a-link |{a_link}| with URL |{url}| rejected as invalid: examine URL'
        print( err_msg )
        raise Exception( err_msg )
    err_msg = f'page /{page_name}: http request to page {url} returned incorrect status code: {response.status_code}. Expected: 200'
    assert response.status_code == 200, err_msg