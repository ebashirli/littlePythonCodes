import requests                 # servere sorğu gönd?rmek üçün kitabxana
from bs4 import BeautifulSoup   # html sənəddən məlumat çıxarmaq üçün kitabxana
from webbrowser import get      # əldə edilmiş keçidləri brauzerdə açmaq üçün kitabxana


def downloader():
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
        'social-studies': 'Social studies'
        }

    for i in range(len(list(grades.keys()))):
        for k in range(len(list(subjects.keys()))):
            link = 'https://www.education.com/worksheets/' + list(grades.keys())[i] + '/' + list(subjects.keys())[k] + '/'
        
            pageNum = int(BeautifulSoup(requests.get(link).text, 'html.parser').select('a[title^="Page "]')[-1].getText())      # Filtrlənmiş nəticələrin verildiyi səhifələrin sayı
            for i in range(1, pageNum + 1):
                res = requests.get(link + '?page=' + str(i))
                wSheets = map(lambda l: l.get('href', None), BeautifulSoup(res.text, 'html.parser').select('.ContentCard-module_link_bi8gq'))
                for i in wSheets:
                    res1 = requests.get('https://www.education.com/' + i)
                    k = BeautifulSoup(res1.text, 'html.parser').select('.react-signup.btn.btn-primary')[0].get('href', None)
                    url = 'https://www.education.com/' + k
                    chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
                    get(chrome_path).open(url)

downloader()

