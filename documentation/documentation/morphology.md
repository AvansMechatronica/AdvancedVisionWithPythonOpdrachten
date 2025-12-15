# Morphology

In deze sectie behandelen we morfologische bewerkingen die vaak worden gebruikt in de beeldverwerking. Morfologie is een verzameling van niet-lineaire bewerkingen die gebaseerd zijn op de vorm van structuren in een afbeelding. De meest gebruikte morfologische operaties zijn erosie, dilatatie, opening en sluiting.

## Inleiding

Morfologische bewerkingen zijn technieken in de beeldverwerking die gebaseerd zijn op de vorm en structuur van objecten in een afbeelding. Ze worden vaak toegepast op binaire afbeeldingen om ruis te verwijderen, objecten te scheiden of juist te verbinden, en om de structuur van objecten te analyseren. De belangrijkste morfologische operaties zijn erosie (het verkleinen van objecten), dilatatie (het vergroten van objecten), opening (ruis verwijderen) en sluiting (gaten opvullen). Deze bewerkingen zijn essentieel bij het voorbereiden van afbeeldingen voor verdere analyse, zoals objectherkenning of contourdetectie.
## Opdrachten

Download voor deze opdrachten de afbeelding `stars_1.png` vanaf de volgende link:

https://raw.githubusercontent.com/AvansMechatronica/CursusSupport/main/images/stars_1.png

### Opdracht 1:
Maak een Python script dat de afbeelding `stars_1.png` inleest en weergeeft. Gebruik hiervoor de OpenCV bibliotheek.

### Opdracht 2:
Voer op de ingelezen afbeelding een color conversie naar een grijswaarden afbeelding uit. Gebruik hiervoor de functie `cv2.cvtColor()` met de parameter `cv2.COLOR_BGR2GRAY`. Geef de resulterende grijswaarden afbeelding weer.

### Opdracht 3:
Voer een drempelbewerking (thresholding) uit op de grijswaarden afbeelding om een binaire afbeelding te verkrijgen. Gebruik hiervoor de functie `cv2.threshold()`. Experimenteer met verschillende drempelwaarden en geef de binaire afbeelding weer.

### Opdracht 4:
Maak een structurerend element (kernel) aan met behulp van numpy, bijvoorbeeld een vierkante kernel van 5x5 pixels:

```python
import numpy as np
kernel = np.ones((5,5), np.uint8)
```

### Opdracht 5:
Voer een erosie uit op de binaire afbeelding met behulp van de functie `cv2.erode()`. Experimenteer met verschillende structurerende elementen (kernels) en geef de geërodeerde afbeelding weer.

### Opdracht 6:
Voer een dilatatie uit op de binaire afbeelding met behulp van de functie `cv2.dilate()`. Experimenteer met verschillende structurerende elementen (kernels) en geef de gedilateerde afbeelding weer.

### Opdracht 7:
Voer een opening uit op de binaire afbeelding met behulp van de functie `cv2.morphologyEx()` met de parameter `cv2.MORPH_OPEN`. Geef de resulterende afbeelding weer.

### Opdracht 8:
Voer een sluiting uit op de binaire afbeelding met behulp van de functie `cv2.morphologyEx()` met de parameter `cv2.MORPH_CLOSE`. Geef de resulterende afbeelding weer.

### Opdracht 9:
Vergelijk de resultaten van de verschillende morfologische bewerkingen en beschrijf de effecten die ze hebben op de binaire afbeelding. Welke bewerking is het meest geschikt voor het verwijderen van ruis? Welke bewerking is het meest geschikt voor het verbinden van objecten in de afbeelding?

### Opdrcht 10:
Gebruik eigen afbeeldingen met verschillende kenmerken (zoals ruis, gaten, verbonden objecten) en pas de morfologische bewerkingen toe. Analyseer en beschrijf hoe de verschillende bewerkingen de afbeeldingen beïnvloeden.


### Opdracht 11 (uitdaging):
Maak een interactief (GUI)script waarbij je de volgende invoervelden hebt:
* Selectie van het bestand (gebruik bijvoorbeeld `easygui.fileopenbox()`).
* Invoer van dremplewaarde voor de binaire drempelbewerking.
* Keuze van de morfologische bewerking (erosie, dilatatie, opening, sluiting).
* Keuze van de grootte van het structurerend element (kernel).  
Voer de geselecteerde morfologische bewerking uit op de afbeelding met de opgegeven kernel grootte en geef het resultaat weer. 