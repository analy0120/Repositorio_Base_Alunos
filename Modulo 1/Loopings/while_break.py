L=[]
while True:
    n=input(input("digite um numero(digite >pare< para sair):")) 
    if n == ('pare'):
        print("encerrando processo")
        break 
    L.append(n)
x=0
while x < len(L):
    print(L[x])
    x=x+1
