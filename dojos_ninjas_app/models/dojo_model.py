from dojos_ninjas_app.config.mysqlconnection import connectToMySQL

class Dojo:
    def __init__(self, data):
        self.id = data['id']
        self.nombre = data['nombre']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']


    #METODO PARA CREAR
    @classmethod
    def crear_un_dojo(cls, data):
        query = "INSERT INTO dojos (nombre) VALUES (%(name)s);"
        resultado = connectToMySQL('esquema_dojos_y_ninjas').query_db(query, data)
        return resultado


    #METODOS DE LECTURA
    @classmethod
    def mostrar_dojos(cls):
        query = "SELECT * FROM dojos;"
        resultado = connectToMySQL('esquema_dojos_y_ninjas').query_db(query) #es una lista de diccionarios
        dojos_lista = []
        for i in resultado:
            dojos_lista.append(cls(i))
        return dojos_lista
    

    @classmethod
    def obtener_un_dojo(cls, data):
        query = "SELECT * FROM dojos WHERE id = %(id)s;"
        resultado = connectToMySQL('esquema_dojos_y_ninjas').query_db(query, data)
        return cls(resultado[0])


    @classmethod
    def mostrar_ninjas_del_dojo(cls, data):
        query = "SELECT * FROM ninjas JOIN dojos ON ninjas.dojo_id = dojos.id WHERE dojos.id = %(id)s;"
        resultado = connectToMySQL('esquema_dojos_y_ninjas').query_db(query, data)
        return resultado