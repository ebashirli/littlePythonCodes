import os

rfiNos = []

path = "D:\\Ortak\\3. Ortak Geçici Paylaşım Dosyaları\\IPC 13\\EW+OK\\"

for i in range(len(rfiNos)):
    try:
        os.startfile(path + rfiNos[i] + '.pdf', "print")
    except:
        print(rfiNos[i])
        continue
