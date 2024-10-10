import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    time = s.split(' ')
    formatedTime = [00,00,00,00]
    # print(formatedTime)

    try:
        if (time[1] != "AM" and time[1] != "PM") or (time[4] != "AM" and time[4] != "PM") or time[2] != "to":
            raise ValueError
    except IndexError:
        raise ValueError

    if re.search(r":",time[0]):
        hour,minutes = time[0].split(":")
        formatedTime[0] = int(hour) 
        formatedTime[1] = int(minutes) 
    else:
        formatedTime[0] = int(time[0])


    if re.search(r":",time[3]):
        hour,minutes = time[3].split(":")
        formatedTime[2] = int(hour) 
        formatedTime[3] = int(minutes)
    else:
        formatedTime[2] = int(time[3]) 

    # print(formatedTime)

    if time[1] == "PM":
        if formatedTime[0] != 12:
            formatedTime[0] = formatedTime[0] + 12
    else:
        if formatedTime[0] == 12:
            formatedTime[0] = formatedTime[0] + 12

    if time[4] == "PM":
        if formatedTime[2] != 12:
            formatedTime[2] = formatedTime[2] + 12
    else:
        if formatedTime[2] == 12:
            formatedTime[2] = formatedTime[2] + 12

    # print(formatedTime)

    if formatedTime[0] > 24 or formatedTime[1] >= 60 or formatedTime[2] > 24 or formatedTime[3] >= 60:
        raise ValueError
    
    # print(formatedTime)

    formatedTime[0] = formatedTime[0] % 24
    formatedTime[1] = formatedTime[1] % 60
    formatedTime[2] = formatedTime[2] % 24
    formatedTime[3] = formatedTime[3] % 60

    # print(time)
    # print(formatedTime)


    return f"{formatedTime[0]:02}:{formatedTime[1]:02} to {formatedTime[2]:02}:{formatedTime[3]:02}"

if __name__ == "__main__":
    main()