# Name: Pavan Krishna Ponugoti
# IST 5001 Midterm
# Question : 3

group = open('group_by_boat.csv','w')
dict = {}

with open('titanic3.csv') as titanic:
    next(titanic)
    for line in titanic:
        line = line.rstrip('\n')
        line = line.split(',')
        name = line[3].rstrip('"') + ' '+ line[2].lstrip('"')
        if line[12].isnumeric():
            line[12] = line[12].zfill(2)
        if line[12] == '5 7' or line[12] == '5 9':
            luck = line[12].split()
            luck = line[12][0].zfill(2)
            line[12] = luck
        if line[12] == '8 10':
            stri = line[12].split()
            stri = line[12][0].zfill(2)
            line[12] = stri
        list = []
        if line[12] != '':
            list.append(name)
            list.append(line[12])
            dict[list[0]] = list[1]

for x in sorted(dict.items(), key = lambda x:x[1]):
    group.write(x[0] + ', ' + x[1] + '\n')

titanic.close()
group.close()