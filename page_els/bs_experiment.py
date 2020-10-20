from bs4 import BeautifulSoup
import requests

url = 'https://www.caat.org.uk'
req = requests.get(url)
soup = BeautifulSoup(req.text, 'html.parser' )
print(soup.title)

a_links = soup.find_all( 'a' )

body_contents = soup.html.body.contents

p = hasattr( soup.html.body, 'header' )
q = hasattr( soup.html.body, 'headerXYX' )    

header = soup.html.body.header
assert( header )


link_list = list( soup.html.body.select( 'a' ) )

print( link_list )
