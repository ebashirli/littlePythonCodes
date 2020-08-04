from PyPDF2 import PdfFileMerger
# from os import listdir

# grades = ['preschool', 'kindergarten', 'first-grade', 'second-grade', 'third-grade', 'fourth-grade', 'fifth-grade', 'No grade']

# subjects = ['the-arts', 'math', 'ela', 'science', 'social-emotional-learning', 'social-studies', 'No subject']

# location = r"E:\Variation order appendixes A-B-C-D\\"
# pdfs = listdir(location)

pdfs = ["D:\Shared files\Title-Variation order appendixes D.pdf", "D:\Shared files\Title-Variation order appendixes A.pdf","D:\Shared files\Title-Variation order appendixes B.pdf", "D:\Shared files\Title-Variation order appendixes C-Part 1.pdf","D:\Shared files\Title-Variation order appendixes C-Part 2.PDF"]

merger = PdfFileMerger()

for pdf in pdfs:
    merger.append(pdf)

merger.write(r'D:\Shared files\\' + "result.pdf")
merger.close()
