print("Treasure Locator")


def input_cords():
    print(" ")
    cords = input("put your cords here: ")

    if cords.lower() == "close":
        return

    usercords = cords.split()

    try:
        xIn = int(usercords[0])
        zIn = int(usercords[1])
    except ValueError:
        print("An error has accured! make sure you do) {x cords} {z cords}")
        input_cords()
        return

    counter1 = 0
    counter2 = 0

    countX = int
    countZ = int

    closeX4 = 0
    closeZ4 = 0

    # find nearest x 4, 4
    while (counter1 <= 8):
        countX = counter1 + xIn

        if (countX - 9) % 16 == 0:
            closeX4 = countX

        counter1 += 1

    while (counter1 >= -8):
        countX = counter1 + xIn

        if (countX - 9) % 16 == 0:
            closeX4 = countX

        counter1 -= 1

    # find nearest z 4, 4
    while (counter2 <= 8):
        countZ = counter2 + zIn

        if (countZ - 9) % 16 == 0:
            closeZ4 = countZ

        counter2 += 1

    while (counter2 >= -8):
        countZ = counter2 + zIn

        if (countZ - 9) % 16 == 0:
            closeZ4 = countZ

        counter2 -= 1

    # print sh entrance
    print("Treasure location: " + str(closeX4) + ", " + str(closeZ4) + ".")
    input_cords()


input_cords()
