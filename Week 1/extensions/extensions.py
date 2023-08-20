file = input("Filename: ").strip().lower().split(".")

match file[-1]:
    case "txt":
        print("text/plain")
    case "gif" | "png":
        print(f"image/{file[-1]}")
    case "jpg" | "jpeg":
        print("image/jpeg")
    case "zip" | "pdf":
        print(f"application/{file[-1]}")
    case _:
        print("application/octet-stream")