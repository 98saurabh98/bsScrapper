#import required libraries
import urllib.request, urllib.parse, urllib.error
import re 								  #Import Regular Expressions
from bs4 import BeautifulSoup			  #Importing BeautifulSoup in Python 3
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
url = input()
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'lxml')        #tree builder - 'lxml'

#tags to find
taggs = input("Enter a tag to scrape: ")  #tag to be scraped

tags = soup(taggs)						  
lst= list()
count = 0
for tag in tags:
	count = count + 1					  #counter to find number of iterations
#	print('TAG: ', tag)
#	print('URL:', tag.get('href', None))
#	print('Contents:', tag.contents[0])
#	print('Attrs:', tag.attrs)
	for line in tag.contents:
		val = re.findall('[0-9]+', line)  #finding integers in a string using Regular Expressions
		for value in val:
#			print(value)
			lst.append(int(value))
print(sum(lst))                           #sum of numbers
print(count)                              #number of iterations