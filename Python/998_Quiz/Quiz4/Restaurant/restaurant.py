import random
mc = ["Burger, ", "Fries, ", "Milkshake"]
stop = ["Hot wings, ", "Fries, ", "Soda"]
way = ["Sandwich, ", "Sandwich2, ", "Soda and chips "]
sus = input("Pick one of the restaurants: Type x for Mcdonalds, Type f for Wingstop, Type u for Subway: ")
if sus == "x":
    print("Mcdonalds menu: " + mc[0] + mc[1] + mc[2])
    x = random.randrange(2)
    print("Suggested Menu item: " +mc[x])
elif sus == "f":
    print("Wingstop menu: " + stop[0] + stop[1] + stop[2])
    x = random.randrange(2)
    print("Suggested Menu item: " + stop[x])
elif sus == "u":
    print("Subway menu: " + way[0] + way[1] + way[2])
    x = random.randrange(2)
    print("Suggested Menu item: " + way[x])
else: 
    print("Pick one of the restaurants: Type x for Mcdonalds, Type f for Wingstop, Type u for Subway: ")

