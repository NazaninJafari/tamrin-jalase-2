
while True :

    h = int(input("heure: "))
    m = int(input("minute : "))
    s = int(input("seconde: "))

    clock = (h * 3600) + (m * 60) + s 

    print("tabdile saat be sanie: " , clock)
    y = int (input("1:continue or 2:exite "))
    if y == 2 :
        break