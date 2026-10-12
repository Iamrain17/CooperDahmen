windspeed = int(input ("What's the windspeed?\n> "))
if windspeed < 74:
    print("Tropical Storm")
elif windspeed < 96:
    print("Category 1")
elif windspeed < 111:
    print("Category 2")
elif windspeed < 130:
    print("Category 3")
elif windspeed < 157:
    print("Category 4")
elif windspeed >= 157:
    print("Category 5")