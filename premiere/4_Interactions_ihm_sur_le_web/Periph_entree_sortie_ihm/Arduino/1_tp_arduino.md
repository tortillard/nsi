# TP Arduino - Branchement d'une LED  

Ce TP à pour but de se familiariser avec l'équipement Arduino.  
Dans un premier temps nous allons effectuer le branchement nécessaire pour l'allumage d'une LED.  

## L'alimentation 
Afin d'allumer une led nous allons nous servir de la carte Arduino comme source d'alimentation.   

Pour cela, prenez les cables Dupont (aussi appelés "F-M cables").   
Branchez sur la carte Arduino,   
- Un fil(généralement rouge) sur la tension 5V  
- Un autre fil(généralement noir) sur GND  

## Reliage à la patine  
Sur la patine un groupe de 5 noeuds(a,b,c,d et e) sur une même ligne sont tous alimentés de la même manière.  

Le fil rouge et le fil noir doivent être branchées sur un groupe de 5 pin différent. 

Par exemple, branchez

- Le fil rouge sur le pin A19   
- Le fil noir sur le pin B13  


## La résistance  

> [!WARNING] Attention !
> Avant de relier notre branchement à la LED il faut utiliser une **résistance** !
> Car ...

Branchez une extrémité de la résistance sur la Patine en B19 par exemple, et l'autre extrémité en C14.  

## La led
Enfin branchez la led, attention il ne faut pas se tromper de sens 
l'anode jambe longue va en E14 et la cathode en E13

## Notes 
- sans résistance la LED grille, la résistance permet d'absorber une partie de la tension 
- anode jambe longue, cathode jambe courte
- le courant passe par l'anode(+) et repart par la cathode(-)
