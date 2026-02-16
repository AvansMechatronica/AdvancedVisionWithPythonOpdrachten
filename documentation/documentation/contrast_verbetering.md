# Contras verbetering/gamma correctie


## Inleing
In deze opdracht gaan we de contrast van een afbeelding verbeteren. We kunnen dit doen door middel van gamma correctie. Gamma correctie is een niet-lineaire operatie die wordt gebruikt om de helderheid van een afbeelding aan te passen. Het wordt vaak gebruikt om de details in donkere of lichte gebieden van een afbeelding te verbeteren.
De formule voor gamma correctie is als volgt:

```math
output\_pixel = 255 \times \left(\frac{input\_pixel}{255}\right)^{\gamma}
```

Waarbij `input_pixel` de waarde van een pixel in de originele afbeelding is, `output_pixel` de waarde van de pixel in de aangepaste afbeelding is, en `gamma` een parameter is die bepaalt hoe sterk de contrastverbetering is. Een gamma-waarde kleiner dan 1 zal de details in donkere gebieden verbeteren, terwijl een gamma-waarde groter dan 1 de details in lichte gebieden zal verbeteren.

Om gamma correctie toe te passen in Python, kunnen we de volgende code gebruiken:


## Opdrachten

Download voor deze opdrachten de afbeelding `veel contrast.jpg` vanaf de volgende link: [veel contrast.jpg](https://raw.githubusercontent.com/AvansMechatronica/CursusSupport/main/images/veel%20contrast.jpg)

> Om je pythonscript leesbaar en onderhoudbaar te houden, is het aan te raden om functies te gebruiken voor verschillende onderdelen van je code.

### Opdracht 1: Afbeelding inlezen en weergeven met GUI
Maak een Python script dat de afbeelding `veel contrast.jpg` inleest en weergeeft. Gebruik hiervoor de OpenCV bibliotheek.
Maak hiervoor een grafische gebruikersinterface (GUI) met bv. easygui, waarin de gebruiker een afbeelding kan selecteren vanaf zijn computer.

### Opdracht 2: Gamma correctie toepassen
Pas gamma correctie toe op de ingelezen afbeelding. Vraag de gebruiker om een gamma-waarde in te voeren en gebruik deze waarde om de contrastverbetering toe te passen. Geef de aangepaste afbeelding weer. 

### Opdracht 3: Verschillende gamma-waarden testen
Test de gamma correctie met verschillende gamma-waarden (bijvoorbeeld 0.5, 1.0, 2.0) en observeer hoe de contrastverbetering verandert. Beschrijf de effecten van verschillende gamma-waarden op de afbeelding.

### Opdracht 4: Zelf afbeeldingen testen
Gebruik zelfuitgezochtte afbeeldingen met verschillende kenmerken (zoals donkere afbeeldingen, lichte afbeeldingen, afbeeldingen met veel details) en pas gamma correctie toe. Analyseer en beschrijf hoe de verschillende gamma-waarden de afbeeldingen beïnvloeden.

### Opdracht 5 (uitdaging): Interactieve gamma correctie GUI
Maak een interactief (GUI)script waarbijje de gamma-waarde kunt aanpassen met een schuifbalk (slider) en de aangepaste afbeelding in realtime kunt bekijken. Gebruik hiervoor bijvoorbeeld de `cv2.createTrackbar()` functie van OpenCV.
