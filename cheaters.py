from datetime import datetime
import csv


def cheaters() -> list:
    result = []
    start_times = {}
    with open("start_times.csv") as fp:
        for line in csv.reader(fp, delimiter=";"):
            start_times[line[0]] = datetime.strptime(line[1], "%H:%M")
    finish_times = {}
    with open("submissions.csv") as fp:
        for line in csv.reader(fp, delimiter=";"):
            time = datetime.strptime(line[3], "%H:%M")
            student_time = finish_times.get(
                line[0], datetime.strptime("00:00", "%H:%M"))
            if time > student_time:
                finish_times[line[0]] = line[3]
    # for start_time in start_times:

    print(len(finish_times))
    # for student in finish_times:
    #     print(student)
    return []


# start_time = datetime.strptime("17:00", "%H:%M")
# finish_time = datetime.strptime("16:05", "%H:%M")

# print(start_time > finish_time)

cheaters()
