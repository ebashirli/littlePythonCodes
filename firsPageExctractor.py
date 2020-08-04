import os
from PyPDF2 import PdfFileReader, PdfFileWriter

path = 'D:\\giris\\ot\\'

for fileName in os.listdir(path):
    pdf_reader = PdfFileReader(path + fileName)
    pdf_writer = PdfFileWriter()
    pdf_writer.addPage(pdf_reader.getPage(0))
    output_filename = 'D:\\giris\\op\\' + fileName
    with open(output_filename, 'wb') as out:
            pdf_writer.write(out)
