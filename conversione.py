#!/bin/python
import math;
bad=True;
while bad==True:
    print "Hello World!";
    print "Hello World!!";
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
