score = []

n = int(input("tedad daneshjouyan? "))

for i in range(n) :
    x = float (input("nomarat: "))
    score.append(x)

average = sum(score) / n

print("Max: ", max(score))
print("Min: " , min(score))
print ("average: ", average) 