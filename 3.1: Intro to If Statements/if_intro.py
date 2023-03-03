robot_location = 30
ball_location = 35
goal_location = 20
have_ball = False

if robot_location < ball_location:
    print("Almost at the ball")

if robot_location > goal_location:
    print("You are beyond the goal.")

if robot_location == goal_location:
    print("The robot is at the goal.")

robot_location += 5

if robot_location == goal_location:
    print("At the goal.")

if robot_location == ball_location:
    print("At the ball")
    print("Picking up the ball.")
    have_ball = True
    print("Now make your way to the goal.")

robot_location -= 15

if robot_location < goal_location:
    print("You went too far.")

if robot_location == goal_location and have_ball is True:
    print("You scored a goal!")
    have_ball = False

#---Questions---
# 1. What do you think the if does to the code under it?
    # I think that if the if statement is true, then the code underneath it is put into play.
	# If the if statement is false, then the code underneath it does not work.
	# For example, if robot_location == goal_location is true, then the message underneath it is printed. Otherwise, no message is printed.

# 2. What is the purpose indenting in the if statement? How can we tell what code is enclosed in an if branch and what code is not?
    # The purpose of indenting in the if statement is to show what code is enclosed in an if branch.
	# If the code underneath the if statement is indented, that means that the code is part of that if statement branch.

# 3. Change the initial locations of the objects and get the program to output the same thing.

robot_location = 40
ball_location = 60
goal_location = 30
have_ball = False

if robot_location < ball_location:
    print("Almost at the ball")

if robot_location > goal_location:
    print("You are beyond the goal.")

if robot_location == goal_location:
    print("The robot is at the goal.")

robot_location += 20

if robot_location == goal_location:
    print("At the goal.")

if robot_location == ball_location:
    print("At the ball")
    print("Picking up the ball.")
    have_ball = True
    print("Now make your way to the goal.")

robot_location -= 30

if robot_location < goal_location:
    print("You went too far.")

if robot_location == goal_location and have_ball is True:
    print("You scored a goal!")
    have_ball = False

# 4. What do the operators += and -= do?
    # += adds a value to the given variable, whereas -= substracts a value from the variable.
	# For example, robot_location += 2 would add 2 to the robot's location, and robot_location -= 2 would remove 2.
