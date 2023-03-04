print("WELCOME TO THE HAUNTED MANSION")
print("You are in a haunted mansion. Would you like to explore the A) Basement or B) Attic?")
choice_1 = input("> ").upper()

if choice_1 == "A":
    print("You enter the basement where it is pitch black and hear a scary noise coming from one of the corners of the room. Beside you on a desk there are two objects. Do you choose A) Lollipop or B) Knife?")
    choice_2 = input("> ").upper()

    if choice_2 == "A":
        print("You pick up the lollipop and near the place the scary noise is coming from. Suddenly, a monster jumps out, and it seems interested in your lollipop. Do you A) Give the lollipop to the monster or B) Stick the lollipop in your mouth?")
        choice_3 = input("> ").upper()

        if choice_3 == "A":
            print("You give the monster the lollipop and... it receives it kindly and helps you find an exit to the haunted house, giving you $10,000,000,000 out of gratitude.")
        elif choice_3 == "B":
            print("You stick the lollipop in your mouth, throwing the monster a smug and taunting expression. Of course, that was a terrible idea because before you get to react, the monster charges at you, opening its gaping mouth. The last thing you see before tasting the bitter feeling of death is its millions upon millions rows of teeth. RIP.")
        else:
            print("Oops. Looks like your input is invalid.")
    
    elif choice_2 == "B":
        print("You pick up the knife and near the corner. Suddenly, a monster jumps out and sees your knife, so its expression turns apprehensive. Do you A) Drop the knife or B) Charge at the monster, the tip of your knife pointed towards it?")
        choice_3 = input("> ").upper()

        if choice_3 == "A":
            print("You drop the knife and it clatters to the ground. The monster gives you a look of disgust before backing back into its corner and curling up into a ball to go to sleep. You leave the haunted house without any physical scars, but something definitely got hurt mentally.")
        elif choice_3 == "B":
            print("You decide to run at the monster, knife pointed towards it. However, your rather dumb decision ends up getting you swallowed whole by the monster. Before you die, you see its mouth open to twice your size, and you see that it has millions upon millions of rows of teeth. This may not be obvious, but you made a terrible decision. RIP.")
        else:
            print("Oops. Looks like your input is invalid.")
    else:
        print("Oops. Looks like your input is invalid.")


elif choice_1 == "B":
    print("You decide to climb up to the attic. There, you see a small girl crying in the corner of the room. Do you A) Ask her what is wrong or B) Laugh at her?")
    choice_2 = input("> ").upper()

    if choice_2 == "A":
        print("You ask the girl what is wrong. She doesn't answer, and instead just slowly turns her head to look at you. Her face is veeery scary. Do you A) Tell her that you are here for her if she needs to vent or B) Scream?")
        choice_3 = input("> ").upper()

        if choice_3 == "A":
            print("In a comforting voice, you tell her that you are here to support her. She smiles and calls you over to sit beside her. Then she rants to you about how her parents want her to become a doctor but she wants to pursue her life-long dream of being an artist. She appreciates your consolation and rewards you with 10 gold bars and a way to exit the haunted house. You are strong enough to carry only one gold bar, but it's the thought that counts.")
        elif choice_3 == "B":
            print("Apparently her face is that scary because it causes you to scream. Suddenly, her expression turns grim and in a split second, she leaps at you, baring her sharp claws. She claws you to death. Serves you right. RIP.")
        else:
            print("Oops. Looks like your input is invalid.")
    elif choice_2 == "B":
        print("You laugh at her, and suddenly the crying stops. She slowly turns to look at you, and you see that her face is unnaturally pale and her eyes are glowing red. Uh oh. You messed up. Do you A) Drops to your knees and apologize profusely or B) Insult her looks?")
        choice_3 = input("> ").upper()

        if choice_3 == "A":
            print("You fall to the ground, muttering apologies. It seems as though she gives you the benefit of the doubt, because she just tells at you to get out. You run out of the Haunted House and never go back.")
        elif choice_3 == "B":
            print("Woah, you should really learn not to run your mouth and instead to run on your feet. Unfortunately, it's too late for you to even run away because in a split second, you hear a loud noise come from above. You look up and see that a piano was hanging on the ceiling, but not the strings have been cut and it comes tumbling down towards you. Now you're a pancake. Great. RIP.")
        else:
            print("Oops. Looks like your input is invalid.")
else:
    print("Oops. Looks like your input is invalid.")

print("Thank you for playing!!! Try playing again and getting another outcome.")
