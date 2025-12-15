# Filters

In deze sectie behandelen we verschillende soorten filters die vaak worden gebruikt in de beeldverwerking. Filters worden toegepast om bepaalde kenmerken van een afbeelding te benadrukken of te onderdrukken, zoals ruis, randen of texturen. We zullen zowel lineaire als niet-lineaire filters bespreken, evenals hun toepassingen en implementaties met behulp van de OpenCV bibliotheek.

## Inleiding
Filters zijn essentiële hulpmiddelen in de beeldverwerking die worden gebruikt om afbeeldingen te verbeteren of specifieke kenmerken te extraheren. Lineaire filters, zoals gemiddelde- en Gaussiaanse filters, worden vaak gebruikt voor ruisonderdrukking en het gladmaken van afbeeldingen. Niet-lineaire filters, zoals mediane filters, zijn effectief bij het verwijderen van impulsruis zonder de randen van objecten te vervagen. Daarnaast zijn er speciale filters zoals Sobel- en Laplace-filters die worden gebruikt voor randdetectie. In deze sectie zullen we deze verschillende soorten filters verkennen, hun werking uitleggen en praktische voorbeelden geven van hoe ze kunnen worden toegepast met behulp van OpenCV.

## Opdrachten

Download voor deze opdrachten de afbeelding `stars_1.png` vanaf de volgende link:
> Juiste bestand URL nog maken!!!!!!
https://raw.githubusercontent.com/AvansMechatronica/CursusSupport/main/images/stars_1.png

### Opdracht 1:
Maak een Python script dat de afbeelding `stars_1.png` inleest en weergeeft. Gebruik hiervoor de OpenCV bibliotheek.
Maak hiervoor een grafische gebruikersinterface (GUI) met bv. easygui, waarin de gebruiker een afbeelding kan selecteren vanaf zijn computer.

### Opdracht 2:
Voer op de ingelezen afbeelding een color conversie naar een grijswaarden afbeelding uit. Gebruik hiervoor de functie `cv2.cvtColor()` met de parameter `cv2.COLOR_BGR2GRAY`. Geef de resulterende grijswaarden afbeelding weer.

### Opdracht 3:
Pas een gemiddelde filter toe op de grijswaarden afbeelding om ruis te verminderen. Gebruik hiervoor de functie `cv2.blur()` met een kernelgrootte van (5,5). Geef de gefilterde afbeelding weer.   

### Opdracht 4:
Pas een Gaussiaanse filter toe op de grijswaarden afbeelding om ruis te verminderen. Gebruik hiervoor de functie `cv2.GaussianBlur()` met een kernelgrootte van (5,5) en een sigma van 0. Geef de gefilterde afbeelding weer.   

### Opdracht 5:
Pas een mediane filter toe op de grijswaarden afbeelding om impulsruis te verwijderen. Gebruik hiervoor de functie `cv2.medianBlur()` met een kernelgrootte van 5. Geef de gefilterde afbeelding weer.  

### Opdracht 6:
Voer een Sobel-randdetectie uit op de grijswaarden afbeelding. Gebruik hiervoor de functie `cv2.Sobel()` om de randen in zowel de x- als y-richting te detecteren. Combineer de resultaten en geef de resulterende afbeelding weer.

### Opdracht 7:
Voer een Laplace-randdetectie uit op de grijswaarden afbeelding. Gebruik hiervoor de functie `cv2.Laplacian()`. Geef de resulterende afbeelding weer.   

### Opdracht 8:
Vergelijk de resultaten van de verschillende filters (gemiddelde, Gaussiaans, mediaan, Sobel, Laplace) en beschrijf de effecten die ze hebben op de afbeelding. Welke filter is het meest effectief voor het verminderen van ruis? Welke filter is het meest effectief voor het detecteren van randen?  

### Opdracht 9:
Gebruik eigen afbeeldingen met verschillende kenmerken (zoals ruis, scherpe randen, zachte randen) en pas de verschillende filters toe. Analyseer en beschrijf hoe de verschillende filters de afbeeldingen beïnvloeden.

### Opdracht 10 (uitdaging):
Maak een interactief (GUI)script waarbij je de volgende invoervelden hebt:  
* Selectie van het bestand (gebruik bijvoorbeeld `easygui.fileopenbox()`).
* Keuze van het type filter (gemiddelde, Gaussiaans, mediaan, Sobel, Laplace).
* Invoer van de benodigde parameters voor het gekozen filter (zoals kernelgrootte, sigma, etc.).
Voer het geselecteerde filter uit op de afbeelding met de opgegeven parameters en geef het resultaat weer.



