# Name: Pavan Krishna Ponugoti
# IST 5001 Midterm
# Question : 4

titanic = open('titanic3.csv')
classage = open('classify_age.csv', 'w')

for line in titanic:
    line = line.rstrip('\n')
    lane = line.split(',')
    try:
        if lane[5] == "":
            lane[5] = 'Unknown'
        elif 0 <= float(lane[5]) <= 12:
            lane[5] = 'Child'
        elif 12 <= float(lane[5]) <= 19:
            lane[5] = 'Teenager'
        elif 20 <= float(lane[5]) <= 56:
            lane[5] = 'Adult'
        elif float(lane[5]) >=56:
            lane[5] = 'Senior'
        lune = ','.join(lane + '\n')
        classage.write(lune)
    except:
        a = ','.join(lane)
        classage.write(a + '\n')
titanic.close()
classage.close()