# relacyjna baza danych sql
# sqlite baza w jednym pliku

import sqlite3

try:
    sql_connection = sqlite3.connect('sqlite_python.db')
    query = ''' 
    CREATE TABLE developers (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    joining_data DATETIME,
    salary REAL NOT NULL);
    '''
    cursor = sql_connection.cursor()
    print("Baz danych została podłączona")

    with open('tables.sql', 'r') as file:
        sql_script = file.read()

    # cursor.execute(query)  # wykonanie query na bazie # komentujemy, bo uruchamiamy z pliku (patrz niżej) executescript
    # sql_connection.commit()
    cursor.executescript(sql_script)
except sqlite3.Error as e:
    print("Błąd podczas podłączanie bazy danych", e)
finally:
    if sql_connection:
        sql_connection.close()
        print("Baza danych została zamknięta")

# możemy uruchomić tylko raz, bo jeśli uruchomimy ponownie pojawia się błąd:
# "Błąd podczas podłączanie bazy danych table developers already exists"
