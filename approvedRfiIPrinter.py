import os

# file names
rfiNos = []

# file name extenction
fileExt = ".pdf"

path = "D:\\Ortak\\3. Ortak Geçici Paylaşım Dosyaları\\IPC 11\\SW+OK\\"

for i in range(len(rfiNos)):
    try:
        os.startfile(path + rfiNos[i] + fileExt, "print")
    except:
        print(rfiNos[i])
        continue
