from baraja import Baraja


class GeneradorSolitario:
    # Clase que genera la clave (la base del algoritmo del
    # solitario) a partir de una baraja. Utiliza un objeto
    # baraja que lleva el orden de las cartas tras cada paso
    # y un ConversorLetrasNumeros para pasar de letras a
    # números y viceversa.
    def __init__(self, conversor):
        self.conversor = conversor
        self.baraja = Baraja()

    # Los pasos del algoritmo de crear la clave del solitario
    # para lo que se indica a un objeto de tipo baraja el
    # orden y la cantidad de veces (dependiendo de la cantidad
    # de letras del texto a cifrar/descifrar) que tiene
    # que ejecutarse.
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
