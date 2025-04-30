lt = []
date = ["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]
for i in range(7):
    num = int(input(f"Enter the temperature of {date[i]} :"))
    lt.append(num)
print("The average temperature of the week is ",sum(lt)/len(lt))