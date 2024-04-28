from Producto import Producto

class Tienda:
    
    def ejemplo(self):
        return Producto.PRECIO_MAXIMO
    
    """-------------
    #Atributos
    ----------------"""
    __producto1 = None
    __producto2 =  None
    __producto3 = None
    __producto4 = None
    __dinero_en_caja = 0.0
     
    #Import
    __producto1=Producto
    __producto2=Producto
    __producto3=Producto
    __producto4=Producto
    
    """-------------
    #Metodos
    ----------------"""
    def getProducto1(self):
        return self.__producto1
    def getProducto2(self):
        return self.__producto2
    def getProducto3(self):
        return self.__producto3
    def getProducto4(self):
        return self.__producto4
    
    def __producto1(self):
        return self.__producto1
    def __producto2(self):
        return self.__producto2
    def __producto3(self):
        return self.__producto3
    def __producto1(self):
        return self.__producto1
    
    def __init__(self):
        self.__producto1 = Producto("Papeleria", "Lapiz", 55.0, 30, 9)
        self.__producto2 = Producto("Papeleria", "Borrador", 55.0, 15, 5)
        self.__producto3 = Producto("Supermercado", "Cafe", 55.0, 20, 10)
        self.__producto4 = Producto("Drogueria", "Desinfectante", 55.0, 12, 11)
        self.dineroEnCaja = 0


    def VenderProducto(self,nombre,cantidad):
        if cantidad <= self.__cantidadBodega:
            self.__cantidadUnidadesVendidas += cantidad
            self.__cantidadBodega -= cantidad
        elif self.nombre <= self.__cantidadBodega:
            self.__cantidadUnidadesVendidas += nombre
            self.__cantidadBodega -= nombre
        else: 
            print("Categoria ")
            
    def CuantosPapeleria(self):
        if self.__producto1.__getTipo == "Papeleria":
            return self.__producto1.__getTipo
        elif self.__producto2.__getTipo == "Papeleria":
            return self.__producto2.__getTipo 
        elif self.__producto3.__getTipo == "Supermercado":
            return self.__producto3.__getTipo 
        elif self.__producto4.__getTipo == "Drogueria":
            return self.__producto4.__getTipo
        else:
            print("Categoria no soportada")
            
    def darPrecioProducto(self, pNumeroProducto):
        if pNumeroProducto == 1:
            return self.producto1.valorUnitario
        elif pNumeroProducto == 2:
            return self.producto2.valorUnitario
        elif pNumeroProducto == 3:
            return self.producto3.valorUnitario
        elif pNumeroProducto == 4:
            return self.producto4.valorUnitario
        else:
            return "Producto no encontrado"
        
    def darPrecioProductoPorNombre(self, pNombreProducto):
        if pNombreProducto == self.producto1.nombre:
            return self.producto1.valorUnitario
        elif pNombreProducto == self.producto2.nombre:
            return self.producto2.valorUnitario
        elif pNombreProducto == self.producto3.nombre:
            return self.producto3.valorUnitario
        elif pNombreProducto == self.producto4.nombre:
            return self.producto4.valorUnitario
        else:
            return "Producto no encontrado"