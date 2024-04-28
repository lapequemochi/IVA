from enum import Enum
"""-----------
#Enumeraciones
-----------"""
class Tipo(Enum):

    PAPELERIA = 1
    SUPERMERCADO = 2
    FARMACIA = 3
    
class Producto:
    
    """-------------------
    #Constantes
    -----------------"""
    __IVA_SUPERMERCADO = 0.04
    __IVA_PAPELERIA = 0.16
    __IVA_FARMACIA = 0.12
    
    

    """-----------------------
    Metodos
    --------------------------"""

    def __init__ (self, tipo,pNombre,pValorUnitario, pCantidadBodega, pCantidadMinima,pCantidadUnidadesVendidas):
        self.__tipo=tipo
        self.__nombre=pNombre
        self.__valorUnitario=pValorUnitario
        self.__cantidadBodega=pCantidadBodega
        self.__cantidadMinima=pCantidadMinima
        self.__cantidadUnidadesVendidas = 0

    def getNombre(self):
        return self.__nombre

    def getTipo(self):
        return self.__getTipo

    def getValorUnitario(self):
        return self.__valorUnitario

    def getCantidadBodega(self):
        return self.__cantidadBodega

    def getCantidadMinima(self):
        return self.__cantidadMinima
    
    def getCantidadesUnidadesVendidas(self):
        return self.__cantidadUnidadesVendidas

    def setNombre(self,nombre):
        self.__nombre = nombre
        
    def setTipo(self, tipo):
        self.__tipo = tipo
        
    def setValorUnitario(self, valorUnitario):
        self.__valorUnitario = valorUnitario

    def setCantidadBodega(self, cantidadBodega):
        self.__cantidadBodega = cantidadBodega
        
    def setCantidadMinima(self, cantidadMinima):
        self.__cantidadMinima = cantidadMinima        

    def setCantidadUnidadesVendidas(self, cantidadUnidadesVendidas):
        self.__cantidadUnidadesVendidas = cantidadUnidadesVendidas

    def Vender(self, cantidad):
        if cantidad <= self.__cantidadBodega:
            self.__cantidadUnidadesVendidas += cantidad
            self.__cantidadBodega -= cantidad
        else:
            print("Cantidad no disponible")
    
    def Hay_Suficiente(self, cantidad):
        if cantidad <= self.__cantidadBodega:
            return True
        else:
            return False
        #Forma 2
        Hay_Suficiente= False
        if cantidad <= self.__cantidadBodega:
            Hay_Suficiente = True
            return Hay_Suficiente
        
        #Forma 3
            return cantidad <= self.__cantidadBodega
        
    def DarIva(self):
        if(self.__tipo=="PAPELERIA"):
            return self.__IVA_PAPELERIA
        elif(self.__tipo=="FARMACIA"):
            return self.__IVA_FARMACIA
        elif(self.__tipo=="SUPERMERCADO"):
            return self.__IVA_SUPERMERCADO
        else:
            print("Categoria de producto no existe")

    def subirValorUnitario(self):
        if(self.__valorUnitario < 1000):
            self.__valorUnitario+=0.05
        elif(self.__valorUnitario > 1000 and self.__valorUnitario < 5000):
            self.__valorUnitario+=0.02
        elif(self.__valorUnitario > 5000):
            self.__valorUnitario+=0.03
    
    def HacerPedido(self, cantidad):
        if(self.__cantidadBodega < self.__cantidadMinima):
            self.__cantidadBodega += cantidad
        else:
            print("No se hace nada")

    def cambiarValorUnitario(self):
        if(self.__valorUnitario == (self.__tipo=='PAPELERIA') and (self.__tipo=='DROGUERIA')):
            self.__valorUnitario-=0.1
        
        elif(self.__valorUnitario ==(self.__tipo=='SUPERMERCADO')):
            self.__valorUnitario+=0.05
            
    def __init__(self,nombre,tipo,valorUnitario):
        self.nombre = nombre
        self.tipo = tipo
        self.valorUnitario = valorUnitario
        
    def nombreTipoProducto(self):
        if self.tipo == "Supermercado":
            return "El producto es de supermercado"
  
        elif self.tipo == "Drogueria":
            return "El producto es de drogueria"
        
        elif self.tipo == "Papeleria":
            return "El producto es de papeleria"    

        else: 
            return "Tipo de producto desconocido"
        
    def aumentarValorUnitario(self):
        if self.tipo == "Drogueria":
            self.valorUnitario *= 0.01 
        
        elif self.tipo == "Supermercado":
            self.valorUnitario *= 0.03
            
        elif self.tipo == "Papeleria":
            self.valorUnitario *= 0.02
         
