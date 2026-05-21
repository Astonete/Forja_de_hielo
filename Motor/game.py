import random
from Dominio.luchadores import Luchador
from Dominio.boxeador import Boxeador 
from Dominio.judoka import Judoka
from Dominio.sumotori import Sumotori
from Dominio.reglas import Reglas
from UI_Consola.Interfaz import (
    bienvenida,
    seleccionar_luchador,
    mostrar_cpu_seleccionado,
    mostrar_estado_combate,
    menu_accion_jugador,
    mostrar_resultado_turno,
    resultado_final,
    mensaje_interaccion
)

ACCIONES=["golpear","bloquear","sujetar_y_lanzar"]

#clase padre----------------------------------------------------
def calcular_daño(de: Luchador, Para: Luchador,
                accion_de: str, reaccion_del_enemigo: str) -> tuple:

#---(accion GOLPEAR) ------------------------------------------------------------------------------
    if accion_de=="golpear":# Luchador realiza accion
        daño_base,msg=de.golpear()

        # diferentes reaccines del oponente ante la accion
        if reaccion_del_enemigo =="golpear":
            return 0,"" # misma accion, sin efecto

        if reaccion_del_enemigo =="bloquear":
            # bloquear tiene prioridad el golpe impacta pero reducido
            return round (daño_base * Para.FACTOR_BLOQUEO),msg

        if reaccion_del_enemigo=="sujetar_y_lanzar":# golpear tiene priorida sobre sujetar: daño completo
            return daño_base,msg

#---(accion SUJETAR Y LANZAR)----------------------------------------------------------------------
    elif accion_de =="sujetar_y_lanzar":#luchuador realiza accion
        daño_base,msg=de.sujetar_y_lanzar()

        if reaccion_del_enemigo=="sujetar_y_lanzar":
            return 0,"" # misma accion, sin efecto

        if reaccion_del_enemigo=="bloquear":
        # si el sumotori recibe el daño recibe el valor del daño base + DAÑO_BAJO
            if isinstance(Para, Sumotori):
                return daño_base + Para.DAÑO_BAJO, msg
            # Caso normal: sujetar gana a bloquear
            return daño_base, msg

        if reaccion_del_enemigo=="golpear":
            return 0,""

#---(accion BLOQUEAR)-------------------------------------
    elif accion_de=="bloquear":
        _,msg = de.bloquear()
        
        if reaccion_del_enemigo=="bloquear":
            return 0,"" # misma accion, sin efecto
        
        if reaccion_del_enemigo=="golpear":
        #si el sumotori bloquea recibe daño reducido y causa DAÑO_BAJO=5.7 a quien golpea
            if isinstance(de, Sumotori):
                return de.DAÑO_BAJO, msg
            return 0,msg
        
        if reaccion_del_enemigo=="sujetar_y_lanzar":
            return 0,""
#----------------------------------------------------

def resolver_turno(jugador: Luchador, cpu: Luchador, accion_jugador:str, accion_cpu:str )-> dict:
    #resuelve un turno completo de combate.
    #aplica daños a ambos luchadores y retorna un diccionario con los toda la informacion del turno
    resultado_interaccion = Reglas.gana_interaccion(accion_jugador, accion_cpu)

    #calcula el daño(antes de aplicarlos)
    daño_j, msg_j=calcular_daño(jugador, cpu, accion_jugador, accion_cpu)
    daño_c, msg_c=calcular_daño(cpu, jugador, accion_cpu, accion_jugador)
    
    #aplicar daños
    daño_real_cpu=cpu.daño_recibido(daño_j)
    daño_real_jugador=jugador.daño_recibido(daño_c)
    
    # mensaje de accion del jugador
    def texto_accion(luchador: Luchador, accion:str)->str:
        if accion=="golpear":
            return luchador.golpear()[1]
        elif accion=="bloquear":
            return luchador.bloquear()[1]
        elif accion=="sujetar_y_lanzar":
            return luchador.sujetar_y_lanzar()[1]
        return ""

    lineas=[]
    lineas.append(
        f"[{jugador.nombre} {accion_jugador.upper()}: {texto_accion(jugador, accion_jugador)}]"
    )
    lineas.append(
        f"[{cpu.nombre} {accion_cpu.upper()}: {texto_accion(cpu, accion_cpu)}]"
    )
    lineas.append("---------------------------------------------------------------------------")
    lineas.append(
        f" >>{mensaje_interaccion(accion_jugador, accion_cpu, jugador, cpu, resultado_interaccion)}"
    )
    lineas.append("---------------------------------------------------------------------------")
    
    if daño_real_cpu>0:
        extra=f"({msg_j})" if msg_j else ""
        lineas.append(
            f"{cpu.nombre} recibe {daño_real_cpu} de daño {extra}"
            f" [Energia: {cpu.energia}/{cpu.energia_maxima}]"
        )
    if daño_real_jugador>0:
        extra=f"({msg_c})" if msg_c else ""
        lineas.append(
            f"{jugador.nombre} recibe {daño_real_jugador} de daño {extra}"
            f" [Energia: {jugador.energia}/{jugador.energia_maxima}]"
        )
    if daño_real_cpu==0 and daño_real_jugador==0:
        lineas.append("sin daño en este turno")

    return{
        "daño_a_cpu": daño_real_cpu,
        "daño_a_jugador": daño_real_jugador,
        "accion_jugador": accion_jugador,
        "accion_cpu": accion_cpu,
        "lineas": lineas,
    }

def elegir_accion_cpu()->str:
    return random.choice(ACCIONES)

def crear_cpu_luchador()->Luchador:
    nombre_cpu="C.P.U."
    ClaseCPU=random.choice([Boxeador, Judoka, Sumotori])
    return ClaseCPU(nombre_cpu)

class Game:
    def __init__(self):
        self.jugador = None
        self.cpu = None
        self.turno = 1

    def iniciar(self):
        # 1. Preparamos los luchadores.
        bienvenida()

        self.jugador = seleccionar_luchador("Seleccion del jugador")
        self.cpu = crear_cpu_luchador()

        mostrar_cpu_seleccionado(self.cpu)
        mostrar_estado_combate(self.jugador, self.cpu, self.turno)

        # 2. Repetimos turnos hasta que uno de los luchadores pierda.
        terminado = False
        ganador = None

        while not terminado:
            accion_jugador = menu_accion_jugador()
            accion_cpu = elegir_accion_cpu()

            resultado = resolver_turno(
                self.jugador,
                self.cpu,
                accion_jugador,
                accion_cpu,
            )

            mostrar_resultado_turno(resultado, self.jugador, self.cpu)
            terminado, ganador = Reglas.verificar_fin_juego(self.jugador, self.cpu)
            self.turno += 1

        # 3. Mostramos el resultado final.
        resultado_final(self.jugador, self.cpu, ganador)
