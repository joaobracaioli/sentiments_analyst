#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  2 20:35:51 2018

@author: jvitorio
"""

from sentilex import Sentilex

sl = Sentilex('/SentiLex-PT02')

frase = []

## Adicione uma faze, faça a tokenização dessa frase e percorra cada palabra achando
## a polaridade


acumulador = 0
for palavra in frase:
    f = sl.searchFlex(palavra)
    if f is not None:
        acumulador += f['polaridade']

print 'Polaridade: ' + str(acumulador)
