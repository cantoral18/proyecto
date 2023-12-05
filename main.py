import orm
from Tablas.Alumnos import Alumnos
from Tablas.Carrera import Carrera
from Tablas.Instituto import Instituto



db=orm.SQLiteORM("db_rigistros_alumnos")
db.crear_tabla(Alumnos)
db.crear_tabla(Carrera)
db.crear_tabla(Instituto)


Alumnos_uno={
    
        "dni":"78965412",
        "nombre":"juan",
        "apellidos":"espinoza",
        "f_nacimiento":"12/01/2000",
        "carrera":"administracion"
    }









# print(db.mostrar("alumnos"))