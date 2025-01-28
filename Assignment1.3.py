ammount = int(input("Please enter the ammount :"))
gst = int(input("Please enter the GST percentage :"))
servicetax = int(input("Please enter the Service tax percentage :"))
gst = (ammount*gst)/100
servicetax = (ammount*servicetax)/100
total_ammount = ammount+gst+servicetax
print(total_ammount)