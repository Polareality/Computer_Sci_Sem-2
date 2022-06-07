sus = int(input("How many items are you buying: "))
total = 0
for i in range(0, sus):
    sus1 = (input("What item are you purchasing? "))
    sus2 = int(input("How much is the item? "))
    print("Thank you for purchasing " + sus1)
    total = total + sus2
print("Your total is: " + str(total))
    
    