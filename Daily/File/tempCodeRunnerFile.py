file=open('Stroke1.csv', 'r')
i=0
bmi = []
for line in file:
    i=i+1
    if i < 10:
        line = line.strip()
        
        print(line)
        line = line.split(',')
        # print(line)
        if i > 1:
            bmi.append(float(line[9]))
print(bmi)
print(sum(bmi)/len(bmi))