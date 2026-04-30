# Dataset de ventas
ventas = [
    {"producto": "laptop",  "categoria": "tecnologia", "unidades": 20, "precio": 800},
    {"producto": "teclado", "categoria": "tecnologia", "unidades": 50, "precio": 25},
    {"producto": "mouse",   "categoria": "tecnologia", "unidades": 30, "precio": 15},
    {"producto": "monitor", "categoria": "tecnologia", "unidades": 10, "precio": 200},
    {"producto": "silla",   "categoria": "hogar",      "unidades": 15, "precio": 120},
]

# 1. List comp: valor_total por producto
valor_total = [v["unidades"] * v["precio"] for v in ventas]

# 2. List comp con filtro: productos con valor_total > 1000
alto_valor = [
    v["producto"]
    for v in ventas
    if v["unidades"] * v["precio"] > 1000
]

# 3. Dict comp: nombre → {valor, unidades}
producto_info = {
    v["producto"]: {
        "valor": v["unidades"] * v["precio"],
        "unidades": v["unidades"]
    }
    for v in ventas
}

# 4. Dict comp con filtro: ranking premium (precio > 50)
ranking_premium = {
    v["producto"]: v["unidades"] * v["precio"]
    for v in ventas
    if v["precio"] > 50
}

# Ordenar ranking (esto ya usa sorted como apoyo)
ranking_premium = dict(
    sorted(ranking_premium.items(), key=lambda x: x[1], reverse=True)
)

# 5. Set comp
categorias_unicas = {v["categoria"] for v in ventas}
productos_baratos = {v["producto"] for v in ventas if v["precio"] <= 50}

# 6. Combinar todo
resumen_formateado = [
    f"{v['producto']}: {v['unidades']} unidades → ${v['unidades'] * v['precio']}"
    for v in ventas
]

gran_total = sum(valor_total)

# --- REPORTE FINAL ---
print("VALOR TOTAL:", valor_total)
print("\nPRODUCTOS DE ALTO VALOR:", alto_valor)
print("\nINFO PRODUCTOS:", producto_info)
print("\nRANKING PREMIUM:", ranking_premium)
print("\nCATEGORÍAS ÚNICAS:", categorias_unicas)
print("\nPRODUCTOS BARATOS:", productos_baratos)
print("\nRESUMEN:")
for r in resumen_formateado:
    print(r)

print("\nGRAN TOTAL:", gran_total)