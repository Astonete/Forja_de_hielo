import os
from Dominio.luchadores import Luchador
from Dominio.boxeador import Boxeador
from Dominio.judoka import Judoka
from Dominio.sumotori import Sumotori

def limpiar_consola():
    if os.name=='nt':
        os.system('cls')
    else:
        os.system('clear')

def barra_energia(energia:int, maxima: int)->str:
    return f"Energia: {energia}/{maxima}"

# ----------------Panalla---------------------------------------
def bienvenida():
    limpiar_consola()
    print("<---( Torneno de Artes Marciales Orientada a Objeto)--->")
    print("Tecnicas de combate\n")
    print("    [1] 🥊 Boxeo: ")
    print("el Boxeador habilidad especial - Golpear poderoso (Gancho cruzado)")
    print("    [2] 🥋 Judo : ")
    print("el Judoka habilidad especial - Sujetar y lanza  devastador (Ippon Seoi-nage)")
    print("    [3] 🤼 Sumo : ")
    print("el Sumotori habilidad especial - Bloqueo con contraataque (Kachi-age)\n")
    print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
    print("((( Sistema de prioridades de interacciones)))")
    print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
    print("    [1🤜] Golpear  👍 gana a 👎Sujetar y Lanzar [3🔧]")
    print("    [2🛡️ ] Bloquear 👍 gana a 👎Golpear [1🤜] (reduce daño recibido)")
    print("    [3🔧] Sujetar  👍 gana a 👎Bloquear [3🛡️ ]")
    input("\nPresiona ENTER para elegir tu luchador...")

def seleccionar_luchador(titulo:str)-> Luchador:
    clases={
        "1":("Boxeador", Boxeador),
        "2":("Judoka", Judoka),
        "3":("Sumotori", Sumotori),
    }
    limpiar_consola()
    print(f"  {titulo}")
    for key,(nombre_clase, _) in clases.items():
        print(f"  [{key}] {nombre_clase}")

    while True:
        opcion=input("-> Elige tu clase de Luchador ([1🥊], [2🥋] o [3🤼]): ").strip()
        if opcion in clases:
            break
        print("Opcion invalida. Elige ([1🥊], [2🥋] o [3🤼]")
    nombre_clase,Clase_luchador=clases[opcion]
    nombre=input(f"Competidor {nombre_clase} ¿como te Llamas?: ").strip()
    if not nombre:
        nombre= f" jugador {nombre_clase}"
    return Clase_luchador(nombre)

def mostrar_cpu_seleccionado(cpu: Luchador):#muestra la clase Seleccionada de La Cpu
    print(f"🤖 es {cpu.nombre} ({cpu.TIPO})")

def mostrar_estado_combate(jugador: Luchador, cpu: Luchador,turno:int):
    limpiar_consola()
    
    print(f"Turno: "+str(turno))
    print(f"\nJugador: {jugador.nombre} ({jugador.__class__.__name__})")
    print(f"💚: {barra_energia(jugador.energia,jugador.energia_maxima)}")

    print(" VS ")

    print(f"{cpu.nombre}: ({cpu.__class__.__name__})")
    print(f"💚: {barra_energia(cpu.energia,cpu.energia_maxima)}")
    input("  Que comience el combate! Presiona ENTER...")

def menu_accion_jugador():
    #muestar el menu de accion y retorna la accion elegida
    limpiar_consola()
    print("|---------------------------|")
    print("|Elige tu movimiento        |")
    print("|    [1🤜] Golpear           |")
    print("|    [2🛡️] Bloquear          |")
    print("|    [3🔧] Sujetar y Lanzar  |")
    print("|---------------------------|")
    while True:
        opcion = input("  Tu eleccion (1🤜, 2🛡️ o 3🔧): ").strip()
        if opcion == "1":
            return "golpear"
        elif opcion == "2":
            return "bloquear"
        elif opcion == "3":
            return "sujetar_y_lanzar"
        else:
            print("  Opcion invalida. Elige 1🤜, 2🛡️ o 3🔧.")

def mostrar_resultado_turno(resultado:dict, jugador:Luchador,cpu:Luchador):
#Mostrar el resultado  del turno
    for linea in resultado["lineas"]:
        print(linea)
    print(".........................................................................")
    print(f"👤 {jugador.nombre}: {barra_energia(jugador.energia, jugador.energia_maxima)}")
    print(f"🤖 {cpu.nombre}: {barra_energia(cpu.energia, cpu.energia_maxima)}")
    print(".........................................................................")
    input("  Presiona ENTER para el siguiente turno...")

def resultado_final(jugador:Luchador,cpu:Luchador,ganador:str):
    limpiar_consola()
    print(f"Fin del combate")
    if ganador =="jugador":
        print(f"---🏆 🎖️ Y el Ganador del Kombate orientado a objetos es {jugador}")
        print("eres una Leyenda brindaremos y se haran canciones en tu nombre por tu azaña")
    elif ganador =="cpu":
        print(f"--- Y el Ganador es {cpu.nombre} 🦾")
        print("no te sientas mal es alumno de Cyrax, T-1000, RoboCop y Optimus Prime")
    else:
        print(f"  *** EMPATE! Ambos luchadores han caido Fue un combate Honorable. ***")
    print(f"  {jugador.nombre}💚 Energia final: {jugador.energia}/{jugador.energia_maxima}")
    print(f"  {cpu.nombre}💚 Energia final: {cpu.energia}/{cpu.energia_maxima}")

def mensaje_interaccion(accion_jugador:str, accion_enemigo:str, jugador: Luchador, cpu: Luchador, resultado:str)->str:
    if resultado=="Empate":
        return f"👤 {jugador.nombre} y 🤖{cpu.nombre} 🙅¡Es un empate!: {accion_jugador}"
    elif resultado=="a":
        return f"👤 {jugador.nombre} 👍({accion_jugador}) vence a 🤖 {cpu.nombre} 👎({accion_enemigo})"
    else:
        return f"🤖 {cpu.nombre} 👍({accion_enemigo}) vence a 👤 {jugador.nombre} 👎({accion_jugador})"