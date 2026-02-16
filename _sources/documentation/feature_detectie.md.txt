# Feature detectie

## Inleiding
In deze sectie behandelen we technieken voor het detecteren van specifieke kenmerken in afbeeldingen, zoals hoeken, randen en andere opvallende punten. Feature detectie is een cruciaal onderdeel van veel computer vision-toepassingen, waaronder objectherkenning, beeldregistratie en 3D-reconstructie. We zullen verschillende algoritmen bespreken die worden gebruikt voor feature detectie, zoals Harris Corner Detection, SIFT (Scale-Invariant Feature Transform) en ORB (Oriented FAST and Rotated BRIEF), evenals hun implementaties met behulp van de OpenCV-bibliotheek.

## Opdrachten

Download voor deze opdrachten de afbeelding `pills-in-strip.jpg` vanaf de volgende link:[pills-in-strip.jpg](https://raw.githubusercontent.com/AvansMechatronica/CursusSupport/main/images/pills-in-strip.jpg)

> Om je pythonscript leesbaar en onderhoudbaar te houden, is het aan te raden om functies te gebruiken voor verschillende onderdelen van je code. Bijvoorbeeld een functie voor het inlezen en weergeven van de afbeelding, een functie voor het uitvoeren van de kleurconversie, en aparte functies voor elke blobdetectiemethode.

### Opdracht 1: Afbeelding inlezen en weergeven met GUI
Maak een Python script dat de afbeelding `pills-in-strip.jpg` inleest en weergeeft. Gebruik hiervoor de OpenCV bibliotheek.
Maak hiervoor een grafische gebruikersinterface (GUI) met bv. easygui, waarin de gebruiker een afbeelding kan selecteren vanaf zijn computer.

### Opdracht 2: Grijswaarden conversie
Voer op de ingelezen afbeelding een kleurconversie naar een grijswaarden afbeelding uit. Gebruik hiervoor de functie `cv2.cvtColor()` met de parameter `cv2.COLOR_BGR2GRAY`. Geef de resulterende grijswaarden afbeelding weer. 

### Opdracht 3: Harris Corner Detection
Implementeer de Harris Corner Detection op de grijswaarden afbeelding. Gebruik hiervoor de functie `cv2.cornerHarris()`. Markeer de gedetecteerde hoeken op de originele afbeelding en geef deze weer.  

### Opdracht 4: SIFT Feature Detection
Gebruik de SIFT (Scale-Invariant Feature Transform) methode om kenmerken in de grijswaarden afbeelding te detecteren. Gebruik hiervoor de functie `cv2.SIFT_create()` om een SIFT detector te maken en vervolgens `detectAndCompute()` om de kenmerken en hun descriptors te verkrijgen. Teken de gedetecteerde kenmerken op de originele afbeelding en geef deze weer. 

### Opdracht 5: ORB Feature Detection
Gebruik de ORB (Oriented FAST and Rotated BRIEF) methode om kenmerken in de grijswaarden afbeelding te detecteren. Gebruik hiervoor de functie `cv2.ORB_create()` om een ORB detector te maken en vervolgens `detectAndCompute()` om de kenmerken en hun descriptors te verkrijgen. Teken de gedetecteerde kenmerken op de originele afbeelding en geef deze weer.  

### Opdracht 6: Vergelijking van Feature Detection Methoden
Vergelijk de resultaten van de verschillende feature detectiemethoden (Harris, SIFT, ORB) en beschrijf de voor- en nadelen van elke methode. Welke methode presteert het beste voor de gegeven afbeelding en waarom?    

### Opdracht 7: Feature Matching tussen twee afbeeldingen
Download een tweede afbeelding die vergelijkbare kenmerken bevat als `pills-in-strip.jpg`. Gebruik S    IFT of ORB om kenmerken in beide afbeeldingen te detecteren en hun descriptors te verkrijgen. Gebruik vervolgens de functie `cv2.BFMatcher()` om de kenmerken tussen de twee afbeeldingen te matchen. Teken de overeenkomende kenmerken op een gecombineerde afbeelding en geef deze weer.  

### Opdracht 8: Feature Detectie op eigen afbeeldingen
Gebruik eigen afbeeldingen met verschillende kenmerken (zoals texturen, patronen, objecten) en pas  
de verschillende feature detectiemethoden toe. Analyseer en beschrijf hoe de verschillende methoden de afbeeldingen beïnvloeden en welke het meest effectief zijn voor jouw afbeeldingen.


