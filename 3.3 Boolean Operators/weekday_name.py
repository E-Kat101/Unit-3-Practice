weekday = int(input("What is the day number? "))

if weekday == 1:
    print(f"Weekday {weekday}: Monday")
elif weekday == 2:
    print(f"Weekday {weekday}: Tuesday")
elif weekday == 3:
    print(f"Weekday {weekday}: Wednesday")
elif weekday == 4:
    print(f"Weekday {weekday}: Thursday")
elif weekday == 5:
    print(f"Weekday {weekday}: Friday")
elif weekday == 6:
    print(f"Weekday {weekday}: Saturday")
elif weekday == 0 or weekday == 7:
    print(f"Weekday {weekday}: Sunday")
else:
    print(f"Weekday {weekday}: error")
