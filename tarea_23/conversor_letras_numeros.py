class ConversorLetrasNumeros:
    # Objeto que contiene una lista de letras
    # y métodos para pasar de una letra a su
    # valor numérico y viceversa
    def __init__(self):
        self.letras = [
            'A', 'B', 'C', 'D', 'E',
            'F', 'G', 'H', 'I', 'J',
            'K', 'L', 'M', 'N', 'O',
            'P', 'Q', 'R', 'S', 'T',
            'U', 'V', 'W', 'X', 'Y',
            'Z']

    def transformar_valor_a_letra(self, valor):
        # Función que devuelve la letra a partir de un
        # valor numérico
        return self.letras[valor - 1]

    def transformar_letra_a_valor(self, letra):
        # Función que devuelve un valor numérico a
        # partir de una letra
        valor = self.letras.index(letra.upper()) + 1
        return valor
