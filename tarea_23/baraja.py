class Baraja:
    # Objeto que contiene la lista de "cartas" (valores
    # del 1 al 52 y las letras A y B) con las funciones
    # necesarias para modificar sus posiciones según
    # los pasos descritos en el algoritmo del solitario
    def __init__(self):
        baraja = list(map(str, [*range(1, 53)]))
        baraja.extend(['A', 'B'])
        self.baraja = baraja

    def mover_carta(self, valor, puestos):
        # Función que mueve una carta específica
        # elegida según su valor (1 a 52, A o B)
        # en X puestos (siempre en una dirección)
        posicion_original = self.baraja.index(valor)
        nueva_posicion = posicion_original + puestos
        if nueva_posicion >= len(self.baraja):
            nueva_posicion += 1
        nueva_posicion %= len(self.baraja)
        self.baraja.remove(valor)
        self.baraja.insert(nueva_posicion, valor)

    def mover_cartas_por_comodines(self):
        # Función que intercambia los dos bloques de
        # cartas a ambos lados de los dos comodines
        # (si un comodín está en un extremo de la
        # baraja sólo se mueve un bloque, si ambos
        # están en los extremos la baraja mantiene su
        # posición
        posicion_comodin_a = self.baraja.index('A')
        posicion_comodin_b = self.baraja.index('B')
        if posicion_comodin_a < posicion_comodin_b:
            primer_comodin = 'A'
            segundo_comodin = 'B'
            posicion_primer_comodin = posicion_comodin_a
            posicion_segundo_comodin = posicion_comodin_b
        else:
            primer_comodin = 'B'
            segundo_comodin = 'A'
            posicion_primer_comodin = posicion_comodin_b
            posicion_segundo_comodin = posicion_comodin_a

        primer_bloque = self.baraja[:posicion_primer_comodin]
        segundo_bloque = self.baraja[posicion_primer_comodin +
                                     1:posicion_segundo_comodin]
        tercer_bloque = self.baraja[posicion_segundo_comodin+1:]

        self.baraja = tercer_bloque
        self.baraja.append(primer_comodin)
        self.baraja.extend(segundo_bloque)
        self.baraja.extend(segundo_comodin)
        self.baraja.extend(primer_bloque)

    def cortar_por_valor_ultima_carta(self):
        # Función que mueve un bloque de cartas hacia
        # el final (pero manteniendo la última carta
        # en su posición). El número de cartas movido
        # depende del valor de la última carta
        ultima_carta = self.baraja[-1]
        if ultima_carta != 'A' and ultima_carta != 'B':
            valor_ultima_carta = int(ultima_carta)
            primer_bloque = self.baraja[:valor_ultima_carta]
            segundo_bloque = self.baraja[valor_ultima_carta: -1]
            self.baraja = segundo_bloque
            self.baraja.extend(primer_bloque)
            self.baraja.append(ultima_carta)

    def obtener_valor_de_letra(self):
        # Función que devuelve una letra, en base
        # al valor numérico de la carta "elegida"
        # según el valor de la primera carta en
        # la baraja
        primera_carta = self.baraja[0]
        if primera_carta != 'A' and primera_carta != 'B':
            valor_primera_carta = int(primera_carta)
        else:
            valor_primera_carta = 53
        carta_a_traducir = self.baraja[valor_primera_carta]
        if carta_a_traducir != 'A' and carta_a_traducir != 'B':
            valor_carta_a_traducir = int(carta_a_traducir)
            valor_carta_a_traducir = (valor_carta_a_traducir % 26)
            return valor_carta_a_traducir
        return None
