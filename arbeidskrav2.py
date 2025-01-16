#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Arbeidskrav 2 - PY1010-1 24H Grunnleggende programmering med Python

@author: Anne-Marie Myhrvold
"""

# Oppgave 1) Program som regner ut hvor gammel en person er i 2024 og skriver ut resultatet

# Be om fødselsår:
alder = int(input('Hvilket år er du født? ') )

# Beregne alder i 2024:
alder_2024 = 2024 - alder

# Skrive ut resultat: 
print(f'I 2024 blir du {alder_2024} år gammel.')

# Oppgave 2) Program som beregner hvor mye pizza som må kjøpes inn

import math

#Antall elever
antall_elever = int(input('Skriv inn antall elever: '))

#beregne antall pizza
antall_pizza = math.ceil(antall_elever / 4)

#Skrive ut resultat
print(f'Det må handles inn {antall_pizza} pizzaer til klassefesten')

# Oppgave 3) Program med en funksjon som regner om fra grader til radianer

import numpy as np

def fun_grad_til_radianer(v_grad):
    #beregne radianer
    v_rad = v_grad * np.pi /180
    return v_rad
    
    
#be om gradtallet
v_grad = float(input('Skriv inn gradtallet:' ))

#omregne fra grad til radianer
v_rad = fun_grad_til_radianer(v_grad)

#skrive resultat
print(f' Vinkelen {v_grad} grader er {v_rad} radianer')

# Oppgave 4) 
# a) Opprette Dictionary
data = {
    'Norge': {'hovedstad': "Oslo", 'innbyggere': 0.634},
    'Sverige': {'hovedstad': 'Stockholm', 'innbyggere': 1.515},
    'Danmark': {'hovedstad': 'København', 'innbyggere': 1.336},
    'England': {'hovedstad': 'London', 'innbyggere': 8.982},
    'Frankrike': {'hovedstad': 'Paris', 'innbyggere': 2.161},
    'Italia' : {'hovedstad': 'Roma', 'innbyggere': 2.873}
    }

# b) Program hvor bruker skriver et land og skriver ut info om det

#Be om land
land = input('Skriv inn et land: ')

#Sjekk om land finnes, skriv ut informasjon eller feilmelding
if land in data:
    hovedstad = data[land]['hovedstad']
    innbyggere = data[land]['innbyggere']
    print(f'{hovedstad} er hovedstaden i {land} og det er {innbyggere} mill. innbyggere i {hovedstad}')
else:
    print(f'Landet {land} er ikke registrert i dictionaryen')

# c) Legge til data info om nytt land i dictionary

#skriv inn land
reg_land = input('Skriv inn landet du vil registrere: ')

#Sjekk om land finnes,
if reg_land in data:
    print(f'{reg_land} er allerede registret i dictionaryen')
else:
    hovedstad = input(f'Registrer hovedstad i {reg_land}: ')
    innbyggere = float(input(f'Registrer antall innbyggere i {hovedstad} (i mill) : '))
    
#legge til nytt land
    data[reg_land] = {'hovedstad': hovedstad, 'innbyggere': innbyggere}
    print(f'Nytt land lagt til: {data}')

# Oppgave 5)

# Oppgave 6)

