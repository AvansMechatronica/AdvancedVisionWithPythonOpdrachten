# Rekentool brandpuntsafstand
## Inleiding

Je gaat een Python-tool maken die de brandpuntsafstand van een lenzenstelsel berekent. De tool vraagt de gebruiker om drie waarden in te voeren:

•	Beeldbreedte (de breedte van het object dat je wilt vastleggen, in mm of cm)

•	Sensorbreedte (de breedte van de camerasensor, in mm)

•	Werkafstand (de afstand tussen de lens en het object, in mm of cm)

Met deze waarden berekent de tool de brandpuntsafstand (f) van de lens met behulp van de formule:

$$
f = \frac{\text{sensorbreedte} \times \text{werkafstand}}{\text{beeldbreedte}}
$$

De tool moet de volgende stappen uitvoeren:
1.	Vraag de gebruiker om de beeldbreedte, sensorbreedte en werkafstand in te voeren.
2.	Bereken de brandpuntsafstand met de gegeven formule.
3.	Print de berekende brandpuntsafstand naar de gebruiker.

Deze opdracht helpt je om vertrouwd te raken met het verwerken van gebruikersinvoer, het uitvoeren van berekeningen en het weergeven van resultaten in Python.

Je maakt nog alleen maar gebruik van de input en print functies van Python.`

```python
# Voorbeeld van hoe input en output eruit kunnen zien
beeldbreedte = float(input("Voer de beeldbreedte in (mm of cm): "))
print("Beeldbreedte: ", beeldbreedte)
```


## Opdrachten

## Opdracht 1: 
Implementatieer de tool in Python. Zorg ervoor dat je de invoer van de gebruiker correct verwerkt en dat de berekening nauwkeurig is.

## Opdracht 2:
Test de tool met verschillende invoerwaarden om ervoor te zorgen dat deze correct werkt. Documenteer je testgevallen en de bijbehorende resultaten.

## Opdracht 3(uitdaging):
Maak het programma zodanig dat je steeds weer een nieuwe berekening kunt uitvoeren, zonder dat het programma stopt.
> Tip: maak gebruik van een while statement.

## Opdracht 4(uitdaging):
Maak het programma zodanig dat het programma stopt zodra je een ‘x’ hebt ingevoerd.
> Tip: maak gebruik van een if statement.

## Opdracht 5(extra-uitdaging):
Maak voor je programma een grafische-userinterface b.v. met de  'easygui' bibliotheek. 

> Tip: zie https://pypi.org/project/easygui/

> Opmerking: Voor deze opdrachten is het belangrijk dat je de basisprincipes van Python begrijpt, zoals variabelen, gebruikersinvoer, en eenvoudige wiskundige berekeningen. Als je nog niet vertrouwd bent met deze concepten, raad ik aan om eerst een inleidende Python-cursus te volgen voordat je aan deze opdrachten begint.

```python
# Voorbeeld van hoe input en output eruit kunnen zien in easygui
import easygui
import sys

# Vraag de gebruiker om de beeldbreedte in te voeren
beeld_breedte = easygui.enterbox(
    "Voer de **Beeldbreedte** in (mm of cm):",
    "Invoer Beeldbreedte"
)

easygui.msgbox(f"Beeldbreedte: {beeld_breedte}", "Invoer Bevestigd")
```


