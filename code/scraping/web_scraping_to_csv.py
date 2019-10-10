import requests
import csv
from bs4 import BeautifulSoup
url = "https://www.myhome.ie/residential/mayo/property-for-sale?page=1"
# load the page from the above url in the object page.
page = requests.get(url)
#parse only the html from page.content
soup = BeautifulSoup(page.content, 'html.parser')
#open a file and csv writer objects
home_file = open('week03MyHome.csv', mode='w', newline='\n', encoding='UTF-8')
home_writer = csv.writer(home_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
#parse the listings from soup using the class label
listings = soup.findAll("div", class_="PropertyListingCard" )
#loop trhough the listings
for listing in listings:
    #create an empty list for writing out to csv
    entryList = []
    #parse and append price to listing
    price = listing.find(class_="PropertyListingCard__Price").text.strip()
    entryList.append(price)
    #parse and append address to listing
    address = listing.find(class_="PropertyListingCard__Address").text.strip()
    entryList.append(address)
    #write parsed data to the csv file
    home_writer.writerow(entryList)
#close the file
home_file.close()