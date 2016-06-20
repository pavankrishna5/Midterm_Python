# Name: Pavan Krishna Ponugoti
# IST 5001 Midterm
# Question : 2

import re

titanic = open('titanic3.csv')
maiden = open('maiden.txt', 'w')
aka = open('aka.txt', 'w')
akamaiden = open('akamaiden.txt', 'w')

for line in titanic:
    match1 = re.findall(r'\((\w.+)\)|\s\(""(.*?\w\)")', line)
    match2 = re.findall(r'\s""(.*?)""', line)
    match3 = re.findall(r'\s\(""(.*?)""\)"', line)
    if len(match1) != 0:
        if 0 < len(match1[0][0]) <= 40:
            maiden.write(match1[0][0] + '\n')
        elif 0 < len(match1[0][1]) <=40:
            maiden.write(match1[0][1] + '\n')
        elif len(match1[0][0]) > 40:
            maiden.write(match1[0][0][0:29] + '\n')
    if len(match2) != 0:
        aka.write(match2[0] + '\n')
    if len(match3) != 0:
        akamaiden.write(match3[0] + '\n')

titanic.close()
maiden.close()
aka.close()
akamaiden.close()

# r'\(([^?!"]*)\)'
# r'\(([^")]*)\)