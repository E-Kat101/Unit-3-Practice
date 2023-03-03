weight = int(input("What is your current earth weight? "))
print("Here are the options for which planet to visit:")
print("1. Venus")
print("2. Mars")
print("3. Jupiter")
print("4. Saturn")
print("5. Uranus")
print("6. Neptune")

planet = int(input("Which planet would you like to visit? "))

if planet == 1:
    new_weight = weight * 0.78
    print(f"Your weight would be {new_weight} pounds on Venus.")
elif planet == 2:
    new_weight = weight * 0.39
    print(f"Your weight would be {new_weight} pounds on Mars.")
elif planet == 3:
    new_weight = weight * 2.65
    print(f"Your weight would be {new_weight} pounds on Jupiter.")
elif planet == 4:
    new_weight = weight * 1.17
    print(f"Your weight would be {new_weight} pounds on Saturn.")
elif planet == 5:
    new_weight = weight * 1.05
    print(f"Your weight would be {new_weight} pounds on Uranus.")
elif planet == 6:
    new_weight = weight * 1.23
    print(f"Your weight would be {new_weight} pounds on Neptune.")
else:
    print("Please input a planet based on a number between 1 and 6.")
