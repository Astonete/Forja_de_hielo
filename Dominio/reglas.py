from Dominio.luchadores import Luchador

# Prioridad de acciones primer elemento tiene prioridad sobre el segundo
class Reglas:
    PRIORIDAD_A={
        ("golpear","sujetar_y_lanzar"),
        ("bloquear","golpear"),
        ("sujetar_y_lanzar","bloquear")
}
#reglas----------------------------------------------------
    @staticmethod
    def gana_interaccion(accion_a:str,accion_b:str) ->str:
        if accion_a==accion_b:
            return "Empate"
        elif (accion_a,accion_b) in Reglas.PRIORIDAD_A:
            return "a"
        return "b"

    def verificar_fin_juego(jugador: Luchador, cpu: Luchador)-> tuple:
        # retorna(terminado: bool, ganador: str | None)
        # ganador puede ser judador, cpu o empate
        
        j_vivo=jugador.estado_vivo()
        c_vivo=cpu.estado_vivo()
        
        if not j_vivo and not c_vivo:
            return True,"empate"
        elif not j_vivo:
            return True, "cpu"
        elif not c_vivo:
            return True, "jugador"
        else:
            return False,None