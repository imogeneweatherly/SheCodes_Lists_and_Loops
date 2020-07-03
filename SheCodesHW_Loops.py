

# # QUESTION 1

# # Store input numbers
# num1 = input('Enter first number: ')
# num2 = input('Enter second number: ')
# num3 = input('Enter third number: ')
# num4 = input('Enter fourth number: ')

# # Add two numbers
# sum = float(num1) + float(num2) + float(num3) + float(num4)

# # Display the sum
# print(sum)

# QUESTION 2 

# mailing_list = [
# ["Roary", "roary@moth.catchers"],
# ["Remus", "remus@kapers.dog"],
# ["Prince Thomas of Whitepaw", "hrh.thomas@royalty.wp"],
# ["Biscuit", "biscuit@whippies.park"],
# ["Rory", "rory@whippies.park"],
# ]

# for item in mailing_list:
#    print(f'{item[0]}:' f'{item[1]}')


# QUESTION 3

# names = [] # creates empty list called names
# doneEntering = False
# while (not doneEntering):
#     name = input("Enter a name:")
#     name = name.strip()
#     if (name == ""):
#         doneEntering = True
#     else:
#         names.append(name)
# print(names)

# QUESTION 4
groceries = [
["Baby Spinach", 2.78],
["Hot Chocolate", 3.70],
["Crackers", 2.10],
["Bacon", 9.00],
["Carrots", 0.56],
["Oranges", 3.08]
]
total = 0 

for item in groceries:
    quantity = input (f'How many {item[0]} did you take?')
    item[1] = item[1]*int(quantity)
    total = item[1]

print("====Izzy's Food Emporium====")
for index,item in enumerate(groceries):
    print(f"{item[0]:<20} ${item[1]:.2f}")
print("============================")
print(f"{total:>27}")

