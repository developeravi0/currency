with open('currency.txt') as f:
    lines=f.readlines()
currencydict={}
for line in lines:
    parsed=line.split("\t")
    currencydict[parsed[0]] = parsed[1]
amount=int(input("Enter the amount : "))
print("Here are the options you can convert INR to - ")
[print (item) for item in currencydict.keys()]
currency=str(input("Please enter one of these values to convert to."))
f_currency=amount*float(currencydict[currency])
print(f"{amount} INR is equal to {f_currency} {currency}")