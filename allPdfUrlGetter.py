import requests
from bs4 import BeautifulSoup
from webbrowser import get


link = 'https://www.education.com/science-fair/kindergarten/'
pageNum = int(BeautifulSoup(requests.get(link).text, 'html.parser').select('a[title^="Page "]')[-1].getText())


for p in range(1, pageNum + 1):
   res = requests.get(link + '?page=' + str(p))
   
   wBooks = map(lambda l: l.get('href', None), BeautifulSoup(res.text, 'html.parser').select('.ContentCard-module_link_bi8gq'))
   print(list(wBooks))
##   for wBook in wBooks:
##      
##      d_res = requests.get(link + wBook[13:])
##      url = r'https://www.education.com/download/science-fair/' + wBook[13:] + wBook[13:-1] + '.pdf'
##      
##      # d_link = BeautifulSoup(d_res.text, 'html.parser').select('.download-link')[0].get('href', None)
##      #url = 'https://www.education.com' + d_link
##      #print(url)
##      chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
##      get(chrome_path).open(url)
