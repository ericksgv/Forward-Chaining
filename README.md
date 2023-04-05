# Forward-Chaining
Implementación del algoritmo de inferencia forward chaining

Este código es una implementación del algoritmo de inferencia forward chaining, haciendo uso de hechos atómicos.

El archivo reglas.txt contiene las reglas lógicas que se utilizarán en el algoritmo. Cada regla está escrita en una línea separada y tiene la siguiente estructura:

antecedentes => consecuentes

Los antecedentes y consecuentes están separados por el símbolo "=>" que representa la implicación lógica. Los antecedentes contienen hechos de forma, y operadores lógicos "&" (AND o conjunción) y "|" (OR o disyunción) que permiten combinar esos hechos. Los consecuentes corresponden a un hecho en forma atómica.

Además, el archivo reglas.txt también contiene una línea que comienza con el símbolo "#" que indica la lista de hechos (en forma atómica) iniciales. Esta línea se puede escribir de la siguiente manera:

#hecho1,hecho2,hecho3,...
