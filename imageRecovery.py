import bs4
from bs4 import BeautifulSoup
import base64
import io

bpp1 = open("bpp1.html", "r", encoding="utf-8")
bpp = BeautifulSoup(bpp1, "lxml")
pic = bpp.findAll('img')

#print(pic[0])

i = 0
for image in pic:
	imst = str(image).replace(' ','+').replace('<img+src="data:image/png;base64,','').replace('"/>','')
	dcode = base64.decodebytes(bytes(imst,'utf-8'))
	#print(imst)
	filen = 'bppimg'+str(i)+'.png'
	i = i + 1
	print(filen)
	#print(dcode)
	fh=open(filen,'wb')
	fh.write(dcode)
	fh.close()
