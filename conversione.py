#!/bin/python
import math;
contatore=int(1);
i=int(0);
resti=int(0);
numeroout=0;
bad=True;
while bad==True:
    print "-------------------------------------------------------------------";
    print "Versione Python realizzata da Carmine del";
    print "convertitore decimale-binario binario-decimale Di Carmine e Biagio";
    print "-------------------------------------------------------------------";
    print "";
    print "";
    print "Binario->Decimale o Decimale->Binario?";
    risposta = raw_input();
    print "hai risposto",risposta;
    if risposta=="Binario->Decimale":
        bindec=True;
        decbin=False;
        bad=False;
    if risposta=="Decimale->Binario":
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
numerocorrente=int(numeroin)
if decbin==True:
    while numerocorrente>0:
        resto=numerocorrente%2;
        resti=int(resti+resto*contatore);
        numerocorrente=int(numerocorrente/2);
        contatore=contatore*10;
    print "Il numero convertito in decimale e'",resti;
if bindec==True:
    while numerocorrente>0:
        ultimacifra=numerocorrente%10;
        numeroout=numeroout+(ultimacifra*pow(2,i));
        numerocorrente=int(numerocorrente/10);
        i=i+1;
    print "Il numero convertito in binario e'",numeroout;
