# funkcje zagnieżdzone

def fun1():
    print("To jest fun1")

    def fun2(): # to jest tylko deklaracja funkcji
        print("To jest fun2")

    return fun2 # zwracamy adres funkcji - brak nawiasów!

fun1() #To jest fun1

x = fun1() # To jest fun1
print(x) # <function fun1.<locals>.fun2 at 0x0000017258406F20>
print(type(x))
x() # to jest fun2
# fun2() #<function fun1.<locals>.fun2 at 0x0000017258406F20>


