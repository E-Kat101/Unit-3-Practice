import time
import os

repeats = 5
steps_per_second = 10

for i in range(20 * repeats):
    os.system("clear")

    if i % 20 == 0:
        print(" ---o___---___O---___ ")
    elif i % 20 == 1:
        print(" --o___---___O---___- ")
    elif i % 20 == 2:
        print(" -o___---___O---___-- ")
    elif i % 20 == 3:
        print(" o___---___O---___--- ")
    elif i % 20 == 4:
        print(" ___---___O---___---o ")
    elif i % 20 == 5:
        print(" __---___O---___---o_ ")
    elif i % 20 == 6:
        print(" _---___O---___---o__ ")
    elif i % 20 == 7:
        print(" ---___O---___---o___ ")
    elif i % 20 == 8:
        print(" --___O---___---o___- ")
    elif i % 20 == 9:
        print(" -___O---___---o___-- ")
    elif i % 20 == 10:
        print(" ___O---___---o___--- ")
    elif i % 20 == 11:
        print(" __O---___---o___---_ ")
    elif i % 20 == 12:
        print(" _O---___---o___---__ ")
    elif i % 20 == 13:
        print(" O---___---o___---___ ")
    elif i % 20 == 14:
        print(" ---___---o___---___O ")
    elif i % 20 == 15:
        print(" --___---o___---___O- ")
    elif i % 20 == 16:
        print(" -___---o___---___O-- ")
    elif i % 20 == 17:
        print(" ___---o___---___O--- ")
    elif i % 20 == 18:
        print(" __---o___---___O---_ ")
    elif i % 20 == 19:
        print(" _---o___---___O---__ ")

    time.sleep(0.5/steps_per_second)
