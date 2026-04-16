class Enemigo:
    def __init__(self, nombre, vida, daño, nivel, tipo):
        self.__nombre = nombre
        self.__vida = vida
        self.__daño = daño
        self.__nivel = nivel
        self.__tipo = tipo
    
    def get_nombre(self):
        return self.__nombre
    
    def get_vida(self):
        return self.__vida
    
    def get_daño(self):
        return self.__daño
    
    def get_nivel(self):
        return self.__nivel
    
    def get_tipo(self):
        return self.__tipo
    

