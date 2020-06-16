class ConversorLetrasNumeros:
    def __init__(self):
        self.letras = [
            'A', 'B', 'C', 'D', 'E',
            'F', 'G', 'H', 'I', 'J',
            'K', 'L', 'M', 'N', 'O',
            'P', 'Q', 'R', 'S', 'T',
            'U', 'V', 'W', 'X', 'Y',
            'Z']

    def transformar_valor_a_letra(self, valor):
        return self.letras[valor - 1]

    def transformar_letra_a_valor(self, letra):
        valor = self.letras.index(letra.upper()) + 1
        return valor
