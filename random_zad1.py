import random

# importowanie biblioteki random
# generaowanie liczb pseudolosowych

print(random.randint(1, 6))  # int 1...6 przedział obustronnie zakmniety
print(random.random())  # 0.6010549259493914
print(random.random() * 6)
print(random.randrange(6))  # int 0..5
print(random.randrange(1, 6))  # int 1..5

lista = [5, 7, 45, 34, 56]
print(random.choice(lista))

lista2 = list(range(1,50)) #1...49
print(lista2)
# print(random.choice(lista2))
# print(random.choice(lista2))
# print(random.choice(lista2))
# print(random.choice(lista2))
# print(random.choice(lista2))
# print(random.choice(lista2))

wyn = random.choice(lista2)
lista2.remove(wyn)
print(wyn)
wyn = random.choice(lista2)
lista2.remove(wyn)
print(wyn)
wyn = random.choice(lista2)
lista2.remove(wyn)
print(wyn)
wyn = random.choice(lista2)
lista2.remove(wyn)
print(wyn)

print(random.choices(lista2, k=6)) #[46, 27, 26, 34, 28, 24] - metoda losuje z powtórzeniami
print(random.sample(lista2, 6)) # [34, 21, 37, 42, 19, 2] - metoda losuje bez powtórzeń