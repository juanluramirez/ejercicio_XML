#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
reload(sys)
sys.setdefaultencoding('utf8')

from lxml import etree

arbol=etree.parse('procesion.xml')
raiz=arbol.getroot()

procesiones=raiz.xpath("//procesion")

#1)Lista los nombres de las cofradia que salen el lunes, martes, miercoles,jueves y el viernes, sabado santo y domingo Resurreccion.

print "\n Domingo de Ramos"
print "====================\n"
print "Las cofradias que salen son:\n"
for nombres in procesiones:
	if nombres.find("dia").text=="Domingo de Ramos":
		print nombres.find("cofradia").text
print "\n Lunes Santo"
print "================\n"
print "Las cofradias que salen son:\n"
for nombres in procesiones:
	if nombres.find("dia").text=="Lunes Santo":
		print nombres.find("cofradia").text
print "\n Martes Santo"
print "================\n"
print "Las cofradias que salen son:\n"
for nombres in procesiones:
	if nombres.find("dia").text=="Martes Santo":
		print nombres.find("cofradia").text
print "\n Miércoles Santo"
print "====================\n"
print "Las cofradias que salen son:\n"
for nombres in procesiones:
	if nombres.find("dia").text=="Miércoles Santo":
		print nombres.find("cofradia").text
print "\n Jueves Santo"
print "=================\n"
print "Las cofradias que salen son:\n"
for nombres in procesiones:
	if nombres.find("dia").text=="Jueves Santo":
		print nombres.find("cofradia").text
print "\n Viernes Santo"
print "==================\n"
print "Las cofradias que salen son:\n"
for nombres in procesiones:
	if nombres.find("dia").text=="Viernes Santo":
		print nombres.find("cofradia").text
print "\n Sábado Santo"
print "=================\n"
print "Las cofradias que salen son:\n"
for nombres in procesiones:
	if nombres.find("dia").text=="Sábado Santo":
		print nombres.find("cofradia").text
print "\n Domingo de Resurrección"
print "===========================\n"
print "Las cofradias que salen son:\n"
for nombres in procesiones:
	if nombres.find("dia").text=="Domingo de Resurrección":
		print nombres.find("cofradia").text

#2)Contador del numero de cofradias que salen el Domingo de Ramos, lunes, martes, miercoles,jueves y el viernes, sabado santo y domingo Resurreccion.

contador_domingo=0
contador_lunes=0
contador_martes=0
contador_miercoles=0
contador_jueves=0
contador_viernes=0
contador_sabado=0
contador_resurreccion=0

print "\n Domingo de Ramos"
print "====================\n"
print "Salen un total de:\n"
for nombres in procesiones:
	if nombres.find("dia").text=="Domingo de Ramos":
		contador_domingo=contador_domingo+1
print contador_domingo

print "\n Lunes Santo"
print "================\n"
print "Salen un total de:\n"
for nombres in procesiones:
	if nombres.find("dia").text=="Lunes Santo":
		contador_lunes=contador_lunes+1
print contador_lunes

print "\n Martes Santo"
print "================\n"
print "Salen un total de:\n"
for nombres in procesiones:
	if nombres.find("dia").text=="Martes Santo":
		contador_martes=contador_martes+1
print contador_martes

print "\n Miércoles Santo"
print "====================\n"
print "Salen un total de:\n"
for nombres in procesiones:
	if nombres.find("dia").text=="Miércoles Santo":
		contador_miercoles=contador_miercoles+1
print contador_miercoles

print "\n Jueves Santo"
print "=================\n"
print "Salen un total de:\n"
for nombres in procesiones:
	if nombres.find("dia").text=="Jueves Santo":
		contador_jueves=contador_jueves+1
print contador_jueves

print "\n Viernes Santo"
print "==================\n"
print "Salen un total de:\n"
for nombres in procesiones:
	if nombres.find("dia").text=="Viernes Santo":
		contador_viernes=contador_viernes+1
print contador_viernes

print "\n Sábado Santo"
print "=================\n"
print "Salen un total de:\n"
for nombres in procesiones:
	if nombres.find("dia").text=="Sábado Santo":
		contador_sabado=contador_sabado+1
print contador_sabado

print "\n Domingo de Resurrección"
print "===========================\n"
print "Salen un total de:\n"
for nombres in procesiones:
	if nombres.find("dia").text=="Domingo de Resurrección":
		contador_resurreccion=contador_resurreccion+1
print contador_resurreccion

#3)Pedir por teclado el inicio del campo cofradia, (Por ejemplo buscar todas las cofradias que empiecen por "Hermandad").

cofradia=raw_input("Dime el inicio del nombre de la hermandad: ")

for cofradias in procesiones:
	if cofradias.find("cofradia").text.startswith(cofradia.title()):
		print cofradias.find("cofradia").text

#4)Pedir por teclado el "id" de una cofradia y mostrar la hora de salida y el sitio de salida de esa cofradia.

id_cofradia=raw_input("Dime el id de la cofradia: ")

for cofradias in procesiones:
	if cofradias.find("id").text==id_cofradia:
		print "La hora de salida de la",cofradias.find("cofradia").text,"es a las",cofradias.find("hora").text,"y sale de",cofradias.find("salida").text

#5)Pedir por teclado inicio del campo de salida y muestra la hora de salida y el nombre de la cofradia.

calle=raw_input("Dime por donde pasa la procesion: ")

print "Las cofradias que pasan por la calle",calle, "son:\n"
for cofradias in procesiones:
	if calle.title() in cofradias.find("description").text:
		print cofradias.find("cofradia").text,"y sale a las",cofradias.find("hora").text
