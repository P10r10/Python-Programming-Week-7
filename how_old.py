from datetime import datetime


day = int(input("Day: "))
month = int(input("Month: "))
year = int(input("Year: "))

birth = datetime(year, month, day)
eve_new_millennium = datetime(1999, 12, 31)

days = eve_new_millennium - birth

if days.days >= 0:
    print(f"You were {days.days} days old on the eve of the new millennium.")
else:
    print("You weren't born yet on the eve of the new millennium.")
