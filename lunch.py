weather = input()
temp = int(input())

if weather == "sunny":
    if temp > 25:
        print ("Salad")
    else:
        print ("Sandwich")

elif weather == "cloudy":
    print ("Soup")
