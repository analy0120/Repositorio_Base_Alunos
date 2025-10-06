class Passaro():
    def __init__(self,tamanho,cores,especie,sexo):
        self.tamanho = tamanho
        self.cores = cores 
        self.especie = especie
        self.sexo = sexo 

    def cantar(self):
        return print(f'sou um {self.especie} cantando uma bela cançao 🎵')

    def cantar(self):
        return print('batendo as asas e: voando...')

Passaro1 = Passaro(0.14,['marrom','branco','cinza',],'pardal','M')
Passaro1.cantar()