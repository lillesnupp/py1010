#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Arbeidskrav 2 - PY1010-1 24H Grunnleggende programmering med Python

@author: Anne-Marie Myhrvold
"""

# Oppg 1) Du skal her lage et program som skal starter med 
# alder = int(input('Hvilket år er du født? ') )
# Programmet skal så regne ut hvor gammel personen blir nå i løpet av år 2024 og skrive svaret til skjerm med passende tekst

# Be om fødselsår:
alder = int(input('Hvilket år er du født? ') )

# Beregne alder i 2024:
alder_2024 = 2024 - alder

# Skrive ut resultat: 
print(f'I 2024 blir du {alder_2024} år gammel.')
