import libreria24validaciones

numeroDeEntrada = input("Ingresa el ISBN : ")
if libreria24validaciones.validar_isbn(numeroDeEntrada):
    print("El ISBN es válido.")
else:
    print("El ISBN no es válido.")  
numeroDni = int(input("Ingresa el número del DNI (sin letra): "))
letraCalculada = libreria24validaciones.letraDni(numeroDni)
print("La letra correspondiente al DNI es: " + letraCalculada)
print("EL DNI completo es : " + str(numeroDni) + letraCalculada)

numeroDniconLetra = input("Ingresa el DNI con letra (ejemplo: 12345678Z): ")
if libreria24validaciones.validar_dni(numeroDniconLetra):
    print("El DNI es válido.")
else:
    print("El DNI no es válido.")   
