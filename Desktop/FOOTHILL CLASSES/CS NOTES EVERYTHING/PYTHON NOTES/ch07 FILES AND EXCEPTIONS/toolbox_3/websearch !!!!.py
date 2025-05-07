##
# This program illustrates the use of the urllib module to perform a simple
# search on a single web page.
#
import urllib.request

def main() :
  # Read the URL and search targets.
  address = input("Enter a web page URL: ")
  response = urllib.request.urlopen(address)
  text = response.read().decode()

  i = text.find("href")
  while i != -1 :
     start = text.find("\"", i)
     end = text.find("\"", start + 1)
     print(text[start + 1 : end])
     i = text.find("href", end + 1)

  response.close()    

main()  

