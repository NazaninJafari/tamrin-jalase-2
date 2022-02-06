
from this import s


x = int (input("Enter your number(seconde): "))

h = x // 3600
m = (x % 3600) // 60
s = (x % 3600) % 60

print(h ,":",m,":",s)