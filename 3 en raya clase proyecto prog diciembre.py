# -*- coding: cp1252 -*-
def tres_en_raya():
    #Estos son los números que salen en el tablero.
    tablero = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    fin = False
    #Estas son las combinaciones que dan la victoria.
    combi_victoria = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))

    print "Debes introducir los movimientos indicando un numero del 1 al 9, que figuran en el mismo tablero."

    #Este es el dibujo del tablero.
    def dibujo():
        print " _"*6
        print "|",tablero[6],"|",tablero[7],"|",tablero[8],"|"
        print " -"*6
        print "|",tablero[3],"|",tablero[4],"|",tablero[5],"|"
        print " -"*6
        print "|",tablero[0],"|",tablero[1],"|",tablero[2],"|"
        print " -"*6

    #Este es el turno del jugador 1 (el que elige donde poner la X).
    def p1():
        n = elige_numero()
        if tablero[n] == "X" or tablero[n] == "O":
            print("\nNo puedes poner tu ficha ahí­. Intentalo otra vez.")
            p1()
        else:
            tablero[n] = "X"

    #Este es el turno del jugador 2 (el que elige donde poner la O).
    def p2():
        n = elige_numero()
        if tablero[n] == "X" or tablero[n] == "O":
            print("\nNo puedes poner nada ahí ya. Intentalo otra vez.")
            p2()
        else:
            tablero[n] = "O"
    #Esta función valida si el número introdcido por J1 o J2 es válido.
    def elige_numero():
        while True:
            while True:
                a = input()
                try:
                    a  = int(a)
                    a -= 1
                    if a in range(0, 9):
                        return a
                    else:
                        print("\nEse número no está en el tablero. Intentalo otra vez.")
                        continue
                except ValueError:
                   print("\nEso no es un número. Intentalo otra vez.")
                   continue

    #Finalmente, la siguiente función comprueba el tablero y comprueba si alguien ha
    #ganado mirando en "combi_victoria", que es donde están las combinaciones
    #de victoria posibles.

    def comprobar_tablero():
        conteo = 0
        for a in combi_victoria:
            if tablero[a[0]] == tablero[a[1]] == tablero[a[2]] == "X":
                print("¡Ha ganado el jugador 1!\n")
                print("¡Enhorabuena!\n")
                return True

            if tablero[a[0]] == tablero[a[1]] == tablero[a[2]] == "O":
                print("¡Ha ganado el jugador 2!\n")
                print("¡Enhorabuena!\n")
                return True
        for a in range(9):
            if tablero[a] == "X" or tablero[a] == "O":
                conteo += 1
            if conteo == 9:
                print("El juego ha terminado en empate.\n")
                return True

    #Esto siguiente se ejecuta si nadie ha ganado aún.

    while not fin:
        dibujo()
        fin = comprobar_tablero()
        if fin == True:
            break
        print("Jugador 1, elige un lugar en el que poner una X.")
        p1()
        dibujo()
        fin = comprobar_tablero()
        if fin == True:
            break
        print("Jugador 2, elige un lugar en el que poner una O.")
        p2()

    if raw_input("¿Quieres jugar otra vez? (s/n)\n") == "s":
        elige_opcion()
    else:
        print "¡Muchas gracias por jugar!"
        print "FIN DEL JUEGO."

def tres_en_raya_maquina():
    # 3 en raya usando una lista
    import random # para generar numeros aleatorios
    import os # para borrar la pantalla
 
    # VARIABLES
    movpc=random.randint(0,8)
    ganador=0
 
    tablero=[" "," "," ",
             " "," "," ",
             " "," "," " ]
 
    tableroins=["7","8","9",
             "4","5","6",
             "1","2","3" ]
 
    ins="Debes introducir los movimientos indicando un numero del 1 al 9 de este modo."
 
    # funcion para imprimir el tablero
    def imprimetablero():
        print " _"*6
        print "|",tablero[6],"|",tablero[7],"|",tablero[8],"|"
        print " -"*6
        print "|",tablero[3],"|",tablero[4],"|",tablero[5],"|"
        print " -"*6
        print "|",tablero[0],"|",tablero[1],"|",tablero[2],"|"
        print " -"*6
 
    # funcion para comprobar el ganador
    def comprobarjugada():
        # Humano
        if tablero[0]=="X":
            if tablero[1]=="X" and tablero[2]=="X":
                return 1
            if tablero[3]=="X" and tablero[6]=="X":
                return 1
            if tablero[4]=="X" and tablero[8]=="X":
                return 1
        elif tablero[4]=="X":
            if tablero[3]=="X" and tablero[5]=="X":
                return 1
            if tablero[1]=="X" and tablero[7]=="X":
                return 1
            if tablero[2]=="X" and tablero[6]=="X":
                return 1
        elif tablero[8]=="X":
            if tablero[2]=="X" and tablero[5]=="X":
                return 1
            if tablero[7]=="X" and tablero[6]=="X":
                return 1
            if tablero[4]=="X" and tablero[0]=="X":
                return 1
        #maquina
        elif tablero[0]=="O":
            if tablero[1]=="O" and tablero[2]=="O":
                return 2
            if tablero[3]=="O" and tablero[6]=="O":
                return 2
            if tablero[4]=="O" and tablero[8]=="O":
                return 2
        elif tablero[4]=="O":
            if tablero[3]=="O" and tablero[5]=="O":
                return 2
            if tablero[1]=="O" and tablero[7]=="O":
                return 2
            if tablero[2]=="O" and tablero[6]=="O":
                return 2
        elif tablero[8]=="O":
            if tablero[2]=="O" and tablero[5]=="O":
                return 2
            if tablero[7]=="O" and tablero[6]=="O":
                return 2
            if tablero[4]=="O" and tablero[0]=="O":
                return 2
        else:
        # final de la comprobacion si no ha ganado ninguno mantiene en 0 la variable ganador
            return 0
 
    def resultado(ganador):
        if ganador==1:
            print "¡Enhorabuena, has ganado!"
        elif ganador==2:
            print "Acabas de perder... ¡Otra vez será!"
        else:
            print "El juego ha terminado en empate."
 
    # IMPRIME INSTRUCCIONES
    print ins
    print " _"*6
    print "|",tableroins[0],"|",tableroins[1],"|",tableroins[2],"|"
    print " -"*6
    print "|",tableroins[3],"|",tableroins[4],"|",tableroins[5],"|"
    print " -"*6
    print "|",tableroins[6],"|",tableroins[7],"|",tableroins[8],"|"    print " -"*6
 
    # bucle; movimientos 5 humano (empieza) 4 maquina
    for turno in range(1,6):
    
        # movimiento humano y comprobacion
        movhuman=int(raw_input("Elige un movimiento del 1 al 9: "))
        movhuman-=1
        while movhuman>8 or movhuman<0 or tablero[movhuman]=="X" or tablero[movhuman]=="O":
            movhuman=int(raw_input("Ese número no es correcto. Elige un número válido del 1 al 9: "))
            movhuman-=1
        tablero[movhuman]="X"
    
        # impresion del turno humano
        os.system("clear")
        print "Humano:"
        imprimetablero()
    
        # comprueba si alguno de los 2 ha ganado ganado
        ganador=comprobarjugada()
        if ganador>0 and ganador<3:
            break
    
        # pc 4 turnos el ultimo no lo juega por falta de espacio en el tablero
        if turno < 5:
            #movimiento maquina genero el numero aleatorio con la resta aplicada, el while evita que la compu ponga ficha encima de las existentes
            movpc=random.randint(0,8)
            while tablero[movpc]=="X" or tablero[movpc]=="O":
                movpc=random.randint(0,8)
            tablero[movpc]="O"
        
            # Impresion turno maquina
            os.system("clear")
            print "Maquina:"
            imprimetablero()
        
            # comprueba si alguno de los 2 ha ganado
            ganador=comprobarjugada()
            if ganador>0 and ganador<3:
                break
 
    resultado(ganador)
    
    if raw_input("¿Quieres jugar otra vez? (s/n)\n") == "s":
        elige_opcion()
    else:
        print "¡Muchas gracias por jugar!"
        print "FIN DEL JUEGO."

print "BIENVENIDO AL 3 EN RAYA DE PYTHON."
def elige_opcion():
    opcion=int(raw_input("Elige si quieres jugar contra otro jugador (1) o contra la máquina (2): "))
    if opcion == 1:
        tres_en_raya()
    elif opcion == 2:
        tres_en_raya_maquina()
    else:
	print "Esa opción no existe. Elige 1 o 2."
	elige_opcion()
elige_opcion()
