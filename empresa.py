class Empresa:
    def __init__(self,ruc,nombre,tel,dir,correo):
        self.ruc=ruc
        self.razonsocial=nombre
        self.tel=tel
        self.dir=dir
        self.correo=correo

if __name__ == '__main__':
    emp1 = Empresa("0988755343","Security","0969188908","Milagro","epardos@unemi.edu.ec")
    print(emp1.ruc,emp1.razonsocial)