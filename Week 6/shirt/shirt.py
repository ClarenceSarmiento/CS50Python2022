from PIL import Image, ImageOps
import sys
import os

def to_edit(input_file, output_file):
    try:
        shirt = Image.open("shirt.png")
        with Image.open(input_file) as image:
            cropped_image = ImageOps.fit(image, shirt.size)
            cropped_image.paste(shirt, mask= shirt)
            cropped_image.save(output_file)
    except FileNotFoundError:
        sys.exit("Input does not exist")

def main():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    else:
        extensions = [".jpg", ".jpeg", ".png"]
        input_file = os.path.splitext(sys.argv[1])
        output_file = os.path.splitext(sys.argv[2])
        if output_file[1].lower() not in extensions:
            sys.exit("Invalid Output")
        elif input_file[1].lower() == output_file[1].lower():
            to_edit(sys.argv[1], sys.argv[2])
        else:
            sys.exit("Input and output have different extensions")

if __name__ == "__main__":
    main()