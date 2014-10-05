class Tennis():

    def juego(self):
        tennis = Tennis()
        jugador1 = 0
        jugador2 = 0

        while(jugador1 != 50 and jugador2 != 50):
            print "===Juego de Tennis==="
            val = input("1-Jugador1 \n2-Jugador2\n")
            # KeyboardInterrupt
            if val == 1:
                if jugador1 < 30:
                    jugador1 = jugador1 + 15
                    # print "jugador1",jugador1
                    tennis.hazPuntos(jugador1, jugador2)
                else:
                    jugador1 = jugador1 + 10
                    # print "jugador1",jugador1
                    tennis.hazPuntos(jugador1, jugador2)
            elif val == 2:
                if jugador2 < 30:
                    jugador2 = jugador2 + 15
                    # print "jugador2",jugador2
                    tennis.hazPuntos(jugador1, jugador2)
                else:
                    jugador2 = jugador2 + 10
                    # print "jugador2",jugador2
                    tennis.hazPuntos(jugador1, jugador2)

    def hazPuntos(self, jugador1, jugador2):
        if jugador1 == 40 and jugador2 == 40:
            print "DEUCE!!"
            # if jugador1 == 50:
            #  print "Score:","AD","-",jugador2
            # jugador1 = jugador1 - 10
            # elif jugador2 == 50:
            #  print "Score:",jugador1,"-","AD"
            # jugador2 = jugador2 - 10
        else:
          # else:
            if jugador1 == 50 and jugador2 < 50:
                print "Set y Juego"
            elif jugador1 < 50 and jugador2 == 50:
                print "Set y Juego"
            else:
                print "Score:", jugador1, "-", jugador2
