# Basis beeldverwerking
In dit hoofdstuk leer je over:
- Beeldverwerking met OpenCV
## Opdrachten

### Opdracht 1: Beelden inlezen en weergeven
<!-- Hier komt de inhoud van opdracht 1 -->
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


### Opdracht 2: Filters en transformaties
<!-- Hier komt de inhoud van opdracht 2 -->

### Opdracht 3: Feature detectie
<!-- Hier komt de inhoud van opdracht 3 -->

### Opdracht 4: Object detectie
<!-- Hier komt de inhoud van opdracht 4 -->
