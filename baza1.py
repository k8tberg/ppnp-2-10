# relacyjna baza danych sql
# sqlite baza w jednym pliku

import sqlite3

try:
    sql_connection = sqlite3.connect('sqlite_python.db')
    cursor = sql_connection.cursor()
    print("Baz danych została podłączona")

except sqlite3.Error as e:
    print("Błąd podczas podłączanie bazy danych")
finally:
    if sql_connection:
        sql_connection.close()
        print("Baza danych została zamknięta")
