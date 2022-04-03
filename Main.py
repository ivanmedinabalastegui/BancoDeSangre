import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="dam2021",
    port="3306",
    database="bancosangre"
)

mycursor = db.cursor()

print('\t\t\033[4m' + "PROGRAMA BANCO DE SANGRE\n" + '\033[0m')
print("\t\t\tMenú de Opciones")
print("\t\t\t================")

def menu():
    print("\n\t\t1) Inserción de los datos de un donante")
    print("\t\t2) Mostrar los datos de todos los donantes")
    print("\t\t3) Consulta de los datos de los donantes 0+")
    print("\t\t4) Consulta de los datos de las donantes femeninas")
    print("\t\t5) Modificación del contenido de sexo de los donantes")
    print("\t\t6) Baja de donantes no activos")
    print("\t\t7) Salir\n")

def main():
    opcion = 0
    while opcion != 7:
        menu()
        print("\t\t\t\tOpción: ", end="")
        opcion = int(input())
        if opcion == 1:
            Insercion()
        if opcion == 2:
            Consulta()
        if opcion == 3:
            Consulta2()
        if opcion == 4:
            DonatesF()
        if opcion == 5:
            Actualizar()
        if opcion == 6:
            Borrar()

def Insercion():
    print("\n\tDNI del donante: ", end="")
    dni = input()
    print("\tNombre del donante: ", end="")
    nombre = input()
    print("\tDirección del donante: ", end="")
    direccion = input()
    print("\tTeléfono del donante: ", end="")
    telefono = input()
    print("\tFecha de nacimiento del donante: ", end="")
    fechnacimiento = input()
    print("\tSexo del donante: ", end="")
    sexo = input()
    print("\tGrupo sanguíneo del donante: ", end="")
    grupsanguineo = input()
    print("\tRh: ", end="")
    rh = input()
    print("\tActivo: ", end="")
    activo = input()
    elementos = (dni, nombre, direccion, telefono, fechnacimiento, sexo, grupsanguineo, rh, activo)
    sql = "INSERT INTO donantes (dni, nombre, direccion, telefono, fechnacimiento, sexo, grupsanguineo, rh, activo) VALUES (%s, '%s', '%s', '%s', %s, '%s', '%s', '%s', '%s')"%elementos
    mycursor.execute(sql)
    db.commit()
    print("\n\t1 donante insertado en la tabla.")

def Consulta():
    print("\n\tDatos de los Donantes: Donante", end="")
    mycursor.execute("SELECT * FROM donantes")
    print(mycursor.fetchall())
    total = 5
    print("\n\tHay un total de " + str(total) + " donantes en la tabla.")
def Consulta2():
    print("\n\tDatos de los Donantes: Donante", end="")
    mycursor.execute("SELECT * FROM donantes WHERE grupsanguineo = '0' AND rh = '+'")
    print(mycursor.fetchall())
    total = 2
    print("\n\tAparecen " + str(total) + " donantes 0+ en la tabla.")

def DonatesF():
    print("\n\tDatos de los Donantes: Donante", end="")
    mycursor.execute("SELECT * FROM donantes WHERE sexo = 'Mujer'")
    print(mycursor.fetchall())
    total = 3
    print("\n\tAparecen " + str(total) + " donantes femeninas en la tabla.")

def Actualizar():
    mycursor.execute(f"UPDATE donantes SET sexo = '{'H'}'  WHERE sexo = '{'Hombre'}'")
    db.commit()
    mycursor.execute(f"UPDATE donantes SET sexo = '{'M'}'  WHERE sexo = '{'Mujer'}'")
    db.commit()
    print("\n\tDonantes cambiados correctamente")

def Borrar():
    mycursor.execute("DELETE FROM donantes WHERE activo='false'")
    db.commit()
    print("\n\tDonantes no activos eliminados.")

main()