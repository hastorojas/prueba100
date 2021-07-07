from psycopg2 import connect, Error

try:

    conn = connect(
    user = "postgres",
    password = "Nomeacuerdo1701",
    host = "localhost",
    database = "postgres",
    port="5432"
    )

    cursor = conn.cursor()
    sql = "select version();"
    cursor.execute(sql)
    result = cursor.fetchall()
    print(result)

except(Exception,Error) as error:
    print(f"Hubo un error {str(error)}")
finally:
    if(conn):
        cursor.close()
        conn.close()