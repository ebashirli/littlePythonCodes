import time
import xlrd
import requests                 # servere sorğu gönd?rmek üçün kitabxana
from bs4 import BeautifulSoup   # html s?n?dd?n m?lumat çıxarmaq üçün kitabxana
from webbrowser import get      # ?ld? edilmiş keçidl?ri brauzerd? açmaq üçün kitabxana

def downloader():
    

    wb = xlrd.open_workbook(r"D:\Shared files\Education_com\Lists - English.xlsx")
    wsnames = wb.sheet_names()
    
    ws = wb.sheet_by_name("Stories")
    for i in range(1, 20):
        url = "https://www.education.com/download/stories/" + str(int(ws.cell(i,1).value)) + "/" + ws.cell(i,2).value

        chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
        get(chrome_path).open(url)
        time.sleep(5)
    


'''
    pageNum = 11

    link = "https://www.education.com/workbooks/?page="

    for p in range(1, pageNum + 1):
        res = requests.get(link + str(p))
        wBooks = map(lambda l: l.get('href', None), BeautifulSoup(res.text, 'html.parser').select('.ContentCard-module_link_bi8gq'))
        # print(list(wBooks))
        
        for wb in wBooks:
            res1 = requests.get('https://www.education.com/' + wb)
            h = BeautifulSoup(res1.text, 'html.parser').select('.download-link')[0].get('href', None)
            url = 'https://www.education.com' + h
            print(h)
            chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
            get(chrome_path).open(url)
            time.sleep(3)

'''
downloader()
