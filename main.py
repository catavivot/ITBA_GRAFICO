#---------------------------ARCHIVO PRINCIPAL PARA LA EJECUCIÓN DEL PROGRAMA---------------------#
#Archivo principal del programa
import responsabilidad_base_datos.base_datos as db
import funcionalidad_pantallas.Menu_principal as mp

if __name__ == '__main__':
    #Se crea la base de datos   
    db.creacionDB()
    #Abro menú principal
    mp
