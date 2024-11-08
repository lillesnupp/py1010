#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  5 18:47:50 2024

@author: anne-marie.myhrvold

Arbeidskrav 1 - PY1010-1 24H Grunnleggende programmering med Python
"""

Antall_km = 10000 #km/år = antall kjørte kilometer per år 
Forsikring_elbil = 5000 #kr/år = Forsikring Elbil per år
Forsikring_bensinbil = 7500 #kr/år = Forsikring Bensinbil per år
Trafikk_avg = 8.38 #kr/dag = Trafikkforsikringsavgift 
Forbruk_elbil = 0.2 #kWh/km = Drivstoffbruk Elbil
Stroempris = 2.0 #kr/kWh = Strømpris ved hjemmelading
Forbruk_bensinbil = 1.0 #kr/km = Drifstoffbruk Bensinbil
Bom_elbil = 0.1 #kr/km = Bomavgift Elbil
Bom_bensinbil = 0.3 #kr/km = Bomavgift Bensinbil

#felleskostnader
Kostnad_trafikkavg = Trafikk_avg*365

#Elbil kostnadsbereegning
Kostnad_forbruk_elbil = Antall_km * Forbruk_elbil * Stroempris
Kostnad_bom_elbil = Antall_km*Bom_elbil
Totalkostnad_elbil = Forsikring_elbil + Kostnad_trafikkavg + Kostnad_forbruk_elbil + Kostnad_bom_elbil

#Bensinbil kostnadsberegning
Kostnad_forbruk_bensinbil = Antall_km*Forbruk_bensinbil
Kostnad_bom_bensinbil = Antall_km*Bom_bensinbil
Totalkostnad_bensinbil = Forsikring_bensinbil + Kostnad_trafikkavg + Kostnad_forbruk_bensinbil + Kostnad_bom_bensinbil

#kostnadsdifferanse mellom elbil og bensinbil
Kostnadsdifferanse = Totalkostnad_bensinbil - Totalkostnad_elbil

#visning av resultater
print("Sammenligning av årlige kostnader foe Elbil sammenliknet med Bensinbil")
print("Årlige kosnader Elbil: ", Totalkostnad_elbil, " kr")
print("Årlige kostnader Bensinbil: ", Totalkostnad_bensinbil, " kr")
print("Kostnadsdifferanse: ", Kostnadsdifferanse, " kr")