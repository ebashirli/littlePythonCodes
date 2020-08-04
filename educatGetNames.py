import requests
from bs4 import BeautifulSoup

grades = ['kindergarten', 'first-grade', 'second-grade', 'third-grade', 'fourth-grade', 'fifth-grade'] # 'preschool', 

subjects = ['science', 'social-studies', 'foreign-language'] # ['the-arts', 'math', 'ela', 'science', 'social-emotional-learning', 'social-studies']

for grade in grades:
   for subject in subjects:
      link = 'https://www.education.com/science-fair/' + grade + '/' + subject + '/'
      try:
         pageNum = int(BeautifulSoup(requests.get(link).text, 'html.parser').select('a[title^="Page "]')[-1].getText())
         for p in range(1, pageNum + 1):
            res = requests.get(link + '?page=' + str(p))
            wBooks = map(lambda l: l.get('href', None), BeautifulSoup(res.text, 'html.parser').select('.ContentCard-module_link_bi8gq'))
            for wBook in wBooks:
               
               print(grade, subject, p, wBook)
      except:
         continue
