def mostrar_conjuntos(conjuntos):
    print("Conjuntos de dígitos únicos:")
    for i, c in enumerate(conjuntos, 1):
        print(f"Conjunto {chr(64+i)}: {sorted(c)}")
      
      
mostrar_conjuntos([{1, 2, 3}, {4, 5, 6}, {7, 8, 9}])