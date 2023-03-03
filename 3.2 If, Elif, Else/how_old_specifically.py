name = input("Hey, what's your name? ")
age = int(input(f"Okay, {name}, what's your age? "))

if age < 16:
    print(f"You can't drive, vote, or rent a car, {name}.")
elif age == 16 or age == 17:
    print(f"You can drive but not vote or rent a car, {name}.")
elif age == 18 or age == 19 or age == 20:
    print(f"You can vote but not rent a car, {name}.")
else:
    print(f"You can do pretty much anything, {name}.")
