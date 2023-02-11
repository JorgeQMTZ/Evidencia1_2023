contactos = {}
salir = False
while (not salir):
    nombre=input("Nombre: ")
    telefono=int(input("Telefono: "))
    if(nombre not in contactos):
        contactos[nombre] = telefono
        print('El contacto se añadio correctamente')
    else:
        print('Error (Contacto duplicado)')
    respuesta = input("Para salir, ingresa el numero 1, para agregar otro contacto presiona solo enter: ")
    if(respuesta == "1"):
        salir = True        
print("Tu agenda completa es: ")
print(contactos)