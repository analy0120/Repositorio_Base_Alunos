try:
    divisao = 10 / 0
    print(divisao)
except:
    print('''nao foi
    possivel realizar
    essa operacao''')

def atividade(x,y):
    try:
        result = x/y
    except ZeroDivisionError:
        print("por Favor, nao utilize zeros!")
    except:
        print("\033[91m algo deu errado...]")
    else:
        print("seu resultado e:{resulta}")
    finally:
        print("\033[92m vamos de novo?]")
    divide(13,0)

    