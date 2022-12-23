import random
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.collections as collections
nombre=(input('ingrese su nombre:'))
print('Hola', nombre)
while(True):
    print('''Ahora se te precentaran las opciones de esta plataforma:
    1)Jugar piedra, papel y tijeras.
    2)adivinar un numero
    3)tirar un dado
    4)graficar una funcion''')
    opcion=int(input())
    while(True):
        if opcion==1:
                print('vamos a jugar piedra papel y tijeras')
                print('''seleccione la opcion que considere apropiada
                1)piedra
                2)papel
                3)tijeras''')
                usuario=int(input())
                computadora= random.randrange(1,4)
                if usuario==computadora:
                    print('has empatado')
                elif usuario==1 and computadora==2:
                    print('has perdido')
                elif usuario==1 and computadora==3:
                    print('has ganado')
                elif usuario==2 and computadora==3:
                    print('has perdido')
                elif usuario==2 and computadora==1:
                    print('has ganado')
                elif usuario==3 and computadora==1:
                    print('has perdido')
                elif usuario==3 and computadora==2:
                    print('has perdido')
                else:
                    print('su eleccion no esta entre las opciones')
                    break
                if computadora==1:
                    print('la computadora a elejido piedra')
                elif computadora==2:
                    print('la computadora a elejido papel')
                elif computadora==3:
                    print('la computadora a elejido tijeras')
                print('''deseas seguir jugando
                1)si
                2)no''')
                seguir=input()
                if seguir=='2':
                    break
    
        elif opcion==2:
            print('''vamos a jugar a adivina el numero

primero la computadora generara un numero al azar y luego tu deberas adivinarlo
elije la modalidad de juego:
                1)facil
                2)intermedio
                3)dificil
                4)imposible''')
            dificultad=int(input())
            if dificultad==1:
                numerofinal=random.randrange(1,6)
                print('has seleccionado dificultad facil, en esta dificultad deberas acertar un numero del 1 al 5')
                print('tienes 3 intentos')
                for x in range(0,3):
                    intento=int(input())
                    if intento==numerofinal:
                        print('felicitaciones has acertado')
                        break
                    elif intento<numerofinal:
                        print('no has acertado, prueba con un numero mas grande')
                    elif intento>numerofinal:
                        print('no has acertasdo, prueba con un numero mas pequeño')
                    elif intento>5:
                        print('te recuerdo que el numero se encuentra entre el 1 y el 5')
            if dificultad==2:
                numerofinal2=random.randrange(1,11)
                print('has seleccionado la dicultad intermedia, en esta dificultad deberas acertar un numero del 1 al 10')
                print('tines 3 intentos')
                for x in range(0,3):
                    intento2=int(input())
                    if intento2==numerofinal2:
                        print('has acertado felicitaciones')
                        break
                    elif intento2<numerofinal2:
                        print('no has acertado, prueba con un numero mas grande')
                    elif intento2>numerofinal2:
                        print('no has acertado, prueba con un numero mas chico')
                    elif intento2>10:
                        print('te recuerdo que el numero se encuentra entre el 1 y el 10')
            if dificultad==3:
                numerofinal3=random.randrange(1,21)
                print('has seleccionado la dicultad dificil, en esta dificultad deberas acertar un numero del 1 al 20')
                print('tines 3 intentos')
                for x in range(0,3):
                    intento3=int(input())
                    if intento3==numerofinal3:
                        print('has acertado felicitaciones')
                        break
                    elif intento3<numerofinal3:
                        print('no has acertado, prueba con un numero mas grande')
                    elif intento3>numerofinal3:
                        print('no has acertado, prueba con un numero mas chico')
                    elif intento3>20:
                        print('te recuerdo que el numero se encuentra entre el 1 y el 20')
            if dificultad==4:
                numerofinal4=random.randrange(1,11)
                print('has seleccionado dificultad imposible, en esta dificultad debes acertar un numero del 1 al 10, pero no tendras pistas')
                print('tines 3 intentos')
                for x in range(0,3):
                    intento4=int(input())
                    if intento4==numerofinal4:
                        print('que suerte tines, has acertadio')
                        break
            print('''deseas volver a jugar?
                1)Si
                2)No''')
            vuelta=int(input())
            if vuelta==2:
                break

        elif opcion==3:
            print('has seleccionado la opcion de tirar un dado')
            maximo=int(input('ingrse el numero de caras que tendra el dado:'))
            randm=random.randrange(1,maximo)+1
            print('el dado a dado el numero',randm)
            print('''deseas seguir tirando del dado?
                1)si
                2)no''')
            volver=int(input())
            if volver==2:
                break
        elif opcion==4:
            print('has seleccionado la opcion de ver una grafico')
            t = np.arange(0.0, 2, 0.01)
            s1 = np.sin(2*np.pi*t)
            s2 = 1.2*np.sin(4*np.pi*t)


            fig, ax = plt.subplots()
            ax.set_title('using span_where')
            ax.plot(t, s1, color='black')
            ax.axhline(0, color='black', lw=2)

            collection = collections.BrokenBarHCollection.span_where(
                t, ymin=0, ymax=1, where=s1 > 0, facecolor='green', alpha=0.5)
            ax.add_collection(collection)

            collection = collections.BrokenBarHCollection.span_where(
                t, ymin=-1, ymax=0, where=s1 < 0, facecolor='red', alpha=0.5)
            ax.add_collection(collection)


            plt.show()
            print('''deseas volver a ver el grafico??
            1)si
            2)no''')
            volvicion=int(input())
            if volvicion==2:
                break
        
        else:
            print('el numero ingrsesado no corresponde a ninguna actividad')
            break
        
        
