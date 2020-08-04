import pyodbc
import datetime
import os
import shutil
import xlsxwriter

def wrter(ri):
    for row in cur.fetchall():
        worksheet.write(ri, 0, row[0].strip())
        worksheet.write(ri, 1, row[3])
        worksheet.write(ri, 2, row[4].time())
        worksheet.write(ri, 3, row[5])
        worksheet.write(ri, 4, row[9].strip())
        worksheet.write(ri, 5, row[12].strip())
        worksheet.write(ri, 6, row[13].strip())
        worksheet.write(ri, 7, row[14].strip())
        worksheet.write(ri, 8, row[5] > 100000 and 'K1' or 'K2')
        worksheet.write(ri, 9, abs(int(row[19])-int(row[18])))
        worksheet.write(ri, 10, row[7].strip())
        ri+=1
    return ri

def mover():
    try:
        path0 = 'D:\\'
        folders0 = os.listdir(path0)
        for i in range(len(folders0)):
           shutil.move(path0 + folders0[i], r'E:\Transportation data\Daily\From Scale')
        return len(folders0)
    except:
        op = int(input('No flash disk. Would you like insert the flash disk (1) or continue on PC storage (2)?'))
        if op == 1:
            input('Insert flash disc and press Enter')
            mover()
        elif op == 2:
            return int(input("Number of scales: "))

folder_num = mover()        

trMonths = ['OCA', 'SUB', 'MAR', 'NIS', 'MAY', 'HAZ', 'TEM', 'AUG', 'EYL', 'EKI', 'KAS', 'ARA']

if datetime.datetime.now().month == 1 and datetime.datetime.now().day == 1:
    year = str(datetime.datetime.now().year - 1)[2:]
else:
    year = str(datetime.datetime.now().year)[2:]


if datetime.datetime.now().day == 1:
    month = datetime.datetime.now().month - 1
else:
    month = datetime.datetime.now().month

path = r'E:\Transportation data\Daily\From Scale'
folders = list(filter(lambda x: x[:2]==year, os.listdir(path)))  # until the year 2100 :)

workbook = xlsxwriter.Workbook(r"E:\Transportation data\Daily" + '\\' + ('' if month > 9 else '0') + str(month) + ".20" + str(year) + "\K1ve2p.xlsx") # 
worksheet = workbook.add_worksheet("Cikkay")

headings = ['plaka', 'cıktar', 'cıksaa', 'tartımno', 'malad', 'alan1', 'alan2', 'alan3', 'kantar', 'NET', 'firmaad']
for c in range(len(headings)):
    worksheet.write(0, c, headings[c])

for i in range(1,3):
    MDB = path + '\\' + folders[-i] + '\CIK' + trMonths[month-1] + year + '.mdb'
    
    DRV = 'ODBC Driver 13 for SQL Server' #{Microsoft Access Driver(*.mdb)}'
    PWD = 'pw'

    con = pyodbc.connect('DRIVER={};DBQ={};PWD={}'.format(DRV,MDB,PWD))
    cur = con.cursor()

    cur.execute('select * from cikkay')
    if i == 1:
        row_index = 1
        
    row_index = wrter(row_index)

    if folder_num != 2:
        break

cur.close()
con.close()
workbook.close()

os.system(r"start EXCEL.EXE Book1.xlsm")
