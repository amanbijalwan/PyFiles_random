
pets = ["Tom", "Jerry", "Donald", "Mickey", "Pluto"]

for i in pets:
    if i == "Donald":
        print(i.upper())
    else:
        print(i)
        
#check values in list

if "Tom" in pets:
    print(f"{pets[0]} is here")
if "Car" not in pets:
    print("No cars here")