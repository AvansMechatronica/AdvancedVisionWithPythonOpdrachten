# Uitrollen van een Neuraal Netwerk

## Inleiding
In deze sectie leer je hoe je een getraind neuraal netwerk kunt uitrollen en gebruiken voor inferentie (voorspellingen) op beelden uit een bestand of van een live video stream, zoals een webcam. We maken gebruik van het YoloV8 model voor deze opdrachten.

## Opdrachten
#### Opdracht 1: Voorbereiden van het Getrainde Model
Zorg ervoor dat je het getrainde model (`best.pt`) hebt dat je hebt verkregen na het trainen van je neuraal netwerk. Dit bestand is essentieel voor het uitvoeren van inferentie. Je hebt dit al verkregen in de vorige sectie over het trainen van een neuraal netwerk. Zoek het bestand op je computer.

> Als je getraind hebt met behulp van een colab notebook, zorg er dan voor dat je het model hebt gedownload van je Google Drive naar je lokale computer.

#### Opdracht 2: Detectie van objecten in Afbeeldingen uit een Bestand
1. Maak een Python script genaamd `DetectFromFile.py`.
2. Importeer de benodigde bibliotheken, zoals `ultralytics` voor YoloV8 en `cv2` voor beeldverwerking.
```python
from ultralytics import YOLO
```
3. Laad het getrainde model (`best.pt`) in je script. Gebruik hiervoor de volgende functie:
```python
model = YOLO('bestandspad_naar_best.pt')
```

4. Schrijf code om een afbeelding te laden vanaf je computer en voer inferentie uit met het geladen model.

5. Detecteer de objecten met de volgende functie:
```python
results = model()
``` 
6. Druk de resultaten af in een terminal en evalueer de waardes uit de resultaten. Gebruik hiervoor de volgende code:
```python
for result in results:
    print(result)
``` 
7. Gebruik de resultaten om de gedetecteerde objecten van bounding boxes te voorzien en daarbij het label en confidence score weer te geven.


#### Opdracht 3: Detectie van objecten in een Live Webcam Stream
1. Maak een Python script genaamd `DetectFromWebcam.py`.
2. Maak het programma zodanig dat je de webcam van je computer gebruikt om een live video stream te verkrijgen, waarbij live inferentie wordt uitgevoerd met het getrainde model.

Je hebt nu geleerd hoe je een getraind neuraal netwerk kunt uitrollen en gebruiken voor objectdetectie in zowel afbeeldingen uit een bestand als in een live webcam stream. Experimenteer met verschillende beelden en video streams om de prestaties van je model te evalueren!
