# Name: Pavan Krishna Ponugoti
# IST 5001 Midterm
# Question : 1

import re

titanic = open('titanic3.csv')
single = open('single.csv', 'w')
married = open('married.csv', 'w')
unknown = open('unknown.csv', 'w')

for line in titanic:
    lane = line.split(',')
    match1 = re.search('Miss.|Master.', line)
    match2 = re.search('Mrs.|Mme.|Sir$|Lady', line)
    match3 = re.search('Mr.|Sir.|Count.', line)
    if match1:
        single.write(line)
    elif match2:
        married.write(line)
    elif match3 and int(lane[6])>=1:
        married.write(line)
    elif match3 and int(lane[6])==0:
        unknown.write(line)
    else:
        unknown.write(line)

titanic.close()
single.close()
married.close()
unknown.close()