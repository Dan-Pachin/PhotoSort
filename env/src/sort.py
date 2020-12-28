import os


def run(path):
    print(path)
    location = path[1:-2]
    print(location)
    base, folder = os.path.split(location)
    print("base: " + base)
    print("folder: " + folder)

    for img in os.listdir(location):
        if os.path.isfile(location + "/" + img):
            filename, file_extension = os.path.splitext(img)
            if folder not in img:
                os.rename(location + "/" + img, location + "/" + folder + " " + filename + " " + file_extension)
                print(filename)
            else:
                print(filename + " Папка уже в названии!")

if __name__ == "__main__":
    run(input("Выберите папку:"))
