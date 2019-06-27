from bs4 import BeautifulSoup
import requests
url='https://en.wikipedia.org/wiki/Machine_learning'
req=requests.get(url)
req
