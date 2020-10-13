import requests
import pytest

from bs4 import BeautifulSoup

def test_home_page_has_right_title():
    url = 'http://www.caat.org.uk/' 
    response = requests.get(url)

    soup = BeautifulSoup( response.text, 'html.parser' )
    print(soup.title)
    assert 'Campaign Against the ArmsXXX Trade' in soup.title, 'did not find "Campaign Against the Arms Trade" in home page title'


