#regular expressions

import re
Nameage = '''
Jance is 22 and Theon is 33
Gabriel is 44 and Joey is 21
'''
ages = re.findall(r'\d{1,3}',Nameage)
names = re.findall(r'[A-Z][a-z]*', Nameage)

ageDict = {}

y = 0

for x in names:
    ageDict[x] = ages[y]
    y += 1

print(ageDict)