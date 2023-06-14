import urllib.request
import json
from math import floor


def retrieve_all() -> list:
    """
    At the address https://studies.cs.helsinki.fi/stats-mock/api/courses you
    will find basic information about some of the courses offered by the
    University of Helsinki Department of Computer Science, in JSON format.
    Please write a function named retrieve_all(), which retrieves the data of
    all the courses which are currently active (the field enabled has the value
    true). These should be returned as a list of tuples, in the following
    format:

    Sample output
    [
        ('Full Stack Open 2020', 'ofs2019', 2020, 201),
        ('DevOps with Docker 2019', 'docker2019', 2019, 36),
        ('DevOps with Docker 2020', 'docker2020', 2020, 36),
        ('Beta DevOps with Kubernetes', 'beta-dwk-20', 2020, 28)
    ]
    """
    my_request = urllib.request.urlopen(
        "https://studies.cs.helsinki.fi/stats-mock/api/courses")
    courses = json.loads(my_request.read())
    result = []
    for course in courses:
        if course["enabled"]:
            total = 0
            for n in course['exercises']:
                total += n
            result.append((course['fullName'],
                          course['name'], course['year'], total))
    return result


def retrieve_course(course_name: str) -> dict:
    """
    Each course also has its own URL, where more specific weekly data about the
    course is available. The URLs follow the format
    https://studies.cs.helsinki.fi/stats-mock/api/courses/****/stats, where you
    would replace the stars with the contents of the field name for the course
    you want to access.
    For example, the data for the course docker2019 is at the address
    https://studies.cs.helsinki.fi/stats-mock/api/courses/docker2019/stats.
    Please write a function named retrieve_course(course_name: str), which
    returns statistics for the specified course, in dictionary format.
    For example, the function call retrieve_course("docker2019") would return a
    dictionary with the following contents:

        Sample output
        {
            'weeks': 4,
            'students': 220,
            'hours': 5966,
            'hours_average': 27,
            'exercises': 4988,
            'exercises_average': 22
        }
    """
    result = {}
    url = f"https://studies.cs.helsinki.fi/stats-mock/api/courses/{course_name}/stats"
    my_request = urllib.request.urlopen(url)
    course = json.loads(my_request.read())
    result["weeks"] = len(course)
    max_students = 0
    total_hours = 0
    sum_exercises = 0
    for week in course:
        max_students = max(max_students, course[week]["students"])
        total_hours += course[week]["hour_total"]
        sum_exercises += course[week]["exercise_total"]
    result["students"] = max_students
    result["hours"] = total_hours
    result["hours_average"] = floor(total_hours / max_students)
    result["exercises"] = sum_exercises
    result["exercises_average"] = floor(sum_exercises / max_students)

    return result


print(retrieve_all())
print(retrieve_course("docker2019"))
