from Dominio.luchadores import Luchador

class Judoka(Luchador):

    TIPO="Judoka"

    def __init__(self, nombre:str, energia:int = 100):
        super().__init__(nombre, energia)

    def golpear(self)->tuple:
        return self.DAÑO_MEDIO,"(Atemi Waza) golpea"
    
    def bloquear(self)->tuple:
        return self.FACTOR_BLOQUEO,"(Uke Waza) Postura defensiva"
    
    def sujetar_y_lanzar(self)->tuple:
        return self.DAÑO_ALTO,"(Ippon Seoi Nage) Sujetar y lanzar "
