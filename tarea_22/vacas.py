import itertools as it


def main():
    (
        vacas_totales,
        peso_maximo_camion,
        pesos_por_vaca,
        litros_por_vaca
    ) = pedir_datos_usuario()

    vacas = crear_lista_de_vacas(
        vacas_totales, pesos_por_vaca, litros_por_vaca)
    (litros, grupo_mas_eficiente) = elegir_grupo_mas_eficiente(
        vacas, peso_maximo_camion)
    mostrarResultado(litros, grupo_mas_eficiente)


def pedir_datos_usuario():
    '''
    La función pide al usuario y devuelve el número total de vacas que están a la venta, el peso total que el camión puede llevar, la lista de pesos de las vacas y la lista de la producción de leche por vaca, en litros por día.
    '''
    peso_maximo_camion = int(
        input("Introduce el peso máximo que puede llevar el camión: "))
    vacas_totales = int(input("Introduce el número total de vacas: "))
    pesos_por_vaca = []
    litros_por_vaca = []
    for posicion in range(vacas_totales):
        peso_vaca = int(
            input(f'Introduce el peso de la vaca {posicion + 1}: '))
        litros_vaca = int(
            input(f'Introduce los litros por día de la vaca {posicion + 1}: '))
        pesos_por_vaca.append(peso_vaca)
        litros_por_vaca.append(litros_vaca)
    return (vacas_totales, peso_maximo_camion, pesos_por_vaca, litros_por_vaca)


def crear_lista_de_vacas(vacas_totales, pesos_por_vaca, litros_por_vaca):
    '''
    Crear objetos de tipo Vaca usando los datos de entrada (número de vacas, lista de pesos por vaca y lista de listros por vaca)
    '''
    vacas = []
    for posicion in range(0, vacas_totales):
        numero_de_vaca = posicion + 1
        peso_de_vaca = pesos_por_vaca[posicion]
        litros_de_vaca = litros_por_vaca[posicion]
        vacas.append(Vaca(numero_de_vaca, peso_de_vaca, litros_de_vaca))
    return vacas


def elegir_grupo_mas_eficiente(vacas, peso_maximo_camion):
    '''
    Crear todos los grupos posibles de vaca, utilizando la funcion combinations de itertools, lo que nos crea listas con las posibles combinaciones de N elementos en P posiciones, por lo que lo hacemos en bucle desde 1 (sólo una vaca en el camión) hasta len(vacas) + 1 (ya que range coge un elemento menos que el indicado como segundo parámetro, esto haría que el valor mayor sea el de len(vacas), el caso en el que subimos todas las vacas al camión - enlace a explicacion de itertools en https://realpython.com/python-itertools/). 

    Por cada grupo que se genera, calculamos (sumando los valores de cada vaca) tanto el peso total del grupo como los litros por día producidos por el grupo. En caso de que el peso sea menor o igual al permitido en el camión y los litros producidos sean mayores que los grupos anteriores, se guarda el valor de litros por día y el grupo.

    Al acabar el bucle, tendremos el máximo número de litros guardado en litros_maximos y el grupo de vacas (la lista de objetos vacas) que los genera guardados en grupo_con_litros_maximos por lo que devolvemos los dos valores.
    '''
    litros_maximos = 0
    grupo_con_litros_maximos = []
    for numero_de_vacas_elegidas in range(1, len(vacas) + 1):
        for grupo in it.combinations(vacas, numero_de_vacas_elegidas):
            litros_por_grupo = 0
            peso_por_grupo = 0
            for vaca in grupo:
                litros_por_grupo += vaca.litros
                peso_por_grupo += vaca.peso
            if peso_por_grupo < peso_maximo_camion and litros_por_grupo > litros_maximos:
                litros_maximos = litros_por_grupo
                grupo_con_litros_maximos = grupo

    return (litros_maximos, grupo_con_litros_maximos)


def mostrarResultado(litros, grupo_mas_eficiente):
    '''
    La función recibe un número con el máximo número de litros
    y una lista de vacas que forman el grupo más eficiente.
    Se muestran en consola tanto los litros totales como
    información sobre cada una de las vacas que forman el grupo
    '''
    print("Los litros máximos por día son", litros)
    print("Lo conseguimos subiendo las siguientes vacas al camión:")
    for vaca in grupo_mas_eficiente:
        print(vaca.info())


class Vaca:
    '''
    Clase que crea los objetos dentro de los cuales guardaremos información sobre cada una de las vacas.
    Incluye un método info el cual devuelve la información en una cadena de texto.
    '''

    def __init__(self, numero, peso, litros):
        self.numero = numero
        self.peso = peso
        self.litros = litros

    def info(self):
        return f'Número:{self.numero} con un peso de {self.peso} kilos y {self.litros} litros por día'


if __name__ == "__main__":
    main()
