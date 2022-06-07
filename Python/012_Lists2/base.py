andrewgrigor = int(input("How many random numbers would you like? "))
thislist = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
import random
for x in range(andrewgrigor):
    y = (random.randrange(0,10))
    print("Your random numbers are: " + thislist[y])