arquivo=open("numero.txt","r")
for linha in arquivo.readlines():
    print(linha)
arquivo.close() 

impares=open("impares.txt","w")
pares=open("pares.txt","w")
for n in range(0,1000):
    if n % 2 == 0: 
        pares.write("%d\n" % n)
    else:
        impares.whire("%d\n" % n)
impares.close()
pares.close()