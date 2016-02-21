#!/usr/bin/env python
# -*- coding: utf-8 -*-

from lxml import etree

arbol=etree.parse('procesion.xml')
raiz=arbol.getroot()

procesiones=raiz.xpath("//procesion")

#3)Pedir por teclado el inicio del campo cofradia, (Por ejemplo buscar todas las cofradias que empiecen por "Hermandad").

cofradia=raw_input("Dime el inicio del nombre de la hermandad: ")

for cofradias in procesiones:
	if cofradias.find("cofradia").text.startswith(cofradia.title()):
		print cofradias.find("cofradia").text