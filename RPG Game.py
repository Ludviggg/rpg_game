def jump_lines(l):
    for a in range(l):
        print("\t")


health = 10

print("Welcome to THE GAME!")
jump_lines(3)

while True:
    print("You are walking in the woods when you see a bear, what do you do?")
    print("Attack     Run     Hide")
    task1 = input().lower()
    jump_lines(1)

    if task1 == "attack":
        health -= 7
        print("You attacked the bear and lost 7 health")
        print("Your health is currently", health)
        if health < 1:
            break

    elif task1 == "run":
        print("You got away without losing any health")
        print("Your health is currently", health)

    elif task1 == "hide":
        health -= 10
        print("You where hiding but the bear found you and you lost 10 health")
        print("Your health is currently", health)
        if health < 1:
            break

    else:
        print("You typed something wrong!")
        break
    jump_lines(1)


    print("Now you are lost in the woods, where do you walk?")
    print("Right     Left")
    task2 = input().lower()
    jump_lines(1)

    if task2 == "right":
        jump_lines(1)
        print("You walked about 100 meters when u see a river, what do you do?")
        print("Swim     Go back")
        task3 = input().lower()

        if task3 == "swim":
            health -= 3
            print("You swim down the river until you come to the end. You got so tired that you lost 3 health")
            print("Your health is currently", health)
            if health < 1:
                break

        elif task3 == "go back":
            pass

        else:
            print("You typed something wrong!")
            break

    elif task2 == "left":
        pass

    else:
        print("You typed something wrong!")
        break
    jump_lines(1)


    print("You found a lonely house with smoke comming from the chimney, what do you do?")
    print("Enter     Knock")
    task4 = input().lower()
    jump_lines(1)

    if task4 == "enter":
        pass

    elif task4 == "knock":
        health -= 10
        print("A witch opened the door and put a spell on you which made you lose 10 health")
        print("Your health is currently", health)
        if health < 1:
            break

    else:
        print("You typed something wrong!")
        break
    jump_lines(1)


    print("When you enter the house you see four potions, which one do you drink?")
    print("Blue     Black     Red     Green")
    task5 = input().lower()
    jump_lines(1)

    if task5 == "blue":
        health -= 4
        print("You suddenly feel very cold, so cold that you lose 4 health")
        print("Your health is currently", health)
        if health < 1:
            break

    elif task5 == "black":
        print("You instantly turn into stone and die")
        break

    elif task5 == "red":
        health += 3
        print("Your heart start pumping faster and you feel alive, you gain 3 health")
        print("Your health is currently", health)

    elif task5 == "green":
        health += 6
        print("You feel stronger and stronger, you gain 6 health")
        print("Your health is currently", health)

    else:
        print("You typed something wrong!")
        break
    jump_lines(1)


    print("A door opens and a witch comes out, what do you do?")
    print("Run     Fight")
    task6 = input().lower()
    jump_lines(1)

    if task6 == "run":
        break

    elif task6 == "fight":
        health -= 10
        if health < 1:
            print("You fought the witch and lost 10 health")
            print("Yout health is currently", health)
            break
        else:
            print("You killed the witch and won!")
            break

    else:
        print("You typed something wrong!")
        break


jump_lines(1)
if health < 1:
    print("YOU LOST!")