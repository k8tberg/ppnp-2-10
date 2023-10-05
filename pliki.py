# praca z plikami
# kontekst manager (with)
# r - read (default
# w - write, truncating the file first
# x - creat a new file and open it for
# a - open for writing
with open('test.log', 'w', encoding='utf-8') as fh: #filehandler
    fh.write("Powitanie\n")
    fh.write("Kolejne\n")
    fh.write("Jeszcze Jedno\n")

with open('test.log', 'w', encoding='utf-8') as file:
    file.write("Radek\n")

with open('test.log', 'a', encoding='utf-8') as f:
    f.write("dodane\n")
    f.write("dośdane\n")

with open('test.log', 'r', encoding='utf-8') as file:
    lines = file.read()

print(lines)
print(type(lines)) # <class 'str'>