import xlrd
from PyPDF2 import PdfFileMerger
from os import listdir

wb = xlrd.open_workbook(r"D:\Shared files\Education_com\Lists - English.xlsx")
ws1n = wb.sheet_names()[0]
ws = wb.sheet_by_name(ws1n)

grades_subjects = {}

for i in range(22196, 22876): 
    g_s = str(ws.cell(i,3).value) + '_' + ws.cell(i,4).value

    if g_s not in grades_subjects:
        grades_subjects[g_s] = [ws.cell(i,8).value]
    else:
        grades_subjects[g_s].append(ws.cell(i,8).value)


keys = list(grades_subjects.keys()) # keys of 


for key in keys:
    merger = PdfFileMerger()
    for e in grades_subjects[key]:
        merger.append(e)
    merger.write(r'D:\Shared files\Education_com\GS\\' + key + ".pdf")
    merger.close()
    print(key, 'OK')
'''
