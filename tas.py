import random
play_again = "y"

while play_again == "y" :
    print ("tas is rolling....")
    i = random.randint(1 , 6)
    print(i)

    if i == 6 :
        print ("dobare tas bendaz")
        print ("tas is rolling....")
        print(random.randint(1 , 6))

    else :
        play_again = input("do you want play again: y / n ")    