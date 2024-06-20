from tabulate import tabulate

rent = float(input("Rent per month: £"))
gas = float(input("Gas payment per month: £"))
electricity = float(input("Electricity payment per month: £"))
water = float(input("Water payment per month: £"))
council_tax = float(input("Council Tax per month: £"))

total = float(rent) + float(gas) + float(electricity) + float(water) + float(council_tax)
y = "{:.2f}".format(total)
print("TOTAL: £" + str(float(y)))

# create data
data = [["Rent", "£" + str(rent)],
        ["Gas", "£" + str(gas)],
        ["Electricity", "£" + str(electricity)],
        ["Water", "£" + str(water)],
        ["Council Tax", "£" + str(council_tax)]
        ]

# define header names
col_names = ["Categories", "Payments"]

# display table
print("Your monthly expenses are:")
print(tabulate(data, headers=col_names))

data2 = [["Total:", "£" + str(float(y))]]
print(tabulate(data2))
