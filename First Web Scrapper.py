# Importing Libraries 

!pip install bs4
!pip install requests
!pip3 install lxml --user  # needs to be installed seperately
!pip install html5lib      # needs to be installed seperately

# Installing Libraries

from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError


# Defining function to read a url and fetch its title.

def getTitle(url):
    try:
        html = urlopen(url)  #urlopen fetches data from the url
    except HTTPError as e:
        return None
    try:
        bsObj= BeautifulSoup(html, "html5lib") 

# html5lib is used when data is messy. Although slower than both "lxml" and "html.parser", This works best for poorly formatted web pade.

        title = bsObj.body.h1
    except AttributeError as e: 

# Attribute Error occurs if object under tite variable is not found.

        return None
    return title


title = getTitle("http://www.pythonscraping.com/pages/page1.html")
if title == None:
    print("Title could not be found")
else:
    print(title)