greet = input("Enter Greeting Msg : ").split()
greet = greet[0].lower().strip()

if greet == "hello":
    print("$0")
elif greet[0] == "h":
    print("$20")
else:
    print("$100")