import os
from datetime import datetime

command = input("Enter command: ")

if "-f" in command:
    file_index = command.index("-f")
    file_name = command[file_index + 1]
else:
    file_name = None

if "-d" in command:
    dir_index = command.index("-d")
    dir_name = command[dir_index + 1:]
else:
    dir_name = None

if dir_name:
    path = os.path.join(*dir_name)
    os.makedirs(path, exist_ok=True)
    os.chdir(path)

if file_name:
    content = []
    while True:
        content_line = input("Enter content line: ")
        if content_line == "stop":
            content.append("\n")
            break
        content.append(content_line)

    with open(file_name, "a") as file:
        file.write(f"{datetime.now():%Y-%m-%d %H:%M:%S\n}")

        index = 1
        for line in content:
            if line != "\n":
                file.write(f"{index} {line}\n")
                index += 1
            else:
                file.write("\n")
