from cheaters import cheaters
import csv

def final_points():

    with open("submissions.csv") as fp:
        for line in csv.reader(fp, delimiter=";"):
            if line[0] in cheaters():
                continue
            else:
                print(line[0])
    # print(cheaters())




final_points()
# students_who_cheated = cheaters() # list