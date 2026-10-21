# Blob detectie

In deze sectie behandelen we de concepten en technieken die worden gebruikt voor het detecteren van blobs in afbeeldingen. Blobs zijn gebieden in een afbeelding die verschillen van hun omgeving op basis van eigenschappen zoals helderheid, kleur of textuur. We zullen verschillende methoden voor blobdetectie bespreken, waaronder eenvoudige drempelwaarden, Laplacian of Gaussian (LoG), Difference of Gaussian (DoG) en Determinant of Hessian (DoH). Daarnaast zullen we praktische voorbeelden geven van hoe deze technieken kunnen worden geïmplementeerd met behulp van de OpenCV bibliotheek.

## Inleiding


## Opdrachten

Download voor deze opdrachten de afbeelding `pills-in-strip.jpg` vanaf de volgende link:[pills-in-strip.jpg](https://raw.githubusercontent.com/AvansMechatronica/CursusSupport/main/images/pills-in-strip.jpg)

> Om je pythonscript leesbaar en onderhpoudbaar te houden, is het aan te raden om functies te gebruiken voor verschillende onderdelen van je code. Bijvoorbeeld een functie voor het inlezen en weergeven van de afbeelding, een functie voor het uitvoeren van de kleurconversie, en aparte functies voor elke blobdetectiemethode.

### Opdracht 1: Afbeelding inlezen en weergeven met GUI
Maak een Python script dat de afbeelding `pills-in-strip.jpg` inleest en weergeeft. Gebruik hiervoor de OpenCV bibliotheek.
Maak hiervoor een grafische gebruikersinterface (GUI) met bv. easygui, waarin de gebruiker een afbeelding kan selecteren vanaf zijn computer.

### Opdracht 2: Grijswaarden conversie
Voer op de ingelezen afbeelding een kleurconversie naar een grijswaarden afbeelding uit. Gebruik hiervoor de functie `cv2.cvtColor()` met de parameter `cv2.COLOR_BGR2GRAY`. Geef de resulterende grijswaarden afbeelding weer.     

### Opdracht 3: Blob detectie met SimpleBlobDetector
Gebruik de OpenCV `SimpleBlobDetector` om blobs in de grijswaarden afbeelding te detecteren. Stel de parameters van de detector in om blobs te vinden op basis van grootte, circulariteit en andere kenmerken. Geef de gedetecteerde blobs weer door cirkels rond hen te tekenen op de originele afbeelding.    

#### Opdracht 3a: Parameterafstemming SimpleBlobDetector
Experimenteer met verschillende instellingen van de `SimpleBlobDetector` parameters, zoals `minThreshold`, `maxThreshold`, `filterByArea`, `minArea`, `filterByCircularity`, en andere. Observeer hoe deze wijzigingen de gedetecteerde blobs beïnvloeden en documenteer je bevindingen.

#### Opdracht 3b: Overlay van gedetecteerde blobs
Pas je script aan zodat de gedetecteerde blobs worden weergegeven als een overlay op de originele afbeelding. Gebruik verschillende kleuren of vormen om de blobs te markeren, afhankelijk van hun eigenschappen zoals grootte of circulariteit. Geef zowel de originele afbeelding als de afbeelding met de overlay weer in de GUI.

#### Opdracht 3c: Blob eigenschappen weergeven
Breid je script uit om de eigenschappen van elke gedetecteerde blob weer te geven, zoals hun coördinaten, grootte en circulariteit.

#### Opdracht 3d: Bepalen van het zwaartelpunt van blobs
Voeg functionaliteit toe aan je script om het zwaartepunt van elke gedetecteerde blob te berekenen en weer te geven. Markeer het zwaartepunt op de originele afbeelding en geef de coördinaten ervan weer in de GUI.

### Opdracht 4: Blob detectie met Laplacian of Gaussian (LoG)
Implementeer blobdetectie met behulp van de Laplacian of Gaussian (LoG) methode. Gebruik de functie `cv2.GaussianBlur()` om de afbeelding te vervagen en vervolgens de Laplacian operator toe te passen met `cv2.Laplacian()`. Identificeer de lokale maxima in het resultaat als blobs en geef deze weer op de originele afbeelding.   

### Opdracht 5: Blob detectie met Difference of Gaussian (DoG)
Implementeer blobdetectie met behulp van de Difference of Gaussian (DoG) methode. Maak twee vervaagde versies van de grijswaarden afbeelding met verschillende sigma-waarden en trek deze van elkaar af. Identificeer de lokale maxima in het resultaat als blobs en geef deze weer op de originele afbeelding.

### Opdracht 6: Blob detectie met Determinant of Hessian (DoH)
Implementeer blobdetectie met behulp van de Determinant of Hessian (DoH) methode. Bereken de Hessiaan matrix van de grijswaarden afbeelding en bepaal de determinant op elk pixel. Identificeer de lokale maxima in het resultaat als blobs en geef deze weer op de originele afbeelding.

### Opdracht 7: Vergelijking van blobdetectiemethoden
Vergelijk de resultaten van de verschillende blobdetectiemethoden (SimpleBlobDetector, LoG, DoG, DoH) en beschrijf de voor- en nadelen van elke methode. Welke methode presteert het beste voor de gegeven afbeelding en waarom?

### Opdracht 8: Blob detectie op eigen afbeeldingen
Gebruik eigen afbeeldingen met verschillende kenmerken (zoals ruis, scherpe randen, zachte randen) en pas de verschillende blobdetectiemethoden toe. Analyseer en beschrijf hoe de verschillende methoden de afbeeldingen beïnvloeden en welke het meest effectief zijn voor jouw afbeeldingen.


