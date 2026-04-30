# 1. Definir ventas_por_region (dict anidado)
ventas_por_region = {
    "Norte": {"Q1": 1500, "Q2": 2000, "Q3": 1800, "Q4": 2200},
    "Sur":   {"Q1": 1200, "Q2": 1700, "Q3": 1600, "Q4": 2100},
    "Este":  {"Q1": 1000, "Q2": 1500, "Q3": 1400, "Q4": 1900},
    "Oeste": {"Q1": 1300, "Q2": 1600, "Q3": 1700, "Q4": 2000}
}

# 2. Total anual por región
totales_region = {}
for region, ventas in ventas_por_region.items():
    totales_region[region] = sum(ventas.values())

# 3. Región con mayores ventas
region_max = max(totales_region, key=lambda r: totales_region[r])

# 4. Acumular ventas por trimestre
ventas_trimestres = {"Q1": 0, "Q2": 0, "Q3": 0, "Q4": 0}

for ventas in ventas_por_region.values():
    for trimestre, valor in ventas.items():
        ventas_trimestres[trimestre] += valor

# 5. Porcentajes sobre el total global
gran_total = sum(totales_region.values())

porcentajes = {
    region: round((total / gran_total) * 100, 2)
    for region, total in totales_region.items()
}

# 6. Reporte ordenado (mayor a menor)
print("REPORTE DE VENTAS POR REGIÓN\n")

for region, total in sorted(totales_region.items(), key=lambda x: x[1], reverse=True):
    print(f"{region}: {total} ({porcentajes[region]}%)")

print("\nRegión con mayores ventas:", region_max)

print("\nVentas por trimestre:")
for t, total in ventas_trimestres.items():
    print(f"{t}: {total}")