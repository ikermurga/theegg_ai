from baraja import Baraja


class GeneradorSolitario:
    def __init__(self, conversor):
        self.conversor = conversor
        self.baraja = Baraja()

    def generar_letras_secuencia_de_clave(self, numero_letras):
        letras = []
        while len(letras) < numero_letras:
            self.baraja.mover_carta('A', 1)
            self.baraja.mover_carta('B', 2)
            self.baraja.mover_cartas_por_comodines()
            self.baraja.cortar_por_valor_ultima_carta()
            valor = self.baraja.obtener_valor_de_letra()
            if valor is not None:
                letra = self.conversor.transformar_valor_a_letra(valor)
                letras.append(letra)
        return letras
