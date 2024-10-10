import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    if re.search(r'<iframe(.)*><\/iframe>', s):
        link = s.split("src=\"",1)[1].split("\"",1)[0]
        if re.search(r"(youtube.com)",link):
            if link.find("www") != -1 :
                link = link.replace("www.","")
            if link.find("http://") != -1:
                link = link.replace("http","https")
            link = link.replace("youtube.com/embed","youtu.be")
            return link

    return None



if __name__ == "__main__":
    main()