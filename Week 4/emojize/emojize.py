import emoji

input = str(input("Input: ")).lower().strip()

if "_" in input:
    convert = emoji.emojize(input)
else:
    convert = emoji.emojize(input, language = 'alias')

print(f"Output: {convert}")
