import sqlite3
import datetime

con = sqlite3.connect('tienda.db')

'''def sql_table(con):

    cursorObj = con.cursor()

    cursorObj.execute("CREATE TABLE cliente(id integer PRIMARY KEY AUTOINCREMENT, nombre text, apellido text, ciudad text,fecha text)")

    con.commit()

sql_table(con)'''


def actividad1():

    while True:
        print("========================")
        print("  BIENVENIDO AL GESTOR  ")
        print("========================")
        print("1. Añadir cliente      ")
        print("2. Listar clientes     ")
        print("3. Modificar cliente   ")
        print("4. Borrar cliente      ")
        print("5. Salir               ")
        print("========================")

        option = input("> ")

        if option == '1':
            print("Añadiendo un cliente...\n")
            nombre = input("Nombre > ")
            apellidos = input("Apellidos > ")
            ciudad = input("ciudad > ")
            x = datetime.datetime.now()
            datos = (nombre, apellidos, ciudad,x)

            def sql_insert(con, entities):
                cursorObj = con.cursor()
                cursorObj.execute( 'INSERT INTO cliente(id, nombre, apellido, ciudad, fecha) VALUES(null, ?, ?, ?, ?)' , datos )
                con.commit()
            sql_insert(con, datos)
            print("Cliente añadido correctamente\n")

        elif option == '2':
            print("Listando los clientes...\n")

            def sql_fetch(con):
                cursorObj = con.cursor()
                cursorObj.execute('SELECT * FROM cliente')
                rows = cursorObj.fetchall()
                for row in rows:
                    print(row)
            sql_fetch(con)

        elif option == '3':
           cursorObj = con.cursor()
           id= input("¿ Qué id quieres cambiar ? > ")
           cursorObj.execute('SELECT * FROM cliente WHERE id='+id+';')
           rows = cursorObj.fetchall()

           for row in rows:
               print(row)

           def update(con):
               cursorObj = con.cursor()
               while True:

                print("[a] Modificar Nombre")
                print("[b] Modificar Apellido")
                print("[c] Modificar Ciudad")
                print("[d] Salir")

                modificar=(input())

                if(modificar=='a'):
                    nombre = input("Nombre > ")
                    cursorObj.execute('UPDATE cliente SET nombre=?  WHERE id=?;',( nombre,id))
                    con.commit()

                elif(modificar=='b'):
                    apellidos=input("Apellidos > ")
                    cursorObj.execute('UPDATE cliente SET apellido =? WHERE id=? ;',(apellidos,id))
                    con.commit()

                elif(modificar=='c'):
                    ciudad=input("Ciudad >")
                    cursorObj.execute('UPDATE cliente SET WHERE ciudad= ? WHERE id=? ;',(ciudad,id))
                    con.commit()

                elif (modificar == 'd'):
                    return False;

           update(con)

        elif option == '4':
            cursorObj = con.cursor()
            cursorObj.execute('SELECT * FROM cliente ;')
            rows = cursorObj.fetchall()
            for row in rows:
                print(row)

            id = input("¿Que id quieres Borrar > ")
            cursorObj.execute('DELETE FROM cliente WHERE id='+id+';')
            con.commit()
            print("Borrando un cliente...\n")
            print("Cliente borrado correctamente\n")

        elif option == '5':
            print("Saliendo...\n")
            return False
            break

        input("\nPresiona ENTER para continuar...")

actividad1()

