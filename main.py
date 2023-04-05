v_hechos = dict()
base_reglas = list()
reglas = list()
reglas_utilizadas = list()
hechos = list()


# Función para leer las reglas desde un archivo de texto y almacenarlas en una lista
# También se encarga de leer la base de hechos y almacenarla en una lista
def leer_reglas(nombre_archivo):
    global base_reglas
    global reglas
    global hechos
  
    with open(nombre_archivo, 'r') as archivo:
        for linea in archivo:
            linea = linea.strip()
            # Leer base de hechos (se reconoce porque empieza con #)
            if linea.startswith('#'):
                hechos = (linea[1:].split(','))
                continue
            # Dividir la línea en antecedentes y consecuentes a partir de la implicación
            antecedentes, consecuentes = linea.split('=>')
            antecedentes = antecedentes.replace(" ", "")
            # Convertir los consecuentes en una lista de hechoes
            consecuentes = [hecho.strip() for hecho in consecuentes.split(',') if hecho]
            # Agregar la regla a la lista de reglas
            reglas.append((antecedentes, consecuentes))
        base_reglas = reglas
        print("Reglas iniciales: ")
        mostrar_reglas(reglas)
        print("Hechos iniciales: ", hechos)


# Función para asignar valores a los hechos de la base de conocimiento y a los hechos de la base de reglas
def asignar_valores_hechos():
    global v_hechos
    global hechos
    global reglas
    # Asignar valores a los hechos de la base de conocimiento
    v_hechos = {h: h[0] != '-' for h in hechos}
    # Asignar valores a los hechos de la base de reglas
    for r in reglas:
        # Recorrer cada regla
        for i in r:
            j = 0
            bandera = True
            # Recorrer cada hecho de la regla
            for a in i:
                # Si la variable bandera es falsa, se asigna el valor True
                if not bandera:
                    bandera = True
                # Si el hecho no es un operador lógico, se evalúa si ya existe en el diccionario
                elif a != '&' and a != '|':
                    if a not in v_hechos:
                        # Se verifica si el hecho es negado
                        if a == "-":
                            # Se crea el hecho negado
                            b = a + i[j + 1]
                            # Se verifica si el hecho negado ya existe en el diccionario
                            if b not in v_hechos:
                                bandera = False
                                v_hechos[b] = True
                        # Si el hecho no es negado, se asigna el valor False al hecho y se agrega al diccionario
                        else:
                            v_hechos[a] = False
                j += 1


# Función para realizar el algoritmo de inferencia forward chaining
def algoritmo_foward_chaining():
    global v_hechos
    global hechos
    global reglas

    # Recorrer cada regla
    for r in reglas:
        # En este caso, la regla se puede evaluar si solo tiene operadores de conjunción (&, AND)
        if "|" not in r[0]:
            evaluar_reglas(r)
    # Recorrer cada regla en caso de que la regla tenga el operador lógico de disyunción (|, OR)
    for r in reglas:
        evaluar_reglas(r)


# Función para evaluar una regla con operadores lógicos AND y OR
def evaluar_reglas(r):
    aux = list()
    # Si la regla se puede evaluar, se agrega el hecho a la base de hechos
    if probar_and_or(r):
        hecho = r[1][0]
        # Se asigna el valor True al hecho en el diccionario de hechos
        hechos.append(hecho)
        v_hechos[hecho] = True
        # Se agrega la regla a la lista de reglas utilizadas
        reglas_utilizadas.append(r)
        print("\nRegla utilizada: ", end=" ")
        aux.append(r)
        mostrar_reglas(aux)
        # Se elimina la regla utilizada de la lista de reglas
        reglas.remove(r)
        print("Reglas restantes: ")
        mostrar_reglas(reglas)
        print("Base de Hechos: ", hechos)
        # Se llama a la función recursivamente para evaluar las reglas restantes
        algoritmo_foward_chaining()


# Función para evaluar una regla con operadores lógicos AND y OR
def probar_and_or(r):
    global v_hechos
    i = 0
    resultado = ""
    evaluar = True

    # Recorrer cada hecho de la regla
    for a in r[0]:
        if not evaluar:
            evaluar = True
        else:
            if a[0] == '-':
                evaluar = False
                # Se crea el hecho negado a partir del hecho actual (-) y el siguiente hecho
                h = a + r[0][i + 1]
                # Se agrega el hecho negado a la variable resultado que corresponde a la regla a evaluar
                resultado = resultado + str(v_hechos[h])
            # Si el hecho no es negado y no es un operador lógico, se agrega el hecho a la variable resultado
            elif a[0] != '-' and a != '&' and a != '|':
                resultado = resultado + str(v_hechos[a])
            # Si el hecho es el operador lógico AND, se agrega el operador AND a la variable resultado
            if a == '&':
                resultado = resultado + " and "
            # Si el hecho es el operador lógico OR, se agrega el operador OR a la variable resultado
            if a == '|':
                resultado = resultado + " or "
        i += 1
    # Se evalúa la regla y se retorna el resultado de la evaluación de la regla
    return eval(resultado)


# Función para mostrar las reglas utilizadas en el formato de lógica proposicional
def mostrar_reglas(lista_reglas):
    hay_guion = False
    # Recorrer cada regla
    for a in lista_reglas:
        # Se crea la variable regla que corresponde a la regla a mostrar
        regla = ""
        # Recorrer cada hecho de la regla
        for letra in a[0]:
            if letra == "-":
                regla += " " + letra
                hay_guion = True
            elif hay_guion:
                regla += letra
                hay_guion = False
            else:
                regla += " " + letra
                hay_guion = False
        for letra in a[1]:
            regla += " => " + letra
        print(regla.strip())


# Función principal
def main():
    leer_reglas("reglas.txt")
    asignar_valores_hechos()
    algoritmo_foward_chaining()
    print("\n\nBase de hechos: ", hechos)
    print("Reglas utilizadas: ")
    mostrar_reglas(reglas_utilizadas)


# Ejecutar el programa
if __name__ == '__main__':
    main()
