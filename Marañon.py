class Marañon:
    
    def __init__(self):
        self.__nombre=None
        self.__catidad=None
        self.__precio=None
        self.__vitaminaAportada=None
    
    
    
    @property    
    def vitaminaAportada(self):
        return self.__vitaminaAportada
    #declrando el metodo ser(confihguro/llevo un valor a un atrubuto)
    @vitaminaAportada.setter
    def vitaminaAportada(self,dato):
        self.__vitaminaAportada=dato
    
     
    @property    
    def precio(self):
        return self.__precio
    #declrando el metodo ser(confihguro/llevo un valor a un atrubuto)
    @precio.setter
    def precio(self,dato):
        self.__precio=dato   
    
    @property    
    def catidad(self):
        return self.__catidad
    #declrando el metodo ser(confihguro/llevo un valor a un atrubuto)
    @catidad.setter
    def catidad(self,dato):
        self.__catidad=dato
        
    

        #DECLARAN EL METODO GET (OBTEGO/MUESTRO UN ATRUBURO)
    @property    
    def nombre(self):
        return self.__nombre
    #declrando el metodo ser(confihguro/llevo un valor a un atrubuto)
    @nombre.setter
    def nombre(self,dato):
        self.__nombre=dato
        
    def agregarFruta(self):
        print("Se pica y se macera con azucar morena...")