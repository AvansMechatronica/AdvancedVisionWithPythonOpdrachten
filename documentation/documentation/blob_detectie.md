# Werkcollege 5: Blobs en segmentatie

Deze opdrachten horen bij **werkcollege 5 - Blobs en segmentatie**. In het werkcollege maak je opdracht 1 (euromunten sorteren) en opdracht 2 (aanliggende munten scheiden) in het Colab-notebook *Werkcollege 5 - Blobs en segmentatie*. Op deze pagina oefen je hetzelfde lokaal.

In de vision-pipeline zit je bij **segmenteren**, **meten** en **beslissen**: voorwerpen vinden, meten en goed groen en fout rood tekenen.

## Leerdoelen

Na deze opdrachten kun je:

- contouren vinden en tekenen;
- oppervlakte, omtrek, zwaartepunt en omhullende rechthoek meten;
- aanliggende objecten scheiden met watershed;
- segmenteren op kleur met K-means;
- een voorbeeld terugzoeken met template matching.

## Opdrachten

### Opdracht 1: Contouren vinden en tellen (15 min)

1. Lees `euromunten.jpg` in en maak een schoon zwart-witbeeld (grijs, filter, Otsu, opening of closing).
2. Zoek de contouren:
   ```python
   cnts, _ = cv2.findContours(zw, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
   ```
3. Filter kruimels weg op oppervlakte (`cv2.contourArea(c) < 2000`) en tel de munten.
4. Teken alle contouren met `cv2.drawContours` op een kopie van het origineel en nummer elke munt.

> Vuistregel: objecten tellen met `RETR_EXTERNAL`. Gaten in objecten ook nodig: `RETR_TREE`. Methode: `CHAIN_APPROX_SIMPLE`.

### Opdracht 2: Meten (15 min)

1. Print van elke munt de oppervlakte (`cv2.contourArea`) en de omtrek (`cv2.arcLength(c, True)`).
2. Bereken het zwaartepunt met moments:
   ```python
   M = cv2.moments(c)
   cx = int(M["m10"] / M["m00"])
   cy = int(M["m01"] / M["m00"])
   ```
3. Teken het zwaartepunt en de omhullende rechthoek (`cv2.boundingRect`) in het beeld.

### Opdracht 3: Goed of fout: euro's en centen (15 min)

1. Kies een grens op oppervlakte: euro's groen omlijnen, centen rood.
2. Maak een trackbar voor de grens, zodat je ziet waar de indeling omslaat.
3. Waarom wordt de zilveren rand van de 2 euro slecht gevonden? Wat zou je aan het licht of de drempel kunnen veranderen?

### Opdracht 4: Aanliggende munten scheiden met watershed (20 min)

1. Lees `overlap_coins.jpg` in en maak een zwart-witbeeld. Hoeveel contouren vind je? Klopt dat met het aantal munten?
2. Volg de stappen van het notebook:
   ```python
   dist = cv2.distanceTransform(zw, cv2.DIST_L2, 5)
   _, zeker = cv2.threshold(dist, 0.6 * dist.max(), 255, 0)
   n, labels = cv2.connectedComponents(zeker.astype("uint8"))
   ```
   Maak daarna het onbekende gebied en de markers, en roep `cv2.watershed` aan.
3. Maak een trackbar voor de factor op de afstandskaart (0,4 tot 0,8). Bij welke factor vind je precies het juiste aantal munten?

> Vuistregel: tel eerst zelf hoeveel objecten er zijn en kies de factor die precies dat aantal kernen geeft. Meestal 0,5 tot 0,7.

### Opdracht 5: K-means op kleur (10 min)

1. Pas K-means toe op `kerstballen.bmp` met `cv2.kmeans`, met K = 2, 4 en 8.
2. Maak per groep een masker. Welke K scheidt de rode ballen het best van de rest?

### Opdracht 6: Template matching (10 min)

1. Snij uit `euromunten.jpg` één munt uit als template.
2. Zoek die terug met `cv2.matchTemplate(img, template, cv2.TM_CCOEFF_NORMED)` en teken een rechthoek bij elke plek met een score boven een minimale score.
3. Maak een trackbar voor de minimale score. Wat gebeurt er met vals alarm en gemiste munten?
4. Draai het template 45 graden. Werkt het nog?

> Vuistregel: begin bij een score van 0,8 en kijk naar vals alarm en gemiste objecten. Template matching werkt alleen als grootte en draaiing gelijk blijven.

### In de praktijk: goed of fout, groen of rood

1. Zoek de contouren van de voorwerpen in je testbeeld.
2. Meet oppervlakte, omtrek en de verhouding van de omhullende rechthoek.
3. Kies grenzen met een paar goede voorbeelden: wat is goed?
4. Teken goed groen en fout rood over het origineel. Liggen voorwerpen tegen elkaar? Gebruik watershed.

## Kennisvragen

1. Wat is het verschil tussen `cnts` en `c`?
2. Hoe bereken je met OpenCV het zwaartepunt van een contour?
3. Wanneer heb je watershed nodig?
4. Waarom werkt template matching slecht als voorwerpen gedraaid liggen?
