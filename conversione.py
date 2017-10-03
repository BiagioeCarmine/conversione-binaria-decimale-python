#!/usr/bin/env python
import math;
def inizioprogramma():
    contatore=int(1);
    i=int(0);
    resti=int(0);
    numeroout=0;
    numerovabene=True;
    bad=True;
    while bad==True:
        print "-------------------------------------------------------------------";
        print "Versione scritta in Python realizzata da Carmine del";
        print "convertitore decimale-binario binario-decimale Di Carmine e Biagio";
        print "-------------------------------------------------------------------";
        print "";
        print "";
        print "Binario->Decimale o Decimale->Binario?";
        risposta = raw_input();
        print "hai risposto",risposta;
        if risposta=="Binario->Decimale" or risposta=="bindec":
            bindec=True;
            decbin=False;
            bad=False;
        if risposta=="Decimale->Binario" or risposta=="decbin":
            decbin=True;
            bindec=False;
            bad=False;
    print "bad=",bad;
    print "decbin=",decbin;
    print "bindec=",bindec;
    print "bad=",bad;
    if decbin==True:
        print "Inserisci un numero decimale da convertire in binario";
    if bindec==True:
        print "Inserisci un numero binario da convertire in decimale";
    numeroin=input();
    numerocorrente=int(numeroin);
    if decbin==True:
        while numerocorrente>0:
            resto=numerocorrente%2;
            resti=int(resti+resto*contatore);
            numerocorrente=int(numerocorrente/2);
            contatore=contatore*10;
        print "Il numero convertito in binario e'",resti;
    if bindec==True:
        numerodacontrollare=int(numeroin);
        while numerodacontrollare>0:                    #Inizio controllo numero binario
            ultimac=numerodacontrollare%10;
            if ultimac!=1 and ultimac!=0:
                numerovabene=False;
            numerodacontrollare=numerodacontrollare/10; #Fine controllo numero binario
        if not numerovabene:                         #Inizio applicazione controllo numero binario
            print "INSERISCI UN NUMERO BINARIO SE VERAMENTE VUOI FARE Binario->Decimale";
            inizioprogramma();                          #Fine applicazione controllo numero binario
        while numerocorrente>0:
            ultimacifra=numerocorrente%10;
            numeroout=numeroout+(ultimacifra*pow(2,i));
            numerocorrente=int(numerocorrente/10);
            i=i+1;
        print "Il numero convertito in decimale e'",numeroout;
inizioprogramma();
