#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Arbeidskrav 2 - PY1010-1 24H Grunnleggende programmering med Python

@author: Anne-Marie Myhrvold
"""

# Oppg 1) Program som regner ut hvor gammel en person er i 2024 og skriver ut resultatet

# Be om fødselsår:
alder = int(input('Hvilket år er du født? ') )

# Beregne alder i 2024:
alder_2024 = 2024 - alder

# Skrive ut resultat: 
print(f'I 2024 blir du {alder_2024} år gammel.')
