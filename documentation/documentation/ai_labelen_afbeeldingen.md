# Labelen van Afbeeldingen

## Inleiding
In deze sectie leer je hoe je de verzamelde afbeeldingen kunt labelen om ze geschikt te maken voor het trainen van een neuraal netwerk. Het labelen van afbeeldingen is een cruciale stap in het voorbereidingsproces van je dataset, omdat het het netwerk helpt te begrijpen welke objecten op de afbeeldingen aanwezig zijn.

We gebruiken een online omgeving van [roboflow](https://roboflow.com/) om de afbeeldingen te labelen. Volg de onderstaande stappen om je afbeeldingen te labelen:

Roboflow is een gebruiksvriendelijke tool die speciaal is ontworpen voor het beheren en labelen van datasets voor computer vision projecten. Het biedt een intuïtieve interface waarmee je snel en efficiënt afbeeldingen kunt labelen.

Ook kun je in Roboflow je dataset voorbereiden voor training, zoals het splitsen van de dataset in trainings-, validatie- en testsets, en het exporteren van de dataset in verschillende formaten die compatibel zijn met populaire machine learning frameworks.

Tevens kun je in Roboflow modellen trainen en evalueren, waardoor het een alles-in-één oplossing is voor je computer vision projecten.


## Roboflow
:::{caution}
Helaas is Roboflow niet gratis. Je kunt echter een gratis account aanmaken waarmee je een beperkt aantal afbeeldingen kunt labelen en beheren. Dit is meestal voldoende voor kleine projecten of om de tool uit te proberen voordat je besluit om te upgraden naar een betaald plan.
:::

## Alternaitief voor Roboflow
Wil je geen gebruikmaken van Roboflow, dan zijn er ook andere tools beschikbaar voor het labelen van afbeeldingen, zoals LabelImg, VoTT, en RectLabel. Deze tools zijn meestal gratis en kunnen lokaal op je computer worden geïnstalleerd. Ze bieden vergelijkbare functionaliteiten voor het labelen van afbeeldingen, maar hebben mogelijk een minder uitgebreide set functies in vergelijking met Roboflow.
Een voorbeeld hiervan is [makesense.ai](https://www.makesense.ai/), een gratis online tool voor het labelen van afbeeldingen die eenvoudig te gebruiken is en geen account vereist. Je kunt je afbeeldingen uploaden, labelen en vervolgens de gelabelde dataset downloaden in verschillende formaten, waaronder YoloV8.

:::{note}
De uitleg van makesense.ai is niet opgenomen in deze handleiding, maar je kunt de website bezoeken en de instructies volgen om je afbeeldingen te labelen als je deze tool wilt gebruiken.
:::

## Opdrachten

### Opdracht 1: Aanmelden bij Roboflow
1. Ga naar de [Roboflow-website](https://roboflow.com/) en maak een gratis account aan.
2. Volg de instructies om je account te verifiëren en in te loggen.

### Opdracht 2: Uploaden van Afbeeldingen
1. Maak een nieuw project aan in Roboflow.  
2. Upload de verzamelde afbeeldingen naar je project. Zorg ervoor dat je alle afbeeldingen uploadt die je in de vorige sectie hebt verzameld.

### Opdracht 3: Labelen van Afbeeldingen
1. Gebruik de labeltool van Roboflow om de objecten in je afbeeldingen te labelen. Maak voor elk object een aparte label aan.
2. Zorg ervoor dat je nauwkeurig labelt, aangezien de kwaliteit van de labels direct van invloed is op de prestaties van het getrainde netwerk.

> Let op: Maak alleen rechtlijnige bounding boxes rond de objecten die je wilt herkennen.

### Opdracht 4: Proeftraining
1. Nadat je alle afbeeldingen hebt gelabeld, kun je een proeftraining uitvoeren in Roboflow om te zien hoe goed je labels zijn. Zoek zelf uit hoe je dit doet in Roboflow.
:::{caution}
Helaas kun je maar een beperkt aantal proeftrainingen uitvoeren met een gratis account.
:::

### Opdracht 5: Exporteren van de Dataset
Exporteer de gelabelde dataset in een formaat dat compatibel is met het machine learning framework dat je gaat gebruiken (YoloV8) voor het trainen van je neuraal netwerk. 

Er zijn hiervoor twee opties:
1. Exporteer de dataset direct vanuit Roboflow in het gewenste formaat.
2. Gebruik de Roboflow API om de dataset te downloaden naar je lokale machine.
   - Volg de instructies in Roboflow om de API-sleutel te verkrijgen
    - Gebruik de API-documentatie van Roboflow om de dataset te downloaden met een Python script zoals hieronder weergegeven:
    ```python
    import roboflow

    rf = roboflow.Roboflow(api_key="YOUR_API_KEY")
    project = rf.workspace().project("YOUR_PROJECT_NAME")   
    dataset = project.version(YOUR_VERSION_NUMBER).download("yolov8")
    ```
    