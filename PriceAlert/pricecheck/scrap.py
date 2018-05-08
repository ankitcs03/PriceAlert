from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq

def Fscrap(finalUrl):
	uClient = uReq(finalUrl)
	page_html = uClient.read()
	uClient.close()

	page_soup =  soup(page_html, "html.parser")
	price = page_soup.find("div", {"class","_1vC4OE"})
	price = price.text[1:]
	
	product_name = page_soup.find("a", {"class","_2cLu-l"})
	if product_name:
		product_name = product_name.get('title')
	else:
		product_name = page_soup.find("div",{"class","_3wU53n"}).text

	return price, product_name

def Ascrap(finalAmazonUrl):
	uClient = uReq(finalAmazonUrl)
	page_html = uClient.read()
	uClient.close()
	page_soup =  soup(page_html, "html.parser")
	containers = page_soup.findAll("span", {"class","s-price"})

	price = containers[0].text
	return price