#!/usr/bin/env python
# -*- coding: utf-8 -*-

from lxml import etree

arbol=etree.parse('procesion.xml')
raiz=arbol.getroot()

procesiones=raiz.xpath("//procesion")

#1)Lista los nombres de las cofradia que salen el lunes, martes, miercoles,jueves y el viernes, sabado santo y domingo Resurreccion.

print "\n Domingo de Ramos"
print "============\n"
for nombres in procesiones:
	if nombres.find("dia").text=="Domingo de Ramos":
		print "La cofradia se llama",nombres.find("cofradia").text
print "\n Lunes Santo"
print "============\n"
for nombres in procesiones:
	if nombres.find("dia").text=="Lunes Santo":
		print "La cofradia se llama",nombres.find("cofradia").text
print "\n Martes Santo"
print "============\n"
for nombres in procesiones:
	if nombres.find("dia").text=="Martes Santo":
		print "La cofradia se llama",nombres.find("cofradia").text
print "\n Miercoles Santo"
print "============\n"
for nombres in procesiones:
	if nombres.find("dia").text=="Miercoles Santo":
		print "La cofradia se llama",nombres.find("cofradia").text
print "\n Jueves Santo"
print "============\n"
for nombres in procesiones:
	if nombres.find("dia").text=="Jueves Santo":
		print "La cofradia se llama",nombres.find("cofradia").text
print "\n Viernes Santo"
print "============\n"
for nombres in procesiones:
	if nombres.find("dia").text=="Viernes Santo":
		print "La cofradia se llama",nombres.find("cofradia").text
print "\n Sabado Santo"
print "============\n"
for nombres in procesiones:
	if nombres.find("dia").text=="Sabado Santo":
		print "La cofradia se llama",nombres.find("cofradia").text
print "\n Domingo de Resurreccion"
print "============\n"
for nombres in procesiones:
	if nombres.find("dia").text=="Domingo de Resurreccion":
		print "La cofradia se llama",nombres.find("cofradia").text

#2)Contador del numero de cofradias que salen el lunes, martes, miercoles,jueves y el viernes, sabado santo y domingo Resurreccion.

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

salida=raw_input("Dime inicio salida procesion: ")

for cofradias in procesiones:
	if cofradias.find("salida").text.startswith(salida.title()):
		print "La cofradia es",cofradias.find("cofradia").text,"sale de",cofradias.find("salida").text,"y sale a las",cofradias.find("hora").text
