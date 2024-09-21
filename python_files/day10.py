bill = float(input("how much was the bill?"))
pax = int(input("How many people in your party?"))
tip_share = int(input("How much tip (%)?"))

tip_value = bill * tip_share / 100
total = bill + tip_value
share = (total / pax)
venmo = round(share, 2)

print("For your party of", pax, "people,")
print("the bill", bill, "with the tip of", tip_share, "%,")
print("each person must pay", venmo, ".")