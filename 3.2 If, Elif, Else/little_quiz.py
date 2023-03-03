total_correct = 0

print("Welcome to this mini quiz.")

print("Q1) 2 + 2 = 4")
answer_1 = int(input("1) True or 2) False "))

if answer_1 == 1:
    print("That's correct!")
    total_correct += 1
elif answer_1 == 2:
    print("Sorry, you are incorrect.")
else:
    print("That is not an option.")

print("Q2) 10 - 2 = 6")
answer_2 = int(input("1) True or 2) False "))

if answer_2 == 1:
    print("Sorry, you are incorrect.")
elif answer_2 == 2:
    print("That's correct!")
    total_correct += 1
else:
    print("That is not an option.")

print("Q3) 9 * 9 = 81")
answer_3 = int(input("1) True or 2) False "))

if answer_3 == 1:
    print("That's correct!")
    total_correct += 1
elif answer_3 == 2:
    print("Sorry, you are incorrect.")
else:
    print("That is not an option.")

if total_correct == 3:
    print(f"Overall, you got {total_correct} out of 3 correct. Woah, perfect score!")
elif total_correct == 2:
    print(f"Overall, you got {total_correct} out of 3 correct. Nice work!")
elif total_correct == 1:
    print(f"Overall, you got {total_correct} out of 3. Uh... A for effort?")
else:
    print(f"Overall, you got {total_correct} out of 3 correct. Ouch.")
print("Thanks for playing!")
