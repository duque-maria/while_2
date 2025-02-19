
#input 
h = int(input("digite el valor de la altura inicial: "))

#processing
q = h/5 
n = 0

while h>= q:
    h = 0.9*h
    n= n + 1

#output
print("la pelota no alcanza a subir la quinta parte de la altura inicial al  " +str(n) + " rebotes")