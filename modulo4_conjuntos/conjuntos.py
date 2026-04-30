# 1. Definir tiendas como sets
tienda_centro = {"laptop", "mouse", "teclado", "monitor"}
tienda_norte  = {"tablet", "mouse", "audifonos", "monitor"}
tienda_sur    = {"laptop", "impresora", "teclado", "camara"}

# 2. Catálogo completo y productos comunes
catalogo_completo = tienda_centro.union(tienda_norte).union(tienda_sur)
productos_comunes = tienda_centro.intersection(tienda_norte).intersection(tienda_sur)

# 3. Exclusivos y solapamientos
exclusivos_centro = tienda_centro.difference(tienda_norte).difference(tienda_sur)
exclusivos_norte  = tienda_norte.difference(tienda_centro).difference(tienda_sur)
exclusivos_sur    = tienda_sur.difference(tienda_centro).difference(tienda_norte)

# Verificar si no hay elementos en común entre dos tiendas
sin_solapamiento = tienda_centro.isdisjoint(tienda_sur)

# 4. Usuarios con géneros
usuario1 = {"accion", "comedia", "drama"}
usuario2 = {"comedia", "terror", "drama"}
usuario3 = {"accion", "fantasia", "ciencia ficcion"}

# 5. Operadores matemáticos
comunes_usuarios = usuario1 & usuario2 & usuario3
universo_generos = usuario1 | usuario2 | usuario3
exclusivos_u1 = usuario1 - usuario2 - usuario3
dif_simetrica = usuario2 ^ usuario3

# 6. Verificar subconjunto
es_subconjunto = {"accion", "comedia"} <= usuario1

# --- REPORTE FINAL ---

print("=== TIENDAS ===")
print("Catálogo completo:", catalogo_completo)
print("Productos comunes en TODAS:", productos_comunes)

print("\nExclusivos:")
print("Centro:", exclusivos_centro)
print("Norte:", exclusivos_norte)
print("Sur:", exclusivos_sur)

print("\nCentro y Sur sin productos en común?:", sin_solapamiento)

print("\n=== USUARIOS ===")
print("Géneros comunes:", comunes_usuarios)
print("Todos los géneros:", universo_generos)
print("Exclusivos usuario1:", exclusivos_u1)
print("Diferencia simétrica (u2 ^ u3):", dif_simetrica)

print("\nSubconjunto {'accion','comedia'} en usuario1?:", es_subconjunto)