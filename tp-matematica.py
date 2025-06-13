def obtener_conjuntos(dnis):
    """Devuelve una lista de conjuntos de dígitos únicos para cada DNI."""
    return [set(dni) for dni in dnis]
# recibe una lista de dnis (como cad de txt) y devuelve una lista de conjuntos de de digitos de cada dni.

def mostrar_conjuntos(conjuntos):
    print("\n")
    print("Conjuntos de dígitos únicos:")
    for i, c in enumerate(conjuntos, 1):
        print(f"Conjunto {chr(64+i)}: {sorted(c)}")
# imprime cada conjunto de digito unicos, identificandolos con letras A, B, C.

def operaciones_conjuntos(conjuntos):

    A, B, C = conjuntos
    union = A | B | C 
    interseccion = A & B & C
    diferencia_A_B = A - B
    diferencia_sim_B_C = B ^ C
    print("\n")
    print("Operaciones entre conjuntos:")
    print(f"Unión (A ∪ B ∪ C): {sorted(union)}")
    print(f"Intersección (A ∩ B ∩ C): {sorted(interseccion)}")
    print(f"Diferencia (A - B): {sorted(diferencia_A_B)}")
    print(f"Diferencia simétrica (B Δ C): {sorted(diferencia_sim_B_C)}")
    return interseccion
# realiza operaciones entre conjuntos, unión, intersección, diferencia y diferencia simétrica mostrando los resultados.

def evaluar_expresiones_logicas(conjuntos, interseccion):
    print("\n")
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

def frecuencia_y_suma(dnis):
    print("\n")
    print("Frecuencia de dígitos y suma total por DNI:")
    for i, dni in enumerate(dnis, 1):
        frecuencia = {str(d): dni.count(str(d)) for d in range(10)}
        suma = sum(int(d) for d in dni)
        print(f"DNI {i}: {dni} - Frecuencia: {frecuencia} - Suma total: {suma}")
# para cada dni calcula la frecuencia de cada digito (0-9) y la suma total de los dígitos.

def operaciones_anios_nacimiento(anios):
    pares = 0
    impares = 0
    for anio in anios:
        if anio % 2 == 0:
            pares += 1
        else:
            impares += 1
    print("\n")
    print("Operaciones con años de nacimiento:")
    print(f"Nacidos en años pares: {pares}")
    print(f"Nacidos en años impares: {impares}")

    if all(anio > 2000 for anio in anios):
        print("Grupo Z")
    else:
        print("No todos nacieron después del 2000.")

    def es_bisiesto(anio):
        return (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0)

    if any(es_bisiesto(anio) for anio in anios):
        print("Tenemos un año especial")
    else:
        print("Nadie nació en un año bisiesto.")

    anio_actual = 2025
    edades = [anio_actual - anio for anio in anios]
    
    conjunto_anios = set(anios)
    conjunto_edades = set(edades)

    producto_cartesiano = [(a, e) for a in sorted(list(conjunto_anios)) for e in sorted(list(conjunto_edades))]
    print("\n")
    print("Producto cartesiano (Año, Edad):")
    for par in producto_cartesiano:
        print(par)
# realiza operaciones con años de nacimiento: cuenta pares e impares, verifica si todos son mayores a 2000,
# si hay años bisiestos y calcula el producto cartesiano entre años y edades actuales.

def main():
    """
    Punto de entrada del programa.
    Solicita DNI y años de nacimiento al usuario, luego ejecuta las operaciones.
    """
    print("\n" * 2)
    print("Inicio del Programa Integrador de Matemática y Programación")
    print("\n" * 2)

    # --- INGRESO DE DATOS ---
    num_integrantes = 3

    dnis_input = []
    print("INGRESO DE DNIS:")
    print(" ")
    for i in range(num_integrantes):
        while True:
            dni_valido = input(f"Ingrese el DNI del integrante {i+1} de 3 (solo números, 7 u 8 dígitos): ")
            if dni_valido.isdigit() and 7 <= len(dni_valido) <= 8:
                dnis_input.append(dni_valido)
                break
            else:
                print("DNI inválido. Por favor, ingrese solo dígitos (7 u 8 caracteres).")

    anios_input = []
    print("\n")
    print("INGRESO DE AÑOS DE NACIMIENTO:")
    print(" ")
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

    if num_integrantes >= 3:
        conjuntos = obtener_conjuntos(dnis_input)
        mostrar_conjuntos(conjuntos)
        interseccion = operaciones_conjuntos(conjuntos)
        evaluar_expresiones_logicas(conjuntos, interseccion)
        frecuencia_y_suma(dnis_input)
    else:
        print("\n" * 2)
        print("AVISO: No se pueden realizar todas las operaciones de conjuntos (Unión, Intersección, Diferencias)")
        print("ya que se necesitan al menos 3 integrantes. Se omitirán esas secciones.")
        print("\n" * 2)
        frecuencia_y_suma(dnis_input)

    operaciones_anios_nacimiento(anios_input)

    print("\n" * 2)
    print("Fin del Programa")
    print("\n" * 2)


if __name__ == "__main__":
    main()