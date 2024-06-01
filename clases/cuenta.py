class Cuenta:
    ### Constructor
    def __init__(self, nombre, cantidad, numero, clave, estado):
        self.nombre = nombre
        self.cantidad = cantidad
        self.numero = numero
        self.clave = clave
        self.estado = estado
        
    def sacarDinero (self, sacar):
        if sacar <= self.cantidad:
            self.cantidad -= sacar
            print("Operacion realizada con exito")
        else:
            print("No tiene suficiente dinero, su dinero actual es de: " + self.cantidad)
        
    def ingresarDinero (self, ingreso):
        self.cantidad += ingreso
        print("Se ha efectuado el ingreso de " + str(ingreso) + "$")
        
    def getDatos(self):
        print('''
        Nombre: ''' + self.nombre + '''
        Numero de Cuenta: ''' + self.numero + '''
        Cantidad: ''' +str(self.cantidad) + '''
        Estado: ''' + str(self.estado) + '''
        ''') 