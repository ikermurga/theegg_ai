class Pokemon:
    '''
    Clase para instanciar los objetos Pokemon
    Se inicializa con unos puntos de vida,
    ataque y un nombre. 
    En caso de ganar, si ejecutamos el método
    win mostraremos el mensaje de que ha ganadol
    '''

    def __init__(self, vida, ataque, nombre):
        self.vida = vida
        self.ataque = ataque
        self.nombre = nombre

    def win(self):
        print(f'El pokemon {self.nombre} ha ganado')


def main():
    '''
    El método principal del programa. Crea dos objetos
    de tipo Pikachu, asigna sus valores, hace que se
    ataquen entre ellos restando vida hasta que uno
    tenga menos de 0. Finalmente muestra un mensaje
    sobre quién ha ganado
    '''
    pikachu = Pokemon(100, 55, "Pikachu")
    jigglypuff = Pokemon(100, 35, "Jigglypuff")
    turno = 1

    while pikachu.vida > 0 and jigglypuff.vida > 0:
        if turno == 1:
            jigglypuff.vida = jigglypuff.vida - pikachu.ataque
            turno = 0
        else:
            pikachu.vida = pikachu.vida - jigglypuff.ataque
            turno = 1

    if pikachu.vida <= 0:
        jigglypuff.win()
    else:
        pikachu.win()


if __name__ == "__main__":
    main()
