print("TWO QUESTIONS!")
print("Think of an object and I'll try to guess it.")

answer_1 = input("Question 1) Is it animal, vegetable, or mineral? ")

answer_2 = input("Question 2) Is it bigger than a breadbox? ")

if answer_1 == "animal" and answer_2 == "yes":
    print("My guess is that you are thinking of a moose.")
elif answer_1 == "animal" and answer_2 == "no":
    print("My guess is that you are thinking of a squirrel.")

elif answer_1 == "vegetable" and answer_2 == "yes":
    print("My guess is that you are thinking of a watermelon.")
elif answer_1 =="vegetable" and answer_2 == "no":
    print("My guess is that you are thinking of a carrot.")

elif answer_1 == "mineral" and answer_2 == "yes":
    print("My guess is that you are thinking of a Camaro.")
elif answer_1 == "mineral" and answer_2 == "no":
    print("My guess is that you are thinking of a paper clip.")

else:
    print("Whoops, looks like your input is invalid.")
