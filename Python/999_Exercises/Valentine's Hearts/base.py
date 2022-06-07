people_list = ["You're mom,", "Gabe", "Andrew GRIGOR", "Jacob Poole", "DR PASTANJI", "GREG JAVADIAN", "My sister"]
comp_list = [" is amazing!", " is SUS!", " is a gorilla!", " is wondefully basic!", " likes sand!", " smells like dog piss"]
import random
num_people = random.randrange(0, len(people_list))
num_comp = random.randrange(0, len(comp_list))
print(people_list[num_people] + comp_list[num_comp])