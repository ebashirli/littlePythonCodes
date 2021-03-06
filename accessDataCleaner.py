import pyodbc
import xlsxwriter
import datetime
from os import listdir as ld
import os
import shutil

path0 = 'E:\\' #Path to USB

# folders0 = ld(path0) 
# for i in range(len(folders0)):
#     shutil.move(path0 + folders0[i], r'D:\Dosyalar\KANTAR BILGILERI\SANTIYE KANTARI')

trMonths = ['OCA', 'SUB', 'MAR', 'NIS', 'MAY', 'HAZ', 'TEM', 'AUG', 'EYL', 'EKI', 'KAS', 'ARA']


if datetime.datetime.now().month == 1 and datetime.datetime.now().day == 1:
    year = str(datetime.datetime.now().year - 1)[2:]
else:
    year = str(datetime.datetime.now().year)[2:]


if datetime.datetime.now().day == 1:
    month = datetime.datetime.now().month - 1
else:
    month = datetime.datetime.now().month

path = 'D:\Dosyalar\KANTAR BILGILERI\SANTIYE KANTARI\\'

folders = ld(path)


conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=' + path + folders[-1] + '\CIK' + trMonths[month-1] + year + '.mdb;')
cursor = conn.cursor()
cursor.execute('select * from cikkay')

workbook = xlsxwriter.Workbook(r"C:\Users\TexnikOfis\Documents\K1ve2py.xlsx") 
worksheet = workbook.add_worksheet("Cikkay")

headings = ['plaka', 'cıktar', 'cıksaa', 'tartımno', 'firmaad', 'malad', 'alan1', 'alan2', 'alan3', 'kantar', 'NET']
for c in range(len(headings)):
    worksheet.write(0, c, headings[c])

ri = 1
for row in cursor.fetchall():
    worksheet.write(ri, 0, row[0].strip())
    worksheet.write(ri, 1, row[3])
    worksheet.write(ri, 2, row[4].time())
    worksheet.write(ri, 3, row[5])
    worksheet.write(ri, 4, row[7].strip())
    worksheet.write(ri, 5, row[9].strip())
    worksheet.write(ri, 6, row[12].strip())
    worksheet.write(ri, 7, row[13].strip())
    worksheet.write(ri, 8, row[14].strip())
    worksheet.write(ri, 9, "K1")
    worksheet.write(ri, 10, abs(int(row[19])-int(row[18])))
    ri+=1

conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=' + path + folders[-2] + '\CIK' + trMonths[month-1] + year + '.mdb;')
cursor = conn.cursor()
cursor.execute('select * from cikkay')

for row in cursor.fetchall():
    worksheet.write(ri, 0, row[0].strip())
    worksheet.write(ri, 1, row[3])
    worksheet.write(ri, 2, row[4].time())
    worksheet.write(ri, 3, row[5])
    worksheet.write(ri, 4, row[7].strip())
    worksheet.write(ri, 5, row[9].strip())
    worksheet.write(ri, 6, row[12].strip())
    worksheet.write(ri, 7, row[13].strip())
    worksheet.write(ri, 8, row[14].strip())
    worksheet.write(ri, 9, "K2")
    worksheet.write(ri, 10, abs(int(row[19])-int(row[18])))
    ri+=1

workbook.close()
os.system(r"start EXCEL.EXE C:\Users\TexnikOfis\Documents\Book1.xlsm") # starts VBA code 


'''

Private Sub Workbook_Open()

Dim k1 As Workbook
Set k1 = Workbooks.Open(Filename:="C:\Users\TexnikOfis\Documents\K1ve2py.xlsx")

With k1.Worksheets("Cikkay")
    .Range("C:C").NumberFormat = "hh:mm"
    .Range("B:B").NumberFormat = "dd.mm.yyyy"
    .Range("A:K").AutoFilter
    .Columns("A:K").AutoFit
    .Range("A2").Select
    ActiveWindow.FreezePanes = True
    .Cells(Rows.Count, 1).End(xlUp).Offset(1, 0).Select
    k1.Save
End With
Application.Wait (Now + TimeValue("00:00:03"))
ThisWorkbook.Close

End Sub


'''
