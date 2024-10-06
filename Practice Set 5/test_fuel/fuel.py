while(True):
    prompt = input("Fraction :")
    try:
        x , y = prompt.split("/")
        x = int(x)
        y = int(y)
        if x > y :
            continue
        fuel = round((x/y)*100)
        break
    except (ValueError , ZeroDivisionError):
        continue

if fuel <= 1:
    print("E")
elif fuel >= 99:
    print("F")
else:
    print(f"{fuel}%")
