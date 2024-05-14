grocery = {}
while True:
    try:
        prompt = input().upper()
        if prompt in grocery:
            grocery[prompt] += 1 
        else:
            grocery.update({prompt : 1})
    except KeyError:
        continue
    except EOFError:
        break

for k in sorted(grocery.keys()):
        print(grocery[k] , k)
