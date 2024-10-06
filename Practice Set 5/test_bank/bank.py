def main():
    greet = input("Enter Greeting Msg : ").lower().strip()
    # greet = greet.
    print(f"${value(greet)}")



def value(greeting):
    if greeting == "hello":
        return 0
    elif greeting[0] == "h":
        return 20
    else:
        return 100


if __name__ == "__main__":
    main()
