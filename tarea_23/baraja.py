class Baraja:
    def __init__(self):
        baraja = list(map(str, [*range(1, 53)]))
        baraja.extend(['A', 'B'])
        self.baraja = baraja

    def mover_carta(self, valor, puestos):
        posicion_original = self.baraja.index(valor)
        nueva_posicion = posicion_original + puestos
        if nueva_posicion >= len(self.baraja):
            nueva_posicion += 1
        nueva_posicion %= len(self.baraja)
        self.baraja.remove(valor)
        self.baraja.insert(nueva_posicion, valor)

    def mover_cartas_por_comodines(self):
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
        ultima_carta = self.baraja[-1]
        if ultima_carta != 'A' and ultima_carta != 'B':
            valor_ultima_carta = int(ultima_carta)
            primer_bloque = self.baraja[:valor_ultima_carta]
            segundo_bloque = self.baraja[valor_ultima_carta: -1]
            self.baraja = segundo_bloque
            self.baraja.extend(primer_bloque)
            self.baraja.append(ultima_carta)

    def obtener_valor_de_letra(self):
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
