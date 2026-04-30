# 1. Definir catálogo como tupla de tuplas
catalogo = (
    ("Inception", "Christopher Nolan", 2010, 9.0),
    ("Interstellar", "Christopher Nolan", 2014, 8.6),
    ("Parasite", "Bong Joon-ho", 2019, 8.6),
    ("The Godfather", "Francis Ford Coppola", 1972, 9.2)
)

# 2. Desempaquetar cada película en un bucle
print("Catálogo de películas:\n")
for titulo, director, anio, puntuacion in catalogo:
    print(f"{titulo} ({anio}) - Dir: {director} - Puntuación: {puntuacion}")

# 3. Usar operador * para separar primera del resto
primera, *resto = catalogo
print("\nPrimera película:")
print(primera)

print("\nResto de películas:")
print(resto)

# 4. Buscar por director
def buscar_por_director(director_busqueda):
    resultados = ()
    for pelicula in catalogo:
        if pelicula[1] == director_busqueda:
            resultados = resultados + (pelicula,)
    return resultados

# 5. Obtener estadísticas
def obtener_estadisticas():
    puntuaciones = ()
    
    for pelicula in catalogo:
        puntuaciones = puntuaciones + (pelicula[3],)
    
    minimo = min(puntuaciones)
    maximo = max(puntuaciones)
    promedio = sum(puntuaciones) / len(puntuaciones)
    
    return minimo, maximo, promedio

# --- PRUEBAS ---

# Buscar películas de un director
print("\nPelículas de Christopher Nolan:")
resultado = buscar_por_director("Christopher Nolan")
for peli in resultado:
    print(peli)

# 6. Desempaquetar estadísticas
minimo, maximo, promedio = obtener_estadisticas()

print("\nEstadísticas de puntuación:")
print(f"Mínima: {minimo}")
print(f"Máxima: {maximo}")
print(f"Promedio: {promedio:.2f}")