value = int(input("Please enter line length: "))
value1 = input("Do you want a horizontal or vertical line: ")
if(value1 == "horizontal"):
    for y in range(0, value):
        print("*", end=" ")
if(value1 == "vertical"):
    for x in range(0, value):
        print("*")