texto = "primero pYthon"
print("upper ", texto.upper())
print("lower ", texto.lower())
print("replace ", texto.replace("o", "@"))
print("letra[0] ", texto[0])
print("longitud ", len(texto))
print("find(p): ", texto.find("p"))
print("find(z): ", texto.find("z"))
#SOBRE CARGA DE UN METODO
print("find(p,index): ", texto.find("p",1))
print("rfind(p): ", texto.rfind("p"))
print("startswith a: ", texto.startswith("a"))
print("isdigit(): ", texto.isdigit())
print("isalpha() ", texto.isalpha())
print("isalnum() ", texto.isalnum()) #letras y numeros
#Probamos SLICING, llamdo substring
subcadena = texto[2: 5]
print("texto[2: 5] ", subcadena)

for i in range(len(texto)):
    print(texto[i])

for i in range(0,len(texto)):
    print(texto[i], end='')




    


      
