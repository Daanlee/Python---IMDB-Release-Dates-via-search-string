#!/usr/bin/env python

import urllib
import mechanize
from bs4 import BeautifulSoup

searchString = raw_input("Enter search string: ")
#Declare Variables
titles=[]
links = []
results = 0
releaseDate = []
br = mechanize.Browser()
url = 'http://www.imdb.com/find?q='+searchString+'&s=tt&ref_=fn_al_tt_mr'
br.open(url)
response = br.response()
soup = BeautifulSoup(response)
#Get Links
#unable to get href objects though beautifulSoup, concatenate strings
try:
    for link in soup.find_all('td', class_='result_text'):
        if results>=10:
            break
        results+=1
        link = str(link)
        links.append("http://www.imdb.com" + link[link.find("a href=\"")+8:link.find("\">", link.find("a href=\""))])
        titles.append(link[2+link.find("\">", link.find("a href=\"")):link.find("</a>")])
    print "Results found, finding release dates...\n\n"
except:
    print "Error, no results found"
    br.close()
#Get ReleaseDates
for result in links:
    try:
        br.open(result)
    except Exception:
        print ("Unable to open page" + result)
        br.close()
        break
    response = ""
    response = br.response()
    soup = ""
    soup = BeautifulSoup(response)
    info = soup.find('a', title='See more release dates')
    try:
        releaseDate.append(info.get_text())
    except:
        releaseDate.append("no date\n")
for x in xrange(10):
    try:
        print str(titles[x]), str(releaseDate[x])
    except Exception:
        print titles[x], releaseDate[x]
    
