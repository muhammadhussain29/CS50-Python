import sys

content = []
lines=0

if len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
elif len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
else:
    try:
        name , extension = sys.argv[1].split(".")
        if extension == "py":
            try:
                with open(sys.argv[1]) as file:
                    for line in file:
                        content.append(line)      
            except FileNotFoundError:
                sys.exit("File does not exist")   
        else:
            raise ValueError
    except ValueError:
        sys.exit("Not a Python file")

for i in content:
    if i.strip()  == "":
        continue
    elif i.strip()[0] == "#":
        continue
    else:
        lines+=1
    
print(lines)