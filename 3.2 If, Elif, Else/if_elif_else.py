team_a_points = 25
team_a_wins = 15

team_b_points = 20
team_b_wins = 16

if team_a_points > team_b_points:
    print("Team A wins!")
    team_a_wins += 1
elif team_b_points > team_a_points:
    print("Team B wins!")
    team_b_wins += 1
else:
    print("Tie.")

if team_a_wins > team_b_wins:
    print("Team A has more wins than Team B.")
elif team_b_wins > team_a_wins:
    print("Team B has more wins than Team A.")
else:
    print("Both Teams A and B have the same number of wins.")

"""
---Questions---
1. Why do you suppose the output says "Both Teams A and B have the same number of wins." when team_a_wins is initialized as only 15 and team_b_wins is initialized as 16?

In the first if statement, "if team_a_points > team_b_points", the condition is true because
team_a_points equals 25 and team_b_points equals 20, which is less. Due to this, the code
underneath that if statement is run, and part of that code adds a value of 1 to team_a_wins,
increasing the team's total wins from 15 to 16. This is equal to team_b_wins.

2. What do you think elif and else are doing?

I think that 'elif' is executed if the if statement above it comes out as false, meaning the
condition is not met. Then, if the condition stated in the elif statement is false, the else
statement is executed. In other words, 'elif' states a different condition from the if
statement, and 'else' is executed if neither the 'if' nor 'elif' conditions are met.

3. Pick one of the elif statements and change it to if instead. What difference does that make? Why?

if team_a_points > team_b_points:
    print("Team A wins!")
    team_a_wins += 1
if team_b_points > team_a_points:
    print("Team B wins!")
    team_b_wins += 1
else:
    print("Tie.")

By changing the 'elif' to 'if', the code first checks if the condition of the first statement
is met. Then, even though the condition in this case is true, the code will still go on to
check the second if statement. However, with an elif, the code would stop at the first
condition that is true.
"""
