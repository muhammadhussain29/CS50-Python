import random


def main():
    level = get_level()
    i=0
    score=0
    while i<10:
        score += generate_integer(level)
        i+=1
    print(f"Score: {score}")


def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level == 1 or level == 2 or level == 3:
                return level
            else:
                raise ValueError
        except ValueError:
            pass


def generate_integer(level):
    if level == 1:
        x = random.randint(0,9)
        y = random.randint(0,9)
    elif level == 2:
        x = random.randint(10,99)
        y = random.randint(10,99)
    else:
        x = random.randint(100,999)
        y = random.randint(100,999)

    ans = x + y
    i=0
    while i<3:
        try:
            print(f"{x} + {y} = ",end="")
            sol = int(input())
            if sol == ans:
                return 1
            else:
                raise ValueError
        except ValueError:
            i+=1
            print("EEE")
    print(f"{x} + {y} = {ans}")
    return 0



if __name__ == "__main__":
    main()