#Una clase que no hereda de otra se le dice Primitiva String, Numbers, Lista
class Person():
    #atributos
    name = ""
    all_users = [] # Lista de todos los usuarios

    #Methods

    #constructor #self instancia -> tipo de Method + publicos, privados -> class , staticos, clase
    def __init__(self, name):
        #conteo autogenerado
        self.id = len(self.__class__.all_users) + 1
        #construye
        self.name = name
        #siempre existe
        self.friends = [] 
        #agrega a la nueva persona a lista de usuarios
        self.__class__.all_users.append(self)

    #Funcion que agrega amigos a una instancia
    def addFriend(self, new_friend):
        #agrega un amigo a la lista
        self.friends.append(new_friend)
        return True

    # funcion que muestra amigos de una persona
    # JSON <-
    # /endpoints 
    # JS <- 2.000.000
    # 6kb           #2.3MB
    # 200 <- API <- 2.000.000

    def get_friends(self):
        return [ friend.id for friend in self.friends ]

    def __repr__(self) -> str:
        return self.name

    @classmethod
    def get_all_users(cls):
        return [ friend for friend in cls.all_users ]

#instancia de Oscar y de Andres
oscar = Person('Oscar Alvarez 🎈')
andres = Person('Andres Betancourt 🙂')

juan_carlos = Person('Juan Carlos Cabrera ⚾')
juan_carlos_delfin = Person('Juan Carlos Delfin 🐬')

julio = Person('Julio Blando 😂')

#funcion agregar amigos
julio.addFriend(oscar)

julio.addFriend(andres)


#Recomendados(julio) -> Oscar -> Andres 😎

#Clase
print(Person.get_all_users())

#print(oscar)
#print(andres)



