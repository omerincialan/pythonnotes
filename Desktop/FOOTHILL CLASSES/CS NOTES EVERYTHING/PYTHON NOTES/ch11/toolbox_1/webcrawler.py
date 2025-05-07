##
#  This program browses the Web to collect the addresses of all web pages that 
#  can be reached by following the hyperlinks within 3 steps from an initial 
#  page. 
#

import bs4
import urllib.request

def main() :
    url = input("Start with URL: ")
    visited = []
    crawl(url, 3, visited)
    print(visited)

def crawl(address, depth, visited) :
    if depth == 0 :
       return
    try :
       response = urllib.request.urlopen(address)
       doc = bs4.BeautifulSoup(response)
       print("Visiting " + address)
       for link in doc.find_all("a") :
          href = link["href"]
          if href[0:4] == "http" and href not in visited :
             visited.append(href)
             crawl(href, depth - 1, visited)
    except :
       return

main()

