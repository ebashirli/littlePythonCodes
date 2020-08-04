from PyPDF2 import PdfFileReader
from os import listdir, remove
location = r"E:\Variation order appendixes A-B-C-D\\"
pdfs = listdir(location)
print(len(pdfs))
counter = 0
for pdf in pdfs:
    try:
        reader = PdfFileReader(open(location + pdf, 'rb'))
        counter += reader.getNumPages()
    except:
        print(pdf)
        
        
        

print(counter)

'''

from PyPDF2 import PdfFileMerger

from os import listdir
pdfs = listdir(r"D:\Music from Vk\E\All")[135]

merger = PdfFileMerger()

for pdf in pdfs:
    merger.append(r"D:\Music from Vk\E\All\\" + pdf)

merger.write(r"D:\Music from Vk\E\result.pdf")
merger.close()
'''
