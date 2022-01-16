with open('data.txt', 'rb') as file:
    data = file.read()
    c = len(data)
    print("          00 01 02 03 04 05 06 07 08 09 0a 0b 0c 0d 0e 0f")
    string = ""
    for (i, word) in enumerate(data):
        if i % 16 == 0:
            print(string)
            string = "    "
            print('0' * (6 - len(hex(i)[2:])) + hex(i)[2:], end="    ")

        if chr(word).isprintable():
            string += chr(word)

        else:
            string += "."

        print("0" * (2 - len(hex(word)[2:])) + hex(word)[2:], end=" ")
    print(" " * (3 * (16 - 1 - i % 16)) + string)