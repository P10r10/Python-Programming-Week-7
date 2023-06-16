from datetime import datetime
import csv


def time_is_valid(name: str, time: str) -> bool:
    start_times = {}
    with open("start_times.csv") as fp:
        for line in csv.reader(fp, delimiter=";"):
            start_times[line[0]] = datetime.strptime(line[1], "%H:%M")
    finish_time = datetime.strptime(time, "%H:%M")
    return (finish_time - start_times[name]).seconds <= 10800


def final_points():
    # store submissions in nested dictionaries
    submissions = {}
    with open("submissions.csv") as fp:
        for line in csv.reader(fp, delimiter=";"):
            if line[0] not in submissions:  # key = name
                submissions[line[0]] = {}
            if not time_is_valid(line[0], line[3]):
                continue
            if line[1] not in submissions[line[0]]:  # task
                submissions[line[0]][line[1]] = int(line[2])  # points
            elif int(line[2]) > submissions[line[0]][line[1]]:
                submissions[line[0]][line[1]] = int(line[2])
    # compute total points
    total_points = {}
    for name, points in submissions.items():
        total = 0
        for val in points.values():
            total += val
        total_points[name] = total
    return total_points


print(final_points())
