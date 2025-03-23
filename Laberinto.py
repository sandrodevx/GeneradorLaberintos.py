import random

# Configuración del laberinto
FILAS = 10
COLUMNAS = 10

# Direcciones para moverse en la cuadrícula
DIRECCIONES = [('N', -1, 0), ('S', 1, 0), ('E', 0, 1), ('O', 0, -1)]

def crear_laberinto(filas, columnas):
    # Inicializar el laberinto con todas las paredes activadas
    laberinto = [[{'N': True, 'S': True, 'E': True, 'O': True} for _ in range(columnas)] for _ in range(filas)]
    
    # Marcar todas las celdas como no visitadas
    visitado = [[False for _ in range(columnas)] for _ in range(filas)]
    
    # Función para verificar si una celda está dentro de los límites del laberinto
    def es_valida(fila, columna):
        return 0 <= fila < filas and 0 <= columna < columnas
    
    # Función recursiva para generar el laberinto usando DFS
    def dfs(fila, columna):
        visitado[fila][columna] = True
        random.shuffle(DIRECCIONES)  # Mezclar direcciones para aleatoriedad
        
        for direccion, df, dc in DIRECCIONES:
            nueva_fila, nueva_columna = fila + df, columna + dc
            if es_valida(nueva_fila, nueva_columna) and not visitado[nueva_fila][nueva_columna]:
                # Eliminar la pared entre la celda actual y la nueva celda
                if direccion == 'N':
                    laberinto[fila][columna]['N'] = False
                    laberinto[nueva_fila][nueva_columna]['S'] = False
                elif direccion == 'S':
                    laberinto[fila][columna]['S'] = False
                    laberinto[nueva_fila][nueva_columna]['N'] = False
                elif direccion == 'E':
                    laberinto[fila][columna]['E'] = False
                    laberinto[nueva_fila][nueva_columna]['O'] = False
                elif direccion == 'O':
                    laberinto[fila][columna]['O'] = False
                    laberinto[nueva_fila][nueva_columna]['E'] = False
                
                # Llamar a DFS recursivamente
                dfs(nueva_fila, nueva_columna)
    
    # Empezar desde una celda aleatoria
    inicio_fila, inicio_columna = random.randint(0, filas - 1), random.randint(0, columnas - 1)
    dfs(inicio_fila, inicio_columna)
    
    return laberinto

def imprimir_laberinto(laberinto):
    for fila in laberinto:
        for celda in fila:
            if celda['N']:
                print("+---", end="")
            else:
                print("+   ", end="")
        print("+")
        for celda in fila:
            if celda['O']:
                print("|   ", end="")
            else:
                print("    ", end="")
        print("|")
    print("+---" * len(laberinto[0]) + "+")

# Generar y mostrar el laberinto
laberinto = crear_laberinto(FILAS, COLUMNAS)
imprimir_laberinto(laberinto)