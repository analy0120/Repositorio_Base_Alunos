class AnimaisMarinho:
    def __init__(self,nome, especie, tamanho, habitat, venenoso):
        self.nome = nome
        self.especie = especie 
        self.tamanho = tamanho 
        self.habitat = habitat
        self.venenoso = venenoso

    def nadar(self): 
        return f"{self.nome} esta nadando no {self.habitat}."
    def comer(self, alimento):
        return f"{self.nome} esta comendo {alimento}."
    def dormir(self):
        return f"{self.nome} esta dormindo no {self.habitat}."
    def emitir_som(self):
        return f"{self.nome} esta emitindo som bonitos."
    def info(self):
        return (f"{self.nome}\n"
            f"especies: {self.especie}\n"
            f"tamanho: {self.tamanho} m\n "
            f"habitat: {self.habitat}\n"
            f"venenoso:{'Sim' if self.venenoso else 'Nao'}")
  