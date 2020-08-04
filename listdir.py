import os

firstLevel = ['1st grade', '2nd grade', '3rd grade', '4th grade', '5th grade', 'Kindergarten', 'Preschool']

for dir in firstLevel:
        ls = os.listdir(r'C:\Users\Ilkin\Music\Nivle\Education_com' + '\\' + dir)
        for l in ls:
            ts = os.listdir(r'C:\Users\Ilkin\Music\Nivle\Education_com' + '\\' + dir + '\\' + l)
            print(dir, l)
            for t in ts:
                print(t)
            
        
        
