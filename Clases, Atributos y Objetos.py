#Crear 2 clases con 3 atributos y 2 objetos (no es necesario relacionarlas)

class Autos: #Creamo la clase que son autos
    def __init__(self, marca, modelo, tipo): #"init" juega un papel pues es el constructor o lo que daría forma... el esqueleto puede decirse o a lo que entendí
        
        #Agregamos atributos o mejor dicho sus caracteristicas
        #"self." es para definir la caracteristica que vamos a utilizar
        self.marca = marca
        self.modelo = modelo
        self.tipo = tipo

#Definimos los objetos o bueno al objeto le damos sus atributos

Auto_1 = Autos("Nissan", "X-Trail", "Electrico") #Ponemos el primer objeto y para darle su definicion debemos llamar a la clase del donde viene, en este caso es la clase Autos
Auto_2 = Autos("Toyota", "Corolla", "Gasolina") #Lo mismo que el objeto 1 pero en el numero 2

print("Lista de autos")
print("Auto 1: ",{Auto_1.marca}," ",{Auto_1.modelo}," ",{Auto_1.tipo}) #Para imprimir el resultado mandamos a llamar al objeto y su atributo
print("Auto 2: ",{Auto_2.marca}," ",{Auto_2.modelo}," ",{Auto_2.tipo})



#Ahora con una lista de animales y su tipo

class Animales:
    def __init__(self, nombre, tipo, mortal):

        self.nombre = nombre
        self.tipo = tipo
        self. mortal = mortal

Animal_1 = Animales("Paloma", "Aereo", "No")
Animal_2 = Animales("Tiburon", "Acuatico", "Si")

print("\nLista de animales")
print("Animal 1: ",{Animal_1.nombre}," ",{Animal_1.tipo},", Te puede matar?",{Animal_1.mortal})
print("Animal 2: ",{Animal_2.nombre}," ",{Animal_2.tipo},", Te puede matar?",{Animal_2.mortal})