def convert(text):
    # Replace ":)" to emoji 🙂
    converted_text = text.replace(":)", "🙂")
    # Replace ":(" to emoji 🙁
    converted_text = converted_text.replace(":(", "🙁")
    # Return converted text
    return converted_text

def main():
    # Prompt the user
    text = input()
    # Call function convert
    converted = convert(text)
    # Print converted
    print(converted)

main()