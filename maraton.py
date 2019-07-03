i=1
r=0
lista=[]
while i!=0:
    datos=input()
    listaDatos=datos.split(' ')
    j=int(listaDatos[0])
    k=int(listaDatos[1])
    if j!=0 and k!=0:    
        k1=k/100
        c=((k1*k1)-((j*j)/4))/(-2*k1)
        lista.insert(r,c)
        r += 1
    else: 
        i=j+k 
    if i==0:
        for x in range (0, r):
            print (round(lista[x],1) ) 
        break
