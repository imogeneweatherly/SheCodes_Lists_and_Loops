foods = [
"orange",
"apple",
"banana",
"strawberry",
"grape",
"blueberry",
"carrot", 
"cauliflower", 
"pumpkin",
"passionfruit",
"mango",
"kiwifruit"
]
# QUESTION 1 
print(foods)

# orange
print(foods[0])

#banana
print(foods[2])

#kiwi
print(foods [11])

# Q4
print(foods[0:3])

#Q5
print(foods[9:12])

foods2 = [
"orange",
"apple",
"banana",
"strawberry",
"grape",
"blueberry",
["carrot", "cauliflower", "pumpkin"],
"passionfruit",
"mango",
"kiwifruit"
]

print(foods2 [6][2])

# QUESTION 2 

mailing_list = [
["Roary", "roary@moth.catchers"],
["Remus", "remus@kapers.dog"],
["Prince Thomas of Whitepaw", "hrh.thomas@royalty.wp"],
["Biscuit", "biscuit@whippies.park"],
["Rory", "rory@whippies.park"],
]

for item in mailing_list:
   print(f'{item[0]}:' f'{item[1]}')

# QUESTION 3

names = [] # creates empty list called names
doneEntering = False
while (not doneEntering):
    name = input("Enter a name:")
    name = name.strip()
    if (name == ""):
        doneEntering = True
    else:
        names.append(name)
print(names)