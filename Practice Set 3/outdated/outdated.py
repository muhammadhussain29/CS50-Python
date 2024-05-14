months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

while True:
    date = input("Date: ")
    try:
        if "/" in date:
            mm, dd, yyyy = date.split("/")
        elif "," in date:
            mmdd, yyyy = date.split(", ")
            mm, dd = mmdd.split(" ")
            mm = (months.index(mm.capitalize())) + 1
        if int(mm) > 12 or int(dd) > 31:
            continue

        break
    except (AttributeError, NameError, ValueError, KeyError):
        continue
    

print(f"{int(yyyy):0004}-{int(mm):02}-{int(dd):02}")
