Datos = input("Inserta los datos de la cadena: ")
print(Datos)
orden = []
for dato in Datos:
    if(dato not in orden):
        orden.append(dato)
print(orden)