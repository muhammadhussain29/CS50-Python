def main():
    inp = input("Input: ")
    word = shorten(inp)
    print(word)


def shorten(word):
    line = ""
    for i in word:
        if(i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u' or  i == 'A' or  i == 'E' or i == 'I' or  i == 'O' or i == 'U'):
            continue
        else:
            line += i
    return line

if __name__ == "__main__":
    main()
