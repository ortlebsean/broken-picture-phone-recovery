import bs4
from bs4 import BeautifulSoup
import base64
import io


def bookHandle(book):
	bookName = book.find("h2").text.split("'")[0]
	pages = book.findAll("section")
	pageHandle(bookName,pages)

def pageHandle(bookName,pages):
	for page in pages:
		subInfo = page.find("h3").text.replace(",","").replace(":","").replace(" ","-")
		fileName="BPP-"+bookName+"-"+subInfo+".png"
		image=page.find("img")
		imst = str(image).replace(' ','+').replace('<img+src="data:image/png;base64,','').replace('"/>','')
		dcode = base64.decodebytes(bytes(imst,'utf-8'))
		fh=open(fileName,'wb')
		fh.write(dcode)
		fh.close()



bpp1 = open("bpp1.html", "r", encoding="utf-8")
bpp = BeautifulSoup(bpp1, "lxml")
books = bpp.findAll("article")
for book in books:
	bookHandle(book)

