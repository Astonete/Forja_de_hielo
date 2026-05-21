from abc import ABC, abstractmethod # importar la clase ABC y el decorador abstractmethod
#para crear una clase abstracta
import random # alan importar el módulo random para generar números aleatorios

class Luchador(ABC):# ABC hace a la clase como no instanciable
    #clase abstracta que representa un luchador en el juego (abstraccion)
    TIPO= None #//Preguntar despues alan o sofi o samu<- Atributo constante define la sublclase del luchador (Boxeador,Judoka,Sumotori)
    # Valor de daños bases Globales para cada tipo de Luchador
    DAÑO_BAJO=5.7
    DAÑO_MEDIO=20
    DAÑO_ALTO=30
    FACTOR_BLOQUEO=0.5 # factor de reducción de daño al bloquear, se utiliza para calcular el daño reducido
#cuando un luchador bloquea un ataque

    def __init__(self,nombre:str,energia:int=100):
        self._nombre=nombre # atributos privados protegidos por el guion bajo
        self._energia=energia
        self._energia_maxima=energia #preguntar alan o sofi o samu<-
    
    @property # para encapsular un atributo sin esto se acceda a traves de un metodo get_nombre()
    def nombre(self)->str:
        return self._nombre
    
    @property
    def energia(self)->int:
        return self._energia
    
    @energia.setter# preguntar alan o sofi o samu sospecho que esto no es ta bien
    def energia(self,valor:int):# sirve para modificar el valor de energia a traves de un metodo set_energia() pero con la sintaxis de una propiedad
        self._energia=max(0,valor)# se asegura de que la energia no sea negativa, si el valor es menor a 0 se asigna 0, de lo contrario se asigna el valor dado 

    @property
    def energia_maxima(self)->int:
        return self._energia_maxima

#metodo abstracto de accion Polimorfismo que debe ser implementado por las subclases de Luchador, cada tipo de luchador tendra su propia implementacion de este metodo para determinar el daño que inflige al golpear a un oponente
    @abstractmethod
    def golpear(self)->tuple:
        #retorna una tupla(daño base int, mensaje: str tipo de golpe) que representa el daño infligido por el luchador al golpear a un oponente
        pass
#preguntar alan o sofi o samu ver si se puede cambiar entender mejorar con quienes interactua

    @abstractmethod
    def bloquear(self)->tuple:
        #retorna (factor reducido daño base recibido y un mensaje el daño debe ser reducido)
        pass
    
    @abstractmethod
    def sujetar_y_lanzar(self)->tuple:
        #retorna tupla(daño base int, mensaje: str tipo de golpe) que representa el daño infligido por el luchador al realizar una tecnica de sujecion y lanzamiento sobre un oponente
        pass
    
# metodos concretos de daño
    def daño_recibido(self, cantidad:int)->int:
        aplicado= max(0,round(cantidad)) 
        self.energia-=aplicado
        return aplicado
    
    def daño_emitido(self, accion:str)->int:
        if accion=="golpear":
            daño, mensaje=self.golpear()[0]
        elif accion=="sujetar_y_lanzar":
            daño, mensaje=self.sujetar_y_lanzar()[0]
        return 0

# estado
    def estado_vivo(self)->bool:
        return self._energia>0# basta que tenga un punto de energia para
    
    def __str__(self)->str:
        return (f"{self.nombre} [{self.__class__.__name__}] "
                f"- Energia: {self.energia}/{self.energia_maxima}")

