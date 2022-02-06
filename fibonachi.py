from re import A


f = [1]
a = 0
b = 1

n = int(input(" n = ? "))

if n == 0 :
    print ("Error!")

if n == 1 :    
    print(f)

while n>=2 :
    c = a + b 
    f.append(c)
    a = b
    b = c
    print(f)
    n -= 1   
             

