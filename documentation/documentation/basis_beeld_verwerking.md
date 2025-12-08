# Basis beeldverwerking

In deze module leer je de basisprincipes van beeldverwerking met behulp van de OpenCV bibliotheek in Python. We behandelen het inlezen, weergeven, bewerken en analyseren van afbeeldingen. Er worden in deze opdrachten allen verwijzingen gegeven naar welke functies je zou kunnen toepassen. Zelf dien je dan uit te zoeken hoe je deze functies precies toepast. 
Je kunt hiervoor de officiële documentatie van OpenCV raadplegen: https://www.geeksforgeeks.org/python/opencv-python-tutorial/

## Opdrachten

### Opdracht 1: Beelden inlezen en weergeven

Maak een pythhon script in pyCharm die een afbeelding inleest, en vervolgens in een nieuw venster weergeeft. 
Doe dat in de volgende stappen:
1. Maak een nieuw python project aan in PyCharm op een voor jou bekende plaats op je computer.
2. Maak in het project een nieuwe map met de naam `images`.
3. Installeer de OpenCV bibliotheek via pip als je dat nog niet gedaan hebt (in de terminal van PyCharm):
   ```bash
   pip install opencv-python
   ```
4. Download de afbeelding `00-puppy.jpg` vanaf de volgende link: 
   https://raw.githubusercontent.com/AvansMechatronica/CursusSupport/main/images/00-puppy.jpg

   Sla de afbeelding op in de `images` map.

5. Maak een nieuw python bestand aan met de naam `opencv_image_display.py`. 
6. Voeg python code toe die de volgende stappen uitvoert:
* Importeer de OpenCV bibliotheek met
```python
import cv2
```

* Lees de afbeelding in een varaible `img` vanuit de `images` map, gebruikmakend van
```python
cv2.imread()
```

* Toon de afbeelding in een nieuw venster, gebruikmakend van
```python
cv2.imshow()
```
* Wacht tot een toets wordt ingedrukt met
```python
cv2.waitKey(0)
```

* Sluit alle geopende vensters met
```python
cv2.destroyAllWindows()
```

7. Test je script door het uit te voeren en controleer of de afbeelding correct wordt weergegeven in een nieuw venster. Wat valt je op over de kleuren van de afbeelding?
> OpenCV leest afbeeldingen standaard in het BGR-kleurformaat in, wat kan resulteren in afwijkende kleuren bij weergave.

Je kunt de kleuren corrigeren door de afbeelding om te zetten naar het RGB-kleurformaat met behulp van de volgende functie:
```python
img_rgb = cv2.cvtColor()
```
Gebruik voor de conversie de `cv2.COLOR_BGR2RGB` parameter in de `cv2.cvtColor()` functie.

8. Pas je script aan om de afbeelding in het RGB-kleurformaat weer te geven en test het opnieuw.

### Opdracht 2: Elementen aan de afbeelding toevoegen
Bewerk de afbeelding door tekst en een rechthoek toe te voegen. Volg de onderstaande stappen:
1. Open het eerder gemaakte `opencv_image_display.py` bestand.
2. Voeg rechthoek toe aan de afbeelding met behulp van
```python
cv2.rectangle()
```
3. Voeg tekst toe aan de afbeelding met behulp van
```python
cv2.putText()
```

4. Test je script door het uit te voeren en controleer of de rechthoek en tekst correct worden weergegeven op de afbeelding.

### Opdracht 3: Beeld opslaan
Schrijf een script dat de bewerkte afbeelding opslaat. Volg de onderstaande stappen:
1. Open het eerder gemaakte `opencv_image_display.py` bestand. 
2. Voeg code toe om de bewerkte afbeelding op te slaan in de `images` map met een nieuwe naam, bijvoorbeeld `00-puppy-edited.jpg`, gebruikmakend van
```python
cv2.imwrite()
```

### Opdracht 4: Informatie over de afbeelding verkrijgen
Schrijf een script dat informatie over de afbeelding verkrijgt en weergeeft. Volg de onderstaande stappen:
1. Open het eerder gemaakte `opencv_image_display.py` bestand.
2. Voeg code toe om de volgende informatie over de afbeelding te verkrijgen:
   * Afmetingen (hoogte, breedte, aantal kanalen)
   * Datatype van de pixelwaarden
gebruik daarvoor de volgende code:
```python
dimensions = img.shape
height = dimensions[0]
width = dimensions[1]
channels = dimensions[2]
```
3. Print deze informatie naar de console.
4. Test je script door het uit te voeren en controleer of de juiste informatie wordt weergegeven in de console.
5. Maak van deze functionalistet een functie genaamd `print_image_info(img)` die je kunt hergebruiken in andere opdrachten die hierop volgen

### Opdracht 5: Beeld scalen
Schrijf een script dat de afbeelding schaalt naar een nieuwe grootte. Volg de onderstaande stappen:
1. Open het eerder gemaakte `opencv_image_display.py` bestand.
2. Voeg code toe om de afbeelding te schalen naar een nieuwe grootte, bijvoorbeeld 300x300 pixels, met behulp van

```python
cv2.resize()
```

3. Toon de geschaalde afbeelding in een nieuw venster.
4. Test je script door het uit te voeren en controleer of de afbeelding correct is geschaald en weergegeven. Doe dat voor verschillende schalingsfactoren. Gebryuik ook de `print_image_info(img)` functie om de nieuwe afmetingen van de afbeelding te controleren.

### Opdracht 6: Beeld conversie naar grijswaarden
Schrijf een script dat de afbeelding converteert naar grijswaarden. Volg de onderstaande stappen:
1. Open het eerder gemaakte `opencv_image_display.py` bestand. 
2. Voeg code toe om de afbeelding te converteren naar grijswaarden met behulp van
```python
img_gray = cv2.cvtColor()
```
Zoek zelf uit weleke parameter je hiervoor moet gebruiken.

3. Toon de grijswaarden afbeelding in een nieuw venster.
4. Test je script door het uit te voeren en controleer of de afbeelding correct is geconverteerd en weergegeven.

### Opdracht 7: Histogram van de afbeelding weergeven
Schrijf een script dat het histogram van de afbeelding weergeeft. Volg de onderstaande stappen:
1. Maak een nieuw python bestand aan met de naam `opencv_image_histogram.py`.
2. Download de afbeelding `auto.jpg` vanaf de volgende link: 
   https://github.com/AvansMechatronica/CursusSupport/blob/main/images/auto.jpg

   Sla de afbeelding op in een nieuwe map `images` binnen je project.

3. Maak het programma zo dat de aflbeelding van d auto in grijswaarden wordt getoond

4. Voeg code toe om het histogram van de afbeelding te berekenen en weer te geven met behulp van
```python
   cv2.calcHist()
```
   Druk de waardes van het histogram af in de console.

5. Gebruik eventueel de `matplotlib` bibliotheek om het histogram grafisch weer te geven. Installeer deze bibliotheek via pip als je dat nog niet gedaan hebt:
   ```bash
   pip install matplotlib
   ```
   Zet vervolgens de volgende code op de juiste plek in je script om het histogram weer te geven:
   ```python
   import matplotlib.pyplot as plt

   plt.plot(histogram)
   plt.title('Histogram')
   plt.xlabel('Pixelwaarde')
   plt.ylabel('Aantal pixels')
   plt.show()
   ```   

6. Test je script door het uit te voeren en controleer of het histogram correct wordt weergegeven.

7. Test het programma ook met de volgende afbeedlingen:
   * https://github.com/AvansMechatronica/CursusSupport/blob/main/images/veel%20contrast.jpg
   * https://github.com/AvansMechatronica/CursusSupport/blob/main/images/weinig%20contrast.jpg

Wat valt je op aan de histogrammen van deze afbeeldingen? Hoe verhouden deze zich tot de visuele waarneming van de afbeeldingen?
