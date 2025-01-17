"""
Arbeidskrav 2 - PY1010-1 24H Grunnleggende programmering med Python
@author: Anne-Marie Myhrvold
"""

# Oppgave 1) 
# Program som regner ut hvor gammel en person er i 2024 og skriver ut resultatet

# Be om fødselsår:
alder = int(input('Hvilket år er du født? ') )

# Beregne alder i 2024:
alder_2024 = 2024 - alder

# Skrive ut resultat: 
print(f'I 2024 blir du {alder_2024} år gammel.')

# ------------------------------------------------------------------
# Oppgave 2) Program som beregner hvor mye pizza som må kjøpes inn

import math

#Antall elever
antall_elever = int(input('Skriv inn antall elever: '))

#beregne antall pizza
antall_pizza = math.ceil(antall_elever / 4)

#Skrive ut resultat
print(f'Det må handles inn {antall_pizza} pizzaer til klassefesten')

# ------------------------------------------------------------------
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

# ------------------------------------------------------------------
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

# ------------------------------------------------------------------
# Oppgave 5 program som regner ut areal og omkrets til en figur som er satt sammen av em rettvinklet trekant og en halvsirkel.

import numpy as np

# definisjon av funksjon 
def fun_areal_og_omkrets(a, b): 
    areal_trekant = (a * b) / 2  #beregner areal av trekanten
    radius = a / 2  #beregner radius av sirkelen
    areal_halvsirkel = (np.pi * radius **2) / 2 #beregner areal av halvsirkel
    totalt_areal = areal_trekant + areal_halvsirkel #beregner totalt areal av figuren
    omkrets_halvsirkel = np.pi * radius #beregner omkrets halvsirkel
    hypotenus = np.sqrt(a ** 2 + b ** 2) #finner hypotenusen i den rettvinklede trekanten. Kvadratroten av a^2 + b2
    ytre_omkrets = a + b + hypotenus + omkrets_halvsirkel
    return totalt_areal, ytre_omkrets
    
# Be om verdier
print(f'Programmet regner ut areal og omkrets av en figur som er satt sammen av en rettvinklet trekant og en halvsirkel')
a = float(input('Registrer verdi a: ')) 
b = float(input('Registrer verdi b: '))

areal, omkrets = fun_areal_og_omkrets(a, b) #beregne areal og omkrets

#Skrive ut resultater
print(f'Arealet av figuren er {areal:.2f} kvadratmeter.')
print(f'Omkretsen av figuren er {omkrets:.2f} meter ')

# ------------------------------------------------------------------
# Oppgave 6 Program som plotter en funksjon i et gitt intervall

import numpy as np
import matplotlib.pyplot as plt

#array med 200 punkter fordelt jevnt på intervallet mellom [-10,10]
x = np.linspace(-10, 10, 20)

#definere funksjonen f(x)
def fun(x):
    y = -x ** 2 - 5
    return y

y = fun(x)

#plotte funksjonen
plt.xlabel("x")
plt.ylabel("y")
plt.plot(x, y)

