import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    find = r"(^|\W)um($|\W)"
    if matches := re.findall(find, s, re.IGNORECASE):
        return len(matches)
    else:
        return 0

if __name__ == "__main__":
    main()