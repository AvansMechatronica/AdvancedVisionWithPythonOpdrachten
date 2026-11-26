# Werkcollege 4: Filters en convolutie

Deze opdrachten horen bij **werkcollege 4 - Filters en convolutie**. In het werkcollege maak je opdracht 1 (vervagen in drie groottes) en opdracht 2 (ruis toevoegen en wegfilteren) in het Colab-notebook *Werkcollege 4 - Filters en convolutie*. Op deze pagina oefen je hetzelfde lokaal.

In de vision-pipeline zit je bij **voorbewerken**: ruis weghalen vóórdat je gaat drempelen.

## Leerdoelen

Na deze opdrachten kun je:

- uitleggen hoe een filter elke pixel opnieuw berekent uit zijn buren;
- een gemiddelde-, Gauss- en mediaanfilter toepassen;
- het juiste filter kiezen voor het soort ruis;
- het effect van de filtergrootte voorspellen.

## Opdrachten

### Opdracht 1: Drie filters naast elkaar (15 min)

1. Lees `sammy_noise.jpg` in.
2. Pas toe en toon naast elkaar:
   - gemiddelde: `cv2.blur(img, (5, 5))`
   - Gauss: `cv2.GaussianBlur(img, (5, 5), 0)`
   - mediaan: `cv2.medianBlur(img, 5)`
3. Zoom in op de ogen. Welk filter haalt de ruis weg en houdt de ogen het scherpst?

### Opdracht 2: Filtergrootte met een trackbar (15 min)

1. Maak een trackbar voor de kernelgrootte (alleen oneven: 3, 5, 7, ..., 15) en een trackbar om te kiezen tussen blur, Gauss en mediaan.
2. Wat gebeurt er met de ruis, en wat met de randen, als je het venster groter maakt?
3. Zet bij `GaussianBlur` sigma eens op een vaste waarde in plaats van 0. Wat verandert er?

> Vuistregel: begin met 5 x 5. Alleen groter maken als de ruis nog zichtbaar is. Altijd oneven. Geef bij Gauss sigma 0 op: dan rekent OpenCV hem zelf uit.

### Opdracht 3: Verscherpen met een eigen kernel (10 min)

1. Maak een verscherpingsfilter en pas het toe met `cv2.filter2D`:
   ```python
   scherp = np.array([[0, -1, 0],
                      [-1, 5, -1],
                      [0, -1, 0]])
   uit = cv2.filter2D(img, -1, scherp)
   ```
2. Pas het toe op `sammy.jpg` en op `sammy_noise.jpg`. Wat gebeurt er met de ruis?

### Opdracht 4: Zout-en-peperruis en de mediaan (15 min)

1. Lees `sudoku.jpg` in als grijsbeeld en voeg zelf zout-en-peperruis toe:
   ```python
   r = np.random.rand(*img.shape)
   ruis = img.copy()
   ruis[r < 0.04] = 0      # peper
   ruis[r > 0.96] = 255    # zout
   ```
2. Filter met gemiddelde en mediaan van dezelfde grootte. Welk filter laat de cijfers het best leesbaar?
3. Waarom werkt de mediaan beter tegen losse witte en zwarte pixels?

> Vuistregel: mediaan 3 of 5 is meestal genoeg. Verdwijnen er details? Ga terug naar een kleiner venster.

### Opdracht 5: Filteren vóór het drempelen (10 min)

1. Drempel het ruizige sudokubeeld met Otsu: zonder filter, na `blur` en na `medianBlur`.
2. Tel de losse vlekjes in elk zwart-witbeeld met `n, labels = cv2.connectedComponents(zw)`.
3. Met welk filter krijg je de minste kruimels?

### In de praktijk: ruis weg vóór het drempelen

1. Zet een filter vóór het drempelen in de pipeline van je testbeeld.
2. Stof of glimlicht: probeer `medianBlur` 5. Korrelig camerabeeld: probeer `GaussianBlur` 5.
3. Vergelijk het aantal kruimels met en zonder filter.

## Kennisvragen

1. Wat gebeurt er als je het filtervenster groter maakt?
2. Waarom werkt de mediaan beter tegen losse witte en zwarte pixels?
3. Waarom zet je een filter vóór het drempelen en niet erna?
