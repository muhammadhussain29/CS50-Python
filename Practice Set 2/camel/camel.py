word = input("Enter a word is camelCase " )
for a in word:
    if(a.lower() == a):
        print(a ,end="")
    else:
        print("_" + a.lower() , end="")