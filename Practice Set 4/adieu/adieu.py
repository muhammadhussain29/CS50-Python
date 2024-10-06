names = []

i = 0
while True:
    try:
        names.append(input("Name: "))
        i+=1
    except EOFError:
        break
    
print("Adieu, adieu, to ", end="")

for name in names[0:-1]:
    print(name, end="")
    if len(names) > 2:
        print(", ", end="")

if len(names) > 1:
    if len(names) == 2:
        print(" and ", end="")
    else:
        print("and ", end="")
print(names[-1])
