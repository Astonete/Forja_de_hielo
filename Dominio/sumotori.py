from Dominio.luchadores import Luchador

class Sumotori(Luchador):

    TIPO="Sumotori"
    
    def __init__(self, nombre:str, energia:int=100):
        super().__init__(nombre, energia)
    
    def golpear(self)->tuple:
        return self.DAÑO_MEDIO,"(Tsuppari) golpea"
    
    def bloquear(self)->tuple:
        return self.FACTOR_BLOQUEO,"(Kachi-age) Bloquea"
    
    def sujetar_y_lanzar(self)->tuple:
        return self.DAÑO_MEDIO,"(Uwatenage) Sujeta y Lanza"
