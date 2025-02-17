amount = int(input("Please enter the amount :"))
gst = int(input("Please enter the GST percentage :"))
servicetax = int(input("Please enter the Service tax percentage :"))
gst = (amount*gst)/100
servicetax = (amount*servicetax)/100
total_amount = amount+gst+servicetax
print(total_amount)