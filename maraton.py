j=int(input("ingrese el diametro del lago"))
k=int(input("ingrese el k de la caña"))
k1=k/100
c=((k1*k1)-((j*j)/4))/(-2*k1)
  
print ("la profundidad es ",round(c,1))
