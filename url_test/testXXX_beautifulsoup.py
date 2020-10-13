import urllib.request
import pytest


from bs4 import BeautifulSoup

def test_home_page_has_right_title():
    url = 'http://www.caat.org.uk/' 
    request = urllib.request.Request(url)
    response = urllib.request.urlopen(request)

    soup = BeautifulSoup( response.text, 'html.parser' )
    print(soup.title)
    assert 'CAAT' in soup.title


