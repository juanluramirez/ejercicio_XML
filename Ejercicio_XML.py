# -*- coding: utf-8 -*-

#

from lxml import etree
arbol=etree.parse('procesion.xml')

raiz=arbol.getroot()

procesiones=raiz.findall("/resultado/result")

