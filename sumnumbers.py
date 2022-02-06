scores = []
while True :
    y = int (input("enter number :"))
    scores.append(y)

    x = int (input("1: Continue  2: Exite ?"))
    if x == 2 :
        break

b = sum(scores)

print("sum:" , b)
