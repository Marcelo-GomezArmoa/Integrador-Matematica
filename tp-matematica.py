# Ejercicio de Matemática: Conjuntos y Operaciones

def obtener_conjuntos(dnis):
    """Devuelve una lista de conjuntos de dígitos únicos para cada DNI."""
    return [set(dni) for dni in dnis]
# recibe una lista de dnis (como cad de txt) y devuelve una lista de conjuntos de de digitos de cada dni.
# utiliza set para eliminar duplicados.

def mostrar_conjuntos(conjuntos):
    print("Conjuntos de dígitos únicos:")
    for i, c in enumerate(conjuntos, 1):
        print(f"Conjunto {chr(64+i)}: {sorted(c)}")
# imprime cada conjunto de digito unicos, identificandolos con letras A, B, C.
# bucle for con enumerate para recorrer y enumerar los conjuntos.
# Utiliza chr(64+i) para obtener letras A, B, C, etc.
# Utiliza sorted para mostrar los dígitos en orden ascendente.
#


def operaciones_conjuntos(conjuntos):
    A, B, C = conjuntos
    union = A | B | C
    interseccion = A & B & C
    diferencia_A_B = A - B
    diferencia_sim_B_C = B ^ C
    print("\nOperaciones entre conjuntos:")
    print(f"Unión (A ∪ B ∪ C): {sorted(union)}")
    print(f"Intersección (A ∩ B ∩ C): {sorted(interseccion)}")
    print(f"Diferencia (A - B): {sorted(diferencia_A_B)}")
    print(f"Diferencia simétrica (B Δ C): {sorted(diferencia_sim_B_C)}")
    return interseccion
# realiza operaciones entre conjuntos, unión, intersección, diferencia y diferencia simétrica mostrando los resultados.
# operadores de conjuntos: | (unión), & (intersección), - (diferencia), ^ (diferencia simétrica).

def evaluar_expresiones_logicas(conjuntos, interseccion):
    if interseccion:
        print(f"\nDígitos comunes en todos los conjuntos: {sorted(interseccion)}")
    else:
        print("\nNo hay dígitos comunes en todos los conjuntos.")

    if all('0' not in c for c in conjuntos):
        print("Es un grupo sin ceros.")
    else:
        print("Algún conjunto tiene el número 0.")
# evalua expresiones lógicas sobre los conjuntos 1- si hay dígitos comunes, 2- si todos los conjuntos tienen ceros o no.
# utiliza all() para verificar si todos los conjuntos no contienen el 0.
# utiliza if para evaluar si hay dígitos comunes en todos los conjuntos

def frecuencia_y_suma(dnis):
    print("\nFrecuencia de dígitos y suma total por DNI:")
    for i, dni in enumerate(dnis, 1):
        frecuencia = {str(d): dni.count(str(d)) for d in range(10)}
        suma = sum(int(d) for d in dni)
        print(f"DNI {i}: {dni} - Frecuencia: {frecuencia} - Suma total: {suma}")
# para cada dni calcula la frecuencia de cada digito (0-9) y la suma total de los dígitos.
# utiliza  un bucle for con enumerate para recorrer los dnis.
# utiliza un diccionario por comprensión para contar la frecuencia de cada dígito en el DNI.
# utiliza sum() para calcular la suma total de los dígitos en el DNI.



def main():
    dnis = ["33418246", "41885186", "16576288"]
    conjuntos = obtener_conjuntos(dnis)
    mostrar_conjuntos(conjuntos)
    interseccion = operaciones_conjuntos(conjuntos)
    evaluar_expresiones_logicas(conjuntos, interseccion)
    frecuencia_y_suma(dnis)
# define los dnis, genera los conjuntos, ,uestra los resultados de las operaciones y evalua las expresiones lógicas.
# llama a la función main() para ejecutar el programa.
# y es el punto de entrada del programa.


if __name__ == "__main__":
    main()

