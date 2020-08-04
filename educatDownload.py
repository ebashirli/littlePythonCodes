import requests                 # servere sorğu gönd?rmek üçün kitabxana
from bs4 import BeautifulSoup   # html s?n?dd?n m?lumat çıxarmaq üçün kitabxana
from webbrowser import get      # ?ld? edilmiş keçidl?ri brauzerd? açmaq üçün kitabxana


def downloader():
    '''
    grades = {
        'preschool': 'Preschool',
        'kindergarten': 'Kindergarten',
        'first-grade': '1st grade',
        'second-grade': '2nd grade',
        'third-grade': '3rd grade',
        'fourth-grade': '4th grade',
        'fifth-grade': '5th grade'
        }
    
    subjects = {
        'the-arts': 'Fine art',
        'foreign-language': 'Foreign language',
        'math': 'Math',
        'ela': 'Reading & Writing',
        'science': 'Science',
        'social-emotional-learning': 'Social emotional',
        'social-studies': 'Social studies',
        'typing': 'Typing'
        }
    '''

    grades = ['fourth-grade']# 'first-grade', 'second-grade', 'third-grade', 'fourth-grade', 'fifth-grade']
    
    subjects = ['ela']
    
    for i in grades:
        for k in subjects:
            
            link = 'https://www.education.com/worksheets/' + i + '/' + k + '/'

            pageNum = int(BeautifulSoup(requests.get(link).text, 'html.parser').select('a[title^="Page "]')[-1].getText())      # Filtrl?nmiş n?tic?l?rin verildiyi s?hif?l?rin sayı

            print(link, (pageNum - 1) * 25 + len(BeautifulSoup(requests.get(link + '?page=' + str(pageNum)).text, 'html.parser').select('.ContentCard-module_link_bi8gq')))
            
            for p in range(1, pageNum + 1):
                res = requests.get(link + '?page=' + str(p))
                wSheets = map(lambda l: l.get('href', None), BeautifulSoup(res.text, 'html.parser').select('.ContentCard-module_link_bi8gq'))
                for w in wSheets:
                    res1 = requests.get('https://www.education.com/' + w)
                    h = BeautifulSoup(res1.text, 'html.parser').select('.react-signup.btn.btn-primary')[0].get('href', None)
                    url = 'https://www.education.com' + h
                    chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
                    get(chrome_path).open(url)

downloader()
