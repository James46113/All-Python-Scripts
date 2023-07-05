for x in range(10):
    text = input(">>>")
    space = 1
    for x in text:
        if x == " ":
            space += 1

    print(space)
