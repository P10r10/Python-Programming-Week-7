from datetime import datetime


def is_it_valid(pic: str) -> bool:
    if len(pic) != 11:
        return False
    day = pic[0:2]
    month = pic[2:4]
    year = pic[4:6]
    control = int(day + month + year + pic[7:10])
    year = int(year)
    if pic[6] == "-":
        year += 1900
    elif pic[6] == "+":
        year += 1800
    elif pic[6] == "A":
        year += 2000
    else:
        return False
    try:
        datetime(year, int(month), int(day))
    except:
        return False
    control = control % 31
    if "0123456789ABCDEFHJKLMNPRSTUVWXY"[control] != pic[10]:
        return False
    return True


print(is_it_valid("230827-906F"))
print(is_it_valid("120488+246L"))
print(is_it_valid("310823A9877"))
print(is_it_valid("230827-906F1"))
