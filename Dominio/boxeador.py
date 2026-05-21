from Dominio.luchadores import Luchador

class Boxeador(Luchador):

    TIPO="Boxeador"

    def __init__(self, nombre:str, energia:int = 100):
        super().__init__(nombre, energia)

    def golpear(self)->tuple:
        return self.DAÑO_ALTO,"(Gancho Cruzado) golpea"
    
    def bloquear(self)->tuple:
        return self.FACTOR_BLOQUEO,"(Cobertura) Bloquea"
    
    def sujetar_y_lanzar(self)->tuple:
        return self.DAÑO_MEDIO,"(Clich) Sujeta y lanza"
