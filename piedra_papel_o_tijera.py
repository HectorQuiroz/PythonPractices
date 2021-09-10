import random
opciones=['piedra','papel','tijera']
computer=random.choice(opciones)
usuario=input("Piedra, Papel o tijera? \n")

if computer == usuario:
    print("Empate")
    print("Computadora " + computer +" Usuario " + usuario)
elif (computer == 'piedra' and usuario == 'tijera') or (computer == 'tijera' and usuario == 'papel') or (computer == 'papel' and usuario == 'piedra'):
    print("Computadora gano!")
    print("Computadora " + computer + " Usuario " + usuario)
else:
    print("Jugador gana!")
    print("Computadora " + computer +" Usuario " + usuario)

