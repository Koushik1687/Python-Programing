import csv
file=open('D:\\Coding\\Python\\Python-Programing\\Daily\\File\\Stroke.csv', 'r')
i=0
fi=open('D:\\Coding\\Python\\Python-Programing\\Daily\\File\\St.csv', 'a')
bmi = []
for line in file:
    i=i+1
    if i < 5:
        line = line.strip()
        print(line)
        line = line.split(',')
        # print(line)
        if i > 1:
            bmi.append(float(line[9]))
print(bmi)
print(sum(bmi)/len(bmi))