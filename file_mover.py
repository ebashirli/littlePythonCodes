import os
import shutil
import xlrd


wb = xlrd.open_workbook(r"D:\Shared files\Education_com\Lists - English.xlsx")
wsnames = wb.sheet_names()
ws = wb.sheet_by_name("Missings")
for i in range(1, 56):
   fn = ws.cell(i,5).value
   
   
   source = r"D:\Shared files\Education_com\Answers\\" + fn

   destination = r"D:\Shared files\Education_com\Answers\New folder\\" + fn

   shutil.move(source, destination)
