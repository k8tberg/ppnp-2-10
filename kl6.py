class MyException(Exception): # dziedziczenie po klasie Exception
    def __init__(self, message):
        super().__init__(message) # konstruktor z klasy Exception (?)

try:
#print(2/0)
    raise MyException("Wysyąpił wyjątek") # MyException: Wystąpił wyjątek - rzucamy wyjątek
except MyException:
    print("Wystąpił wyjątek MyException")

except Exception as e:
    print("Błąd", e) # Błąd wystąpił wyjątek