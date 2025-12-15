# Rekentool brandpuntsafstand 2.0

In deze uitgebreide versie van de brandpuntsafstand tool, ga je een Python-script schrijven dat niet alleen de brandpuntsafstand berekent, maar ook de sensorgrootte bepaalt op basis van de ingevoerde waarden. Je leert hoe je functies kunt gebruiken, invoervalidatie kunt implementeren, en hoe je een eenvoudige gebruikersinterface kunt maken.


## Opdracht 1: Bereken de sensorgrootte in mm
Maak een Python-script dat de gebruiker vraagt om de beeldbreedte, werkafstand en brandpuntsafstand in millimeters. 
Gebruik de volgende formule om de sensorgrootte te berekenen:

$$
\text{sensor\_breedte} = \frac{\text{beeld\_breedte} \times \text{brandpunts\_afstand}}{\text{werk\_afstand}}
$$

## Opdracht 2: Sensorgrootte berekenen met functie
Herschrijf de code van opdracht 1 zodat de berekening van de sensor_breedte in een functie wordt uitgevoerd. De functie moet drie parameters accepteren: beeld_breedte, werk_afstand en brandpunts_afstand. De functie moet de berekende sensorgrootte retourneren. De functie kan als volgt worden gedefinieerd:

```python
def bereken_sensor_breedte(beeld_breedte, werk_afstand, brandpunts_afstand)
```

> Let op: In de functie mogen geen invoer- of uitvoeropdrachten worden gebruikt. Alle invoer moet buiten de functie worden verzameld en alle uitvoer moet buiten de functie worden weergegeven.

## Opdracht 3: Herhaalde berekeningen
Maak het hoofdprogramma dusdagig dat het programma pas wordt afgesloten als de gebruiker ervoor kiest om te stoppen. Na elke berekening moet de gebruiker worden gevraagd of hij/zij nog een berekening wil uitvoeren.

## Opdracht 4: Invoervalidatie
Voeg invoervalidatie toe aan je script om ervoor te zorgen dat de gebruiker alleen positieve numerieke waarden invoert voor beeld_breedte, werk_afstand en brandpunts_afstand. Als de gebruiker ongeldige invoer geeft, moet het script een foutmelding weergeven en de gebruiker opnieuw om invoer vragen.
> Tip: Maak gebruik van `if` of `while` statements om de invoer te valideren.

## Opdracht 5: Sensor-matching met dictionary
Er zijn een aantal voorgedefinieerde sensorformaten met hun bijbehorende breedtes in millimeters. Voeg deze informatie toe aan je script als een dictionary:

```python
sensor_size = {
    "1/4 inch": 3.6,
    "1/3 inch": 4.8,
    "1/2 inch": 6.4,
    "1/1.8 inch": 7.1,
    "2/3 inch": 8.8,
    "1 inch": 12.8,
}
```

Wijzig je programma zodat het, na het berekenen van de sensorgrootte, het meest overeenkomstige sensorformaat uit de dictionary zoekt en dit formaat samen met de berekende sensorgrootte weergeeft.

## Opdracht 6: Grafische gebruikersinterface
Maak een grafische gebruikersinterface (GUI) voor je programma met behulp van een bibliotheek zoals Tkinter of EasyGUI. De GUI moet invoervelden bevatten voor beeld_breedte, werk_afstand en brandpunts_afstand, evenals een knop om de berekening uit te voeren en een gebied om de resultaten weer te geven.

