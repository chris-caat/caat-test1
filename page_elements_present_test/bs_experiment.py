from bs4 import BeautifulSoup
import requests

url = 'https://www.caat.org.uk'
req = requests.get(url)
soup = BeautifulSoup(req.text, 'html.parser' )
print(soup.title)

a_links = soup.find_all( 'a' )

# print( a_links )

# print( soup.contents )

# for child in soup.contents:
#     print( child.name )
#     if child.name == 'html':
#         html_children = child.contents
#         for html_child in html_children:
#             print( html_child.name )

body_contents = soup.html.body.contents

for body_child in body_contents:
    if body_child.name and body_child.name != 'script':
        print( body_child.name )

if hasattr( soup.html.body, 'header' ):
    print( 'found header' )
if hasattr( soup.html.body, 'headerXYX' ):
    print( 'found headerXYX' )    

p = hasattr( soup.html.body, 'header' )
q = hasattr( soup.html.body, 'headerXYX' )    

print( p, q )
print( dir( soup.html.body ))

header = soup.html.body.header
assert( header )
headerXXX = soup.html.body.headerXXX
assert( headerXXX )