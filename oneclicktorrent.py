import urllib.request
import webbrowser
from urllib.request import urlopen as uopen
from bs4 import BeautifulSoup as soup

url = 'https://pirateproxy.ist/search/'
word = input("Enter a torrent to search: ").strip()
word.replace(" ","%20")
url = url+word

req = urllib.request.Request(
    url, 
    data=None, 
    headers={
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
    }
)

uClient = uopen(req)

page_html = uClient.read()
uClient.close()

page_soup = soup(page_html,"html.parser")


container_link = page_soup.findAll("a",{"title":"Download this torrent using magnet"})[0:3]

container_name = page_soup.findAll("a",{"class":"detLink"})[0:3]

container_category = page_soup.findAll("a",{"title":"More from this category"})[0:6]


if len(container_link) < 1:
    print("Error")
else:
    link = []
    name = []
    category = []
    j = 1
    for i in range(len(container_link)):
        
        name.append(container_name[i].text)
        link.append(container_link[i]["href"])
        category.append(container_category[j].text)
        j=j+2

    for i in range(len(container_link)):
        print((i+1),"---",name[i],"---",category[i])

    print("4 --- Click here to view more torrents")
        
    no = int(input("Enter a number to download: "))
    no = no - 1
    if no > 3 or no < 0:
        print("Number is invalid :(")
    elif no == 3:
        webbrowser.open(url)
    else:
        webbrowser.open(link[no-1])


