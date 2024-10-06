def main():
    plates = input("Plate: ")
    if is_valid(plates):
        print("valid")
    else:
        print("invalid")

def num_check(s):

    location = 0
    first_num = None

    for i in s:
        if i.isnumeric():
            first_num = i
            break
        else:
            location = location + 1

    if first_num == None :
        return True

    if first_num == '0':
        return False
    else:
        s = s.split(s[location])[1]
        for i in s:
            if not i.isnumeric():
                return False
    
    return True

def is_valid(s):
    valid_len = False
    valid_char = True
    valid_punc = True
    valid_num_chk = num_check(s) 

    if len(s) >= 2 and len(s) <= 6:
        valid_len = True
        if s[0].isnumeric() or s[1].isnumeric() :
            valid_char = False
            for i in s:
                if i == "." or i == " " or i == "\'" or i == "," or i == "!" or i == "?" :
                    valid_punc = False
                    for i in s:
                        if i.isnumeric():
                            x = s.split(i)

    if valid_len and valid_char and valid_punc and valid_num_chk:
        return True
    else:
        return False
         

if __name__ == "__main__":
    main()