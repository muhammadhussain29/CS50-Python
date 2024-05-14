x,y,z = input("Enter Expression : ").split(" ")
result = float(0)
x = float(x)
z = float(z)

if y == "+":
    result = round((x+z),1)
elif y == "-":
    result = round((x-z),1)
elif y == "*":
    result = round((x*z),1)
elif y == "/":
    result = round((x/z),1)
    
print(result)