def allparams(a, b, /, c=42, *args, d=256, ** kwargs):
    print("a, b", a, b)
    print("c, d", a, b)
    print("args", args)
    print("kwargs", kwargs)


allparams(1,2)
allparams(1,2, 3)
allparams(1,2, c=3)
#allparams(b=1,a=2, c=3) #TypeError: allparams() missing 2 required positional arguments: 'a' and 'b'
# / - oddziela arumenty pozycyjne od nazwanych
# a i b mogą być podane tylko kolejności
allparams(1,2,3,4,4,5,6,7,8,9)
allparams(1,2,3,4,4,5,6,7,8,100, 106, d=129) # jesli chcemy podać argsy, to 'c' musimy podać pozycyjnie, bo jest taka zasada, ze przed typem jak *arg zawsze musza byc podane argumenty z pozycji
allparams(1,2,3,4,4,5,6,7,8,100, 106, d=129, klucz='wart', a=8) #a trafi do słownika
#args i kwargs mogą być tylko raz w argumentach