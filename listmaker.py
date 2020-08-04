import requests
from bs4 import BeautifulSoup
from webbrowser import get

def downloader():
    grades = ['preschool', 'kindergarten', 'first-grade', 'second-grade', 'third-grade', 'fourth-grade', 'fifth-grade']
    subjects = ['the-arts', 'foreign-language', 'math', 'ela', 'science', 'social-emotional-learning', 'social-studies', 'typing'] # 
    
    names = []
    
    for i in grades:
        for k in subjects:        
            link = 'https://www.education.com/lesson-plans/' + i + '/' + k + '/'
            try:
                pageNum = int(BeautifulSoup(requests.get(link).text, 'html.parser').select('a[title^="Page "]')[-1].getText())
            except:
                continue
            
            print(link, (pageNum - 1) * 25 + len(BeautifulSoup(requests.get(link + '?page=' + str(pageNum)).text, 'html.parser').select('.ContentCard-module_link_bi8gq')))
            
            for p in range(1, pageNum + 1):
                res = requests.get(link + '?page=' + str(p))
                
                wSheets = map(lambda l: l.get('href', None), BeautifulSoup(res.text, 'html.parser').select('.ContentCard-module_link_bi8gq'))
                
                for w in wSheets:
                    # res1 = requests.get('https://www.education.com/' + w)
                    # h = BeautifulSoup(res1.text, 'html.parser').select('.react-signup.btn.btn-primary')[0].get('href', None)
                    print(w)
    
downloader()
