'''
Entrada: Número total de vacas en la zona de Azkoitia que están a la venta.
Entrada: Peso total que el camión puede llevar.
Entrada: Lista de pesos de las vacas.
Entrada: Lista de la producción de leche por vaca, en litros por día.
Salida: Cantidad máxima de producción de leche se puede obtener.
'''
import itertools as it


def main():
    # Datos con resultado: vaca 1, 4, 5, 6, total 93
    vacas_totales = 6
    peso_maximo_camion = 700
    pesos_por_vaca = [360, 250, 400, 180, 50, 90]
    litros_por_vaca = [40, 35, 43, 28, 12, 13]

    # # Datos con resultado: vaca 2, 3, 4, 5, 6 total 188
    # vacas_totales = 8
    # peso_maximo_camion = 1000
    # pesos_por_vaca = [223, 243, 100, 200, 200, 155, 300, 150]
    # litros_por_vaca = [30, 34, 28, 45, 31, 50, 29, 1]

    # # Datos con resultado: vaca 1, 2, 3, 4, 5, 6, 8, 9 total 320
    # vacas_totales = 10
    # peso_maximo_camion = 2000
    # pesos_por_vaca = [340, 355, 223, 243, 130, 240, 260, 155, 302, 130]
    # litros_por_vaca = [45, 50, 34, 39, 29, 40, 30, 52, 31, 1]

    vacas = crear_lista_de_vacas(
        vacas_totales, pesos_por_vaca, litros_por_vaca)
    (litros, grupo_mas_eficiente) = elegir_grupo_mas_eficiente(
        vacas, peso_maximo_camion)
    print("Los litros máximos por día son", litros)
    print("Lo conseguimos subiendo las siguientes vacas al camión:")
    for vaca in grupo_mas_eficiente:
        print("Número: ", vaca.numero, " con un peso de ",
              vaca.peso, " kilos y ", vaca.litros, " litros por día")


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
    Crear todos los grupos posibles de vaca, utilizando la funcion combinations de itertools, lo que nos crear las posibles combinaciones de N elementos en P posiciones, por lo que lo hacemos en bucle desde 1 (sólo una vaca en el camión) hasta len(vacas) + 1 (ya que range coge un elemento menos que el indicado como segundo parámetro, esto haría que el valor mayor sea el de len(vacas), el caso en el que subimos todas las vacas al camión) (enlace a explicacion de itertools en https://realpython.com/python-itertools/). Por cada grupo que se genera, calculamos (sumando los valores de cada vaca) tanto el peso total del grupo como los litros por día producidos por el grupo. En caso de que el peso sea menor o igual al permitido en el camión y los litros producidos sean mayores que los grupos anteriores, se guarda el valor de litros por día y el grupo.
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


class Vaca:
    def __init__(self, numero, peso, litros):
        self.numero = numero
        self.peso = peso
        self.litros = litros


if __name__ == "__main__":
    main()
