# Ejercicio de Matemática: Conjuntos y Operaciones

def obtener_conjuntos(dnis):
    """Devuelve una lista de conjuntos de dígitos únicos para cada DNI."""
    return [set(dni) for dni in dnis]
# recibe una lista de dnis (como cad de txt) y devuelve una lista de conjuntos de de digitos de cada dni.
# utiliza set para eliminar duplicados.

def mostrar_conjuntos(conjuntos):
    print("\n") # Un espacio simple
    print("Conjuntos de dígitos únicos:")
    for i, c in enumerate(conjuntos, 1):
        print(f"Conjunto {chr(64+i)}: {sorted(c)}")
# imprime cada conjunto de digito unicos, identificandolos con letras A, B, C.
# bucle for con enumerate para recorrer y enumerar los conjuntos.
# Utiliza chr(64+i) para obtener letras A, B, C, etc.
# Utiliza sorted para mostrar los dígitos en orden ascendente.


def operaciones_conjuntos(conjuntos):
    # Asegurarse de que hayan 3 conjuntos para descomponer A, B, C
    if len(conjuntos) != 3 :
        print("\nSe necesitan al menos 3 conjuntos para realizar todas las operaciones (A, B, C).")
        return set() # Devolver un conjunto vacío o manejar el error según se prefiera

    A, B, C = conjuntos
    union = A | B | C 
    interseccion = A & B & C
    diferencia_A_B = A - B
    diferencia_sim_B_C = B ^ C
    print("\n") # Un espacio simple
    print("Operaciones entre conjuntos:")
    print(f"Unión (A ∪ B ∪ C): {sorted(union)}")
    print(f"Intersección (A ∩ B ∩ C): {sorted(interseccion)}")
    print(f"Diferencia (A - B): {sorted(diferencia_A_B)}")
    print(f"Diferencia simétrica (B Δ C): {sorted(diferencia_sim_B_C)}")
    return interseccion
# realiza operaciones entre conjuntos, unión, intersección, diferencia y diferencia simétrica mostrando los resultados.
# operadores de conjuntos: | (unión), & (intersección), - (diferencia), ^ (diferencia simétrica).

def evaluar_expresiones_logicas(conjuntos, interseccion):
    print("\n") # Un espacio simple
    print("Evaluación de Expresiones Lógicas (A. Operaciones con DNIs):")
    if interseccion:
        print(f"\nDígitos compartidos: {sorted(interseccion)}")
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
    print("\n") # Un espacio simple
    print("Frecuencia de dígitos y suma total por DNI:")
    for i, dni in enumerate(dnis, 1):
        frecuencia = {str(d): dni.count(str(d)) for d in range(10)}
        suma = sum(int(d) for d in dni)
        print(f"DNI {i}: {dni} - Frecuencia: {frecuencia} - Suma total: {suma}")
# para cada dni calcula la frecuencia de cada digito (0-9) y la suma total de los dígitos.
# utiliza  un bucle for con enumerate para recorrer los dnis.
# utiliza un diccionario por comprensión para contar la frecuencia de cada dígito en el DNI.
# utiliza sum() para calcular la suma total de los dígitos en el DNI.

def operaciones_anios_nacimiento(anios):
    # Contar cuántos nacieron en años pares e impares
    pares = 0
    impares = 0
    for anio in anios:
        if anio % 2 == 0:
            pares += 1
        else:
            impares += 1
    print("\n") # Un espacio simple
    print("Operaciones con años de nacimiento:")
    print(f"Nacidos en años pares: {pares}")
    print(f"Nacidos en años impares: {impares}")

    # Si todos nacieron después del 2000, mostrar "Grupo Z"
    if all(anio > 2000 for anio in anios):
        print("Grupo Z")
    else:
        print("No todos nacieron después del 2000.")

    # Si alguno nació en año bisiesto, mostrar "Tenemos un año especial"
    def es_bisiesto(anio):
        return (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0)

    if any(es_bisiesto(anio) for anio in anios):
        print("Tenemos un año especial")
    else:
        print("Nadie nació en un año bisiesto.")

    # Calcular el producto cartesiano entre años y edades actuales
    anio_actual = 2025
    edades = [anio_actual - anio for anio in anios]
    
    conjunto_anios = set(anios)
    conjunto_edades = set(edades)

    producto_cartesiano = [(a, e) for a in sorted(list(conjunto_anios)) for e in sorted(list(conjunto_edades))]
    print("\n") # Un espacio simple
    print("Producto cartesiano (Año, Edad):")
    for par in producto_cartesiano:
        print(par)
# realiza operaciones con años de nacimiento: cuenta pares e impares, verifica si todos son mayores a 2000,
#  si hay años bisiestos y calcula el producto cartesiano entre años y edades actuales.
# recibe una lista de años de nacimiento y realiza varias operaciones con ellos.
# cuenta cuántos años son pares e impares.
# verifica si todos los años son mayores a 2000 y muestra "Grupo Z" si es así.


def main():
    """
    Punto de entrada del programa.
    Solicita DNI y años de nacimiento al usuario, luego ejecuta las operaciones.
    """
    print("\n" * 2) # Más espacio al inicio
    print("Inicio del Programa Integrador de Matemática y Programación")
    print("\n" * 2)

    # --- INGRESO DE DATOS ---
    num_integrantes = 3

    dnis_input = []
    print("INGRESO DE DNIS:")
    print(" ") # Línea en blanco
    for i in range(num_integrantes):
        while True:
            dni_valido = input(f"Ingrese el DNI del integrante {i+1} de 3 (solo números, 7 u 8 dígitos): ")
            if dni_valido.isdigit() and 7 <= len(dni_valido) <= 8:
                dnis_input.append(dni_valido)
                break
            else:
                print("DNI inválido. Por favor, ingrese solo dígitos (7 u 8 caracteres).")

    anios_input = []
    print("\n") # Espacio simple
    print("INGRESO DE AÑOS DE NACIMIENTO:")
    print(" ") # Línea en blanco
    print("Si dos o más integrantes tienen el mismo año, ingrese un dato ficticio para uno de ellos (por ejemplo, +1 o -1).")
    for i in range(num_integrantes):
        while True:
            try:
                anio_valido = int(input(f"Ingrese el año de nacimiento del integrante {i+1} (ej: 1990): "))
                if 1900 <= anio_valido <= 2025:
                    anios_input.append(anio_valido)
                    break
                else:
                    print("Año inválido. Ingrese un año razonable (ej: entre 1900 y 2025).")
            except ValueError:
                print("Entrada inválida. Por favor, ingrese un número entero para el año.")
    # --- FIN DE INGRESO DE DATOS ---


    # --- Ejecución de las operaciones ---
    if num_integrantes >= 3:
        conjuntos = obtener_conjuntos(dnis_input)
        mostrar_conjuntos(conjuntos)
        interseccion = operaciones_conjuntos(conjuntos)
        evaluar_expresiones_logicas(conjuntos, interseccion)
        frecuencia_y_suma(dnis_input)
    else:
        print("\n" * 2) # Más espacio para el aviso
        print("AVISO: No se pueden realizar todas las operaciones de conjuntos (Unión, Intersección, Diferencias)")
        print("ya que se necesitan al menos 3 integrantes. Se omitirán esas secciones.")
        print("\n" * 2)
        frecuencia_y_suma(dnis_input) # Aún podemos calcular frecuencia y suma si lo deseas.


    operaciones_anios_nacimiento(anios_input) # Esta función siempre se ejecuta con los años ingresados

    print("\n" * 2) # Más espacio al final
    print("Fin del Programa")
    print("\n" * 2)


if __name__ == "__main__":
    main()