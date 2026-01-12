# Rekentool optica

In deze opdrachten ga je een Python-script schrijven dat verschillende optica-gerelateerde berekeningen uitvoert. De tool zal vanuit een gegeven vraagstuk de benodigde waarden vragen en de resultaten berekenen en weergeven.

De opdracht is geleidend opgesteld, maar leidt uiteindelijk tot 1 gehele rekentool voor optica. Je kunt de opdracht zowel als console-applicatie als met een grafische gebruikersinterface (GUI) uitvoeren, de keuze is aan jouzelf.

Er wordt verwacht dat je de volgende Python concepten gebruikt:
- Functies
- Invoervalidatie
- Lussen
- Lijsten
- Dictionaries

Tijdens de uitvoering van de opdrachten dien je zelf onderzoek te doen naar (veelgebruikte) camera's en lenzen, zodat je hiervanuit de juiste waarden kunt gebruiken in je rekentool.

## Opdracht 1: Berekening van de sensorresolutie
Maak een Python-script dat de gebruiker vraagt het field of view in verticale en horizontale richting (in mm). Maak ook een invoer voor het kleinste detail in verticale en horizontale richting dat nog net te onderscheiden is (in mm). Bereken hieruit de pixels per mm in zowel verticale als horizontale richting.

## Opdracht 2: Selectie van een sensor
Maak een lijst van dictionary's van verschillende camera's met hun resoluties (in pixels) en afmetingen (in mm). Laat je Python-script een voorstel doen voor een geschikte sensor op basis van de berekende pixels per mm uit opdracht 1. Houd bij de keuze van je sensor rekening met de vervorming aan de randen van de afbeelding. 

## Opdracht 2a: Efficientie van de sensor
Breid je script uit zodat het ook de efficiëntie van de sensor berekent. De efficiëntie wordt gedefinieerd als het percentage van de sensoroppervlakte dat daadwerkelijk wordt gebruikt voor beeldvorming (in tegenstelling tot randen en andere niet-beeldvormende delen).

## Opdracht 3: Berekeningsmethode kiezen
Bereid je programma voor om een keuze te maken voor 2 doorberekeningspaden:
* Berekening op basis van gekozen lens
* Berekening op basis van vastgestelde voorwerpsafstand

## Opdracht 4: Berekening op basis van gekozen lens
Maak een functie die de brandpuntsafstand van de lens vraagt(zie hieronder) en vandaaruit de voorwerpsafstand en beeldafstand berekent. Maak voor de lenzen een dictionary met verschillende brandpuntsafstanden en hun eigenschappen (zoals maximale diafragma opening). Om de berekening mogelijk te maken dien je de dictionary van de camera's aan te passen zodat ook de brandpuntsafstand van de lens tot de sensor wordt opgeslagen.

## Opdracht 5: Berekening op basis van vastgestelde voorwerpsafstand
Maak een functie die de voorwerpsafstand vraagt en op basis daarvan de benodigde brandpuntsafstand van de lens berekent. Gebruik hiervoor de lens eigenschappen uit de dictionary van opdracht 4.

## Opdracht 6: Presentatie van resultaten
Zorg ervoor dat je script de resultaten van de berekeningen op een duidelijke en overzichtelijke manier presenteert aan de gebruiker. Dit kan zowel in de console als in een grafische gebruikersinterface (GUI) zijn, afhankelijk van je voorkeur.

## Opdracht 7(uitdaging): Resultaten in dictionary opslaan
Sla de resultaten van elke berekening op in een dictionary met duidelijke sleutels, zodat ze later gemakkelijk kunnen worden opgehaald en weergegeven.

## Opdracht 8(extra uitdaging): Resultaten opslaan in JSON-bestand
JSON (JavaScript Object Notation) is een veelgebruikt formaat voor het opslaan en uitwisselen van gegevens. Het is eenvoudig leesbaar voor zowel mensen als machines en wordt vaak gebruikt in webapplicaties. Ga zelfstandig op onderzoek hoe je in Python met de `json`-module gegevens kunt opslaan in een JSON-bestand.

Breid je script uit zodat het de resultaten van de berekeningen opslaat in een JSON-bestand. Dit maakt het mogelijk om de resultaten later te bekijken of te delen met anderen.
