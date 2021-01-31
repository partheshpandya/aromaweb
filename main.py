import requests
from bs4 import BeautifulSoup
url = "https://codewithharry.com"
r = requests.get(url)
htmlContent = r.content
#print(htmlContent)
#stp2:parse the html
soup = BeautifulSoup(htmlContent,'html.parser')
#print(soup)
#stp3: HTMl tree traversal
#

#comonly used types of objects:
#1] tag
#2] NavigableString
#3] BeautifulSoup]
#4] comment
#title = soup.title
#print(type(title))    #1] tag
#print(type(soup))    #2] NavigableString
#print(type(title.string))  #3] BeautifulSoup]
markup="<p><!--this is comment--></p>"
soup2=BeautifulSoup(markup)
#print(type(soup2.p.string))

# Get the title of html page
title = soup.title
#get the  all paragraphs from the page
paras = soup.find_all('p')
#print(paras)
#get the  all anchors tags from the page
anchors = soup.find_all('a')
#print(anchors)

#print(soup.find('p')) #get first element in the html page
#print(soup.find('p')['class']) # get the class of any element

#find all the elements with class lead
#print(soup.find_all('p',class_='lead'))
#gat the text from the tegs/soup
#print(soup.get_text())

#get the  all anchors tags from the page
anchors = soup.find_all('a')
all_links=set()


#get all the links on a page
for link in anchors:
    if(link.get("href")!= '#'):

     linkText ="https://codewithharry.com" +link.get('href')
     all_links.add(link)
     #print(linkText)
navbarSupportedContent= soup.find(id="navbarSupportedContent")   

#.contents = A tag's children are available as a list          #take more memory
#.children = A tag's children are available as a genrator      #fast and less memory 
     # for smaller size of pages both r worsk as a same but for larger size of pages it depends on which one you choose....
for elem in navbarSupportedContent.contents:
    print(elem)
