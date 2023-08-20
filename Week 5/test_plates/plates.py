def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    # contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters
    maxLen, minLen = 6, 2
    if maxLen >= len(s) >= minLen and s.isalnum():
        if s.isalpha():
            return True
        else:
            """ Numbers cannot be used in the middle of a plate; they must come at the end.
            For example, AAA222 would be an acceptable … vanity plate; AAA22A would not be acceptable.
            The first number used cannot be a ‘0’. """
            letters = s[:2].isalpha()
            numbers = s[-2:].isdigit()
            if letters and numbers:
                for i in range(len(s)):
                    if s[i].isdigit():
                        if s[i].startswith("0") or s[i:].isalpha():
                            return False
                        else:
                            return True
            else:
                return False
    else:
        return False

if __name__ == "__main__":
    main()