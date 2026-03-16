# Verzamelen van Afbeeldingen

## Inleiding

In deze sectie leer je hoe je een dataset van afbeeldingen kunt verzamelen die nodig is voor het trainen van een neuraal netwerk voor beeldherkenningstaken. We zullen verschillende methoden bespreken om afbeeldingen te verzamelen, waaronder webscraping, gebruik van bestaande datasets, en handmatige fotografie.

## Opdrachten

### Opdracht 1: Fotograferen van Afbeeldingen
In deze opdracht ga je zelf afbeeldingen maken met de camera van de eindopdracht. Maak minimaal 50 afbeeldingen van elk object dat je wilt herkennen. Zorg ervoor dat je de afbeeldingen onder verschillende omstandigheden maakt, zoals verschillende hoeken, belichting, en achtergronden.
Kies in ieder geval 6 verschillende objecten om te fotograferen. Je mag natuurlijk ook de objecten gebruiken die je in de eindopdracht gaat gebruiken.

Verzamel alle afbeeldingen in een aparte map op je computer, bijvoorbeeld `dataset/raw_images/`.

:::{tip}
1. Om de kwaliteit van de afbeeldingen te waarborgen, is het belangrijk dat je dezelfde camera gebruikt voor zowel het verzamelen van de afbeeldingen als voor het uitrollen van het model in je eindapplicatie. Dit zorgt ervoor dat de afbeeldingen vergelijkbaar zijn in termen van resolutie, kleurweergave, en andere kenmerken.
2. Beperk de resolutie van de afbeeldingen, tot bijvoorbeeld 640x480 pixels, om opslagruimte te besparen en de verwerkingstijd te verminderen.
3. Maak zelf een Python-script dat automatisch de afbeeldingen van de camera opslaat in de juiste map, bijvoorbeeld `dataset/raw_images/`, en zorg ervoor dat de bestandsnamen uniek zijn (bijvoorbeeld door een timestamp toe te voegen). Zorg ervoor dat bestandsnamen geen spaties bevatten, maar gebruik in plaats daarvan underscores (_) of koppeltekens (-) om de leesbaarheid te verbeteren.
:::

