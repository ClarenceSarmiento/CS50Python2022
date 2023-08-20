import re


def main():
    print(parse(input("HTML: ")))


def parse(s):
    link = r"<iframe src=\"https?://(?:www\.)?youtube\.com/embed/([\w]+)\"></iframe>"
    if matches := re.search(link, s):
        return f"https://youtu.be/{matches.group(1)}"
    else:
        return None


if __name__ == "__main__":
    main()