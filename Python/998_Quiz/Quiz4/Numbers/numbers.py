mynumbers = [6,9,32,28,15,22,3,18]
x = (mynumbers[0]+mynumbers[1]+mynumbers[2]+mynumbers[3]+mynumbers[4]+mynumbers[5]+mynumbers[6]+mynumbers[7])/8
x = str(x)
print("The average of the 8 numbers is: " + x)
nm = 1000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
m = 0
for i in range(0, 7):
    if nm > mynumbers[i]:
        nm = mynumbers[i]
nm = str(nm)
print("The min is: " + nm)    
for z in range(0, 7):
    if m<mynumbers[z]:
        m=mynumbers[z]
m = str(m)
print("The max is: " + m)