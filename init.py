from conexion import conexion


conn = conexion()
query = "select * from profesores"
result = conn.consultarBDD(query)
print(result)