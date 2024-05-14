def main():
    time = input("What time is it : ")
    time = convert(time)

    if time >= 7.00 and time <= 8.00 :
        print("Breakfast Time")
    elif time >= 12.00 and time <= 13.00:
        print("Lunch Time")
    elif time >= 18.00 and time <= 19.00:
        print("Dinner Time")

def convert(time):
    hours , minites = time.split(":") 
    return float(int(hours) + (int(minites)/60))


if __name__ == "__main__":
    main()