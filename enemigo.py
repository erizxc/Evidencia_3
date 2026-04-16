class Enemigo:
    def __init__(self, nombre, vida, daño, nivel, tipo):
        self.__nombre = nombre
        self.__vida = vida
        self.__vida_base = vida
        self.__daño = daño
        self.__nivel = nivel
        self.__tipo = tipo
    
    def info(self):
        print(f"Nombre: {self.__nombre}, Vida: {self.__vida}, Daño: {self.__daño}, Nivel: {self.__nivel}, Tipo: {self.__tipo}")

    def atacar(self):
        if self.__vida == self.__vida_base:
            return f"{self.__nombre} ha hecho {self.__daño} de daño"
        
        elif self.__vida <= self.__vida_base / 2:
            return f"{self.__nombre} ha hecho {self.__daño + 7} de daño"
        
        else:
            return f"{self.__nombre} ha hecho {self.__daño} de daño"

    
    #GETTERS
    def get_nombre(self):
        return self.__nombre
    
    def get_vida(self):
        return self.__vida
    
    def get_vida_base(self):
        return self.__vida_base
    
    def get_daño(self):
        return self.__daño
    
    def get_nivel(self):
        return self.__nivel
    
    def get_tipo(self):
        return self.__tipo
    
    #SETTERS
    def set_nombre(self, nombre):
        self.__nombre = nombre

    def set_vida(self, vida):
        self.__vida = vida

    def set_vida_base(self, vida):
        self.__vida_base = vida
    
    def set_daño(self, daño):
        self.__daño = daño

    def set_nivel(self, nivel):
        self.__nivel = nivel
    
    def set_tipo(self, tipo):
        self.__tipo = tipo

    


