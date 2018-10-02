#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  2 20:39:32 2018

@author: jvitorio
"""

#! /usr/bin/env python
# _*_ coding: utf-8 _*_
"""Modulo que contem a classe para representar o SentiLex."""


class Sentilex(object):

    """Classe para representar a base SentiLex PT 02."""

    lemas_filename = "SentiLex-lem-PT02.txt"
    flex_filename = "SentiLex-flex-PT02.txt"
    lemas = []
    flexoes = []

    def __init__(self, sentilex_path=None):
        self.sentilex_path = sentilex_path if sentilex_path is not None else ''
        if sentilex_path is not None:
            self.loadLemas()
            self.loadFlexoes()

    def setSentilexPath(self, sentilex_path):
        self.sentilex_path = sentilex_path

    def getSentilexDir(self):
        return self.sentilex_path

    def getLemasPath(self):
        return self.sentilex_path + '/' + self.lemas_filename

    def getFlexPath(self):
        return self.sentilex_path + '/' + self.flex_filename

    def getLemaLine(self):
        return "aberração.PoS=N;TG=HUM:N0;POL:N0=-1;ANOT=MAN"

    def _parseLemaLine(self, linha):
        """Parseia uma linha e monta o dicionario de lema."""
        lema = {}
        campos = linha.split(';')
        lema['lema'] = campos[0].split('.PoS=')[0]
        lema['POS'] = campos[0].split('.PoS=')[1]
        lema['polaridade'] = int(campos[2].split('=')[1])
        return lema

    def _readLemaFile(self):
        """Le o arquivo de lemas e retorna uma lista com as linhas."""
        fd = open(self.getLemasPath(), 'r')
        return fd.readlines()

    def loadLemas(self):
        for line in self._readLemaFile():
            self.lemas.append(self._parseLemaLine(line))

    def getLema(self, index=0):
        """Retorna um lema como um dicionario."""
        return self.lemas[index]

    def searchLema(self, palavra):
        """Busca o lema e retorna o dicionario correspondente."""

        try:
            dictLema = (lema
                        for lema in self.lemas
                        if lema['lema'] == palavra).next()
        except StopIteration:
            dictLema = None

        return dictLema

    def getFlexLine(self):
        line = "sacudais,sacudir.PoS=V;Flex=S:2p|Y:2p;TG=HUM:N0:N1;"
        line += "POL:N0=1;POL:N1=-1;ANOT=MAN"
        return line

    def getFlex(self, index=0):
        return self._parseFlexLine(self.getFlexLine())

    def searchFlex(self, palavra):
        """Busca a flexao e retorna o dicionario correspondente"""

        try:
            #print("procurando")
            dictFlex = (flex
                        for flex in self.flexoes
                        if flex['flex'] == palavra).next()
        except StopIteration:
            #print ("parou a busca")
            dictFlex = None

        return dictFlex

    def _readFlexFile(self):
        """Le o arquivo de flexoes e retorna uma lista com as linhas."""

        fd = open(self.getFlexPath(), 'r')
        return fd.readlines()

    def _parseFlexLine(self, linha):
        """Parseia uma linha o monta o dicionario da flexao."""
        flexao = {}
        campos = linha.split(';')
        flexao['flex'] = campos[0].split(',')[0]
        flexao['lema'] = campos[0].split(',')[1].split('.PoS=')[0]
        flexao['POS'] = campos[0].split(',')[1].split('.PoS=')[1]
        flexao['polaridade'] = int(campos[3].split('=')[1])
        if len(campos) == 6 and campos[4].startswith('POL:'):
                flexao['polaridade:n1'] = int(campos[4].split('=')[1])
        return flexao

    def loadFlexoes(self):
        for line in self._readFlexFile():
            self.flexoes.append(self._parseFlexLine(line))