# Ejemplo de uso de listas y tuplas en Python
listanombres = ["Ana", "Luis", "Carlos", "Marta"]
listaprecios = [3,5,7,11,2,9,88]
listaprecios.sort()
print(listaprecios)
listaprecios.sort(reverse=True)
print(listaprecios)

for i in range(len(listaprecios)):
    print(f"El número en la posición {i} es {listaprecios[i]}")

print(listanombres)
print("Nombre[0]: ", listanombres[0])
print("Nombre[1]: ", listanombres[1])   
print("Nombre[2]: ", listanombres[2])
print("Nombres[3]: ", listanombres[3])

listanombres.append("Sofía")
print("Después de agregar un nombre:", listanombres)
listanombres.insert(2, "Jorge")
print("Después de insertar un nombre en la posición 2:", listanombres)
listanombres.remove("Luis")
print("Después de eliminar un nombre:", listanombres)
listanombres.pop()
print("Después de eliminar el último nombre:", listanombres)
listanombres.pop(0)
print("Después de eliminar el nombre en la posición 0:", listanombres)
del listanombres[0:2]
print("Después de eliminar los dos primeros nombres:", listanombres)
respuesta = "Carlos" in listanombres
print("¿Está Carlos en la lista?", respuesta)
respuesta = "Marta" in listanombres
print("¿Está Marta en la lista?", respuesta)


listanombres = ["Ana", "Luis", "Carlos", "Marta"]
listaprecios = [3,5,7,11,2,9,88]

print(listanombres)
print(listaprecios)
listacombinada = list(zip(listanombres, listaprecios))
print("Lista combinada de nombres y precios:")
for nombre, precio in listacombinada:
    print(f"Nombre: {nombre}, Precio: {precio}")
listanombres.clear()
print("Lista de nombres después de clear():", listanombres)

# Uso de tuplas para representar productos

tuplaProducto1 = ("Televisor", 4500, "Electrónica")
tuplaProducto2 = ("Lavadora", 3200, "Electrodomésticos")
tuplaProducto3 = ("Microondas", 1200, "Electrodomésticos")
listatuplas = [tuplaProducto1, tuplaProducto2, tuplaProducto3]
print("\nLista de productos con sus detalles:")
for producto in listatuplas:
    nombre, precio, categoria = producto
    print(f"Producto: {nombre}, Precio: {precio}, Categoría: {categoria}")  

listatuplas.append(("Celular", 2500, "Electrónica"))
print("\nLista después de agregar un nuevo producto:")
for producto in listatuplas:
    nombre, precio, categoria = producto
    print(f"Producto: {nombre}, Precio: {precio}, Categoría: {categoria}")



