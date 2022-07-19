class Usuario:
    def __init__ (self,id="0955453741",nom="Damaris Ortiz",dir="Milagro",tel="0969188296",correo="jhgttvgg"):
        self.id = id
        self.nombre = nom
        self.direccion = dir
        self.telefono = tel
        self.correo = correo

    def mostrarUsuario(self):
        return ("Usuario: {} {} {} {} {}".format(self.id,self.nombre,self.direccion,self.telefono,self.correo))




usua1 = Usuario("0988755343","Marcos Perez","Salinas","0987654321","marcosp@gmail.com")
usua2 = Usuario("1301119087","Maria Salvatierra","Montañita","0967543292","mariasalva@gmail.com")
usua3 = Usuario("1308765787","Armando Casas","Playas","0987665337","armacasas@gmail.com")
print(usua1)
print(usua2)
print(usua3)