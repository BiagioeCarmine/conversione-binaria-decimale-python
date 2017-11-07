#!/usr/bin/env python3
BAD_NUMBER=False
import math
def tobin(numin,callback):
    numeroin=int(numin)
    contatore=1
    resti=0
    numerocorrente=numeroin
    while numerocorrente>0:
        resti=resti+numerocorrente%2*contatore

        numerocorrente=int(numerocorrente/2)
        contatore=contatore*10
    return callback(False," ",resti)

def todec(numin,callback):
    numeroin=int(numin)
    numerocorrente=numeroin
    numerodacontrollare=numeroin
    numerovabene=True
    numeroout=0
    i=0
    while numerodacontrollare>0:                    #Inizio controllo numero binario
        if numerodacontrollare%10!=1 and numerodacontrollare%10!=0:
            numerovabene=False
        numerodacontrollare=int(numerodacontrollare/10) #Fine controllo numero binario
    if not numerovabene:                         #Inizio applicazione controllo numero binario
        return callback(True,"Numero non binario",0)                           #Fine applicazione controllo numero binario
    while numerocorrente>0:
        ultimacifra=numerocorrente%10
        numeroout=numeroout+(ultimacifra*pow(2,i))
        numerocorrente=int(numerocorrente/10)
        i=i+1
    return callback(False," ",numeroout)
