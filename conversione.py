#!/usr/bin/env python
BAD_NUMBER=False;
import math;
def tobin():
    while numerocorrente>0:
        resto=numerocorrente%2;
        resti=int(resti+resto*contatore);
        numerocorrente=int(numerocorrente/2);
        contatore=contatore*10;
    return resti;
def todec():
    numerodacontrollare=int(numeroin);
    numerovabene=True;
    while numerodacontrollare>0:                    #Inizio controllo numero binario
        if numerodacontrollare%10!=1 and numerodacontrollare%10!=0:
            numerovabene=False;
        numerodacontrollare=numerodacontrollare/10; #Fine controllo numero binario
        if not numerovabene:                         #Inizio applicazione controllo numero binario
            return BAD_NUMBER                           #Fine applicazione controllo numero binario
        while numerocorrente>0:
            ultimacifra=numerocorrente%10;
            numeroout=numeroout+(ultimacifra*pow(2,i));
            numerocorrente=int(numerocorrente/10);
            i=i+1;
        return numeroout;
