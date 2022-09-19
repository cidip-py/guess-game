import random as r

# variable control
intt = 3
win = False

palabra = None

#generador de numero
ran = r.randint(0,10)

#clase creadora de palabras
class Pl:
    def __init__(pl,name,info):
        pl.name = name
        pl.info = info
    def pfunc(pl):
        print(pl.info)
p1= Pl("tortuga","animal marino con caparazon")
p2= Pl("agua", "liquido esencial")
p3= Pl("bicicleta","vehiculo de dos ruedas")
p4= Pl("remera","prenda de vestir plana")
p5= Pl("esmeralda","piedra preciosa verde")
p6= Pl("vangogh","pintor de la noche estrellada")
p7= Pl("guitarra","instrumento de 6 cuerdas")
p8= Pl("samsung","marca coreana de celulares")
p9= Pl("los simpson","serie de personajes amarillos")
p10= Pl("elon musk","creador de Tesla")

# funcion para generar una palabra random

#palabra a adivinar

words = [p1.name,p2.name,p3.name,p4.name,p5.name,p6.name,p7.name,p8.name,p9.name,p10.name]
info = [p1.info,p2.info,p3.info,p4.info,p5.info,p6.info,p7.info,p8.info,p9.info,p10.info]




while intt != 0 and win == False:
    print("jugaremos a un juego de adivinanza,,,")
    print(info[ran])
    palabra = words[ran]
    #print(palabra) 
    resp = input("inserte palabra: ")

    if resp == palabra and intt > 3:
        print("Has ganado!!!")
        win = True
    elif resp != palabra :
        intt = intt-1
        print("Vamos de nuevo...")
