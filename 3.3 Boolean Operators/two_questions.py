print("TWO QUESTIONS!")
print("Think of an object and I'll try to guess it.")

answer_1 = input("Question 1) Is it animal, vegetable, or mineral? ")

answer_2 = input("Question 2) Is it bigger than a breadbox? ")

if answer_1 == "animal":
    if answer_2 == "yes":
        print("My guess is that you are thinking of a moose.")
    elif answer_2 == "no":
        print("My guess is that you are thinking of a squirrel.")
    else:
        print("Whoops. Looks like your input is invalid.")

if answer_1 == "vegetable":
    if answer_2 == "yes":
        print("My guess is that you are thinking of a watermelon.")
    elif answer_2 == "no":
        print("My guess is that you are thinking of a carrot.")
    else:
        print("Whoops. Looks like your input is invalid.")

if answer_1 == "mineral":
    if answer_2 == "yes":
        print("My guess is that you are thinking of a Camaro.")
    elif answer_2 == "no":
        print("My guess is that you are thinking of a paper clip.")
    else:
        print("Whoops. Looks like your input is invalid.")
