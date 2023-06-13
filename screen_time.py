from datetime import datetime, timedelta


filename = input("Filename: ")
start_date = input("Starting date: ")
start_date = datetime.strptime(start_date, "%d.%m.%Y")
nb_days = int(input("How many days: "))
print("Please type in screen time in minutes on each day (TV computer mobile):")
screen_time = {}
for i in range(nb_days):
    display = datetime.strftime(start_date + timedelta(days=i), '%d.%m.%Y')
    screen_time[display] = input(f"Screen time {display}: ")
start_date = datetime.strftime(start_date, '%d.%m.%Y')
total_minutes = 0
for entry, value in screen_time.items():
    for n in value.split(" "):
        total_minutes += int(n)
    screen_time[entry] = value.replace(" ", "/")
with open(filename, "w") as fp:
    fp.write(f"Time period: {start_date}-{display}\n")
    fp.write(f"Total minutes: {total_minutes}\n")
    fp.write(f"Average minutes: {total_minutes / nb_days}\n")
    for entry, value in screen_time.items():
        fp.write(f"{entry}: {value}\n")
    print(f"Data stored in file {filename}")
