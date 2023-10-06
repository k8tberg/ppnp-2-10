# relacyjna baza danych sql
# sqlite baza w jednym pliku

import sqlite3

try:
    sql_connection = sqlite3.connect('sqlite_python.db')
    insert_sql = "INSERT INTO software (id, name, price) VALUES (1,'Python','1000000);"
    cursor = sql_connection.cursor()
    print("Baz danych została podłączona")
    cursor.execute(insert_sql)
    sql_connection.commit()

except sqlite3.Error as e:
    print("Błąd podczas podłączanie bazy danych")
finally:
    if sql_connection:
        sql_connection.close()
        print("Baza danych została zamknięta")
