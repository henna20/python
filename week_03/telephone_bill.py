i = int(input("Enter number of minutes: "))
print("Number of minutes used:", i)
call_charges = i * 0.15
vat = (call_charges/100) * 20
total = vat + call_charges
print("Basic call charge:", + float(call_charges))
print("VAT due:", +float(vat))
print("Total:", +float(total))
