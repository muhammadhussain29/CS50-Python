change = 50
while change != 0:
    print(f"Amount Due: {change}")
    x = int(input("Insert Coin: "))
    
    if x == 25 or x == 10 or x == 5:
        change = change - x
        if change <= 0 :
            print(f"Change Owed: {abs(change)}")
            break
