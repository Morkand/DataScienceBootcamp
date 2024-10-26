ventas = [
    {"fecha": "2024-10-01", "producto": "Manzanas", "cantidad": 10, "precio": 1.2},
    {"fecha": "2024-10-01", "producto": "Naranjas", "cantidad": 5, "precio": 0.8},
    {"fecha": "2024-11-02", "producto": "Manzanas", "cantidad": 3, "precio": 1.3},
    {"fecha": "2024-11-02", "producto": "Plátanos", "cantidad": 7, "precio": 0.5},
    {"fecha": "2024-11-03", "producto": "Naranjas", "cantidad": 8, "precio": 0.9},
]

ingresos_totales = 0
for venta in ventas:
    ingresos_totales += venta["cantidad"] * venta["precio"]

print("Ingresos Totales:", ingresos_totales)

ventas_por_producto = {}

for venta in ventas:
    producto = venta["producto"]
    if producto in ventas_por_producto:
        ventas_por_producto[producto] += venta["cantidad"]
    else:
        ventas_por_producto[producto] = venta["cantidad"]

# Encontrar el producto más vendido
producto_mas_vendido = max(ventas_por_producto, key=ventas_por_producto.get)
print("Producto más vendido:", producto_mas_vendido)

precios_por_producto = {}

for venta in ventas:
    producto = venta["producto"]
    if producto in precios_por_producto:
        suma_precios, cantidad_vendida = precios_por_producto[producto]
        precios_por_producto[producto] = (suma_precios + venta["precio"] * venta["cantidad"], cantidad_vendida + venta["cantidad"])
    else:
        precios_por_producto[producto] = (venta["precio"] * venta["cantidad"], venta["cantidad"])

# Calcular el precio promedio por producto
precios_promedio = {}
for producto, (suma_precios, cantidad_vendida) in precios_por_producto.items():
    precios_promedio[producto] = suma_precios / cantidad_vendida

print("Precios Promedio:", precios_promedio)

ingresos_por_dia = {}

for venta in ventas:
    fecha = venta["fecha"]
    ingresos = venta["cantidad"] * venta["precio"]
    if fecha in ingresos_por_dia:
        ingresos_por_dia[fecha] += ingresos
    else:
        ingresos_por_dia[fecha] = ingresos

print("Ingresos por día:", ingresos_por_dia)

resumen_ventas = {}

for producto in ventas_por_producto:
    cantidad_total = ventas_por_producto[producto]
    ingresos_totales_producto = precios_por_producto[producto][0]
    precio_promedio_producto = precios_promedio[producto]

    resumen_ventas[producto] = {
        "cantidad_total": cantidad_total,
        "ingresos_totales": ingresos_totales_producto,
        "precio_promedio": precio_promedio_producto
    }

# Mostrar resumen de ventas
for producto, datos in resumen_ventas.items():
    print(f"{producto}: {datos}")
