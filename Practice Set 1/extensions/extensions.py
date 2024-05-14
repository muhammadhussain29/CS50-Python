file = input("File Name : ").lower().split(".")[1]
match file:
    case "gif":
        print("image/gif")
    case "jpg":
        print("image/jpg")
    case "jpeg":
        print("image/jpeg")
    case "png":
        print("image/png")
    case "pdf":
        print("image/pdf")
    case "txt":
        print("image/txt")
    case "zip":
        print("image/zip")
    case _:
        print("application/octet-stream")
