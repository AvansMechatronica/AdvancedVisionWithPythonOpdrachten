# Werkcollege 3: NumPy en morfologie

Deze opdrachten horen bij **werkcollege 3 - NumPy en morfologie**. In het werkcollege maak je opdracht 1 (pallet meten met NumPy) en opdracht 2 (ruis opruimen) in het Colab-notebook *Werkcollege 3 - NumPy en morfologie*. Op deze pagina oefen je hetzelfde lokaal.

In de vision-pipeline zit je bij **voorbewerken** (een uitsnede nemen, rekenen met maskers) en **segmenteren** (het zwart-witbeeld opruimen, zodat elke BLOB één voorwerp is).

## Leerdoelen

Na deze opdrachten kun je:

- een uitsnede (ROI) uit een beeld nemen met NumPy;
- met een masker pixels tellen en een percentage berekenen;
- erosie, dilatatie, opening en closing toepassen en uitleggen waarvoor;
- de juiste kernelvorm en -grootte kiezen.

## Opdrachten

### Opdracht 1: Een uitsnede nemen (ROI) (10 min)

1. Lees `pallet.bmp` in als grijsbeeld en print `shape` en `dtype`.
2. Snij een uitsnede uit met `roi = img[y1:y2, x1:x2]`. Let op: eerst de rijen (y), dan de kolommen (x).
3. Teken de ROI als rechthoek in een kopie van het originele beeld, zodat je ziet welk deel je hebt gekozen.

### Opdracht 2: Meten met een masker (15 min)

1. Maak een masker van de lichte planken: `masker = roi > 150`.
2. Bereken het percentage hout:
   ```python
   pct = 100 * np.count_nonzero(masker) / roi.size
   print(f"{pct:.1f} % hout")
   ```
3. Doe dit voor de linker- en de rechterhelft van de pallet. Welke kant heeft meer hout?
4. Bereken met `img[masker].mean()` de gemiddelde helderheid van alleen het hout.

### Opdracht 3: Rekenen met uint8 (5 min)

1. Tel 100 op bij het beeld met `img + 100` en met `cv2.add(img, 100)`.
2. Toon beide. Wat is het verschil? Waarom is `250 + 10` gelijk aan `4` bij een `uint8`-beeld?

### Opdracht 4: Erosie en dilatatie (10 min)

1. Lees `stars_1.png` in als grijsbeeld en maak er een zwart-witbeeld van met Otsu (zie werkcollege 2).
2. Maak een kernel met `cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))`.
3. Pas `cv2.erode` en `cv2.dilate` toe. Wat gebeurt er met de punten van de sterren?

### Opdracht 5: Ruis opruimen met een trackbar (20 min)

1. Voeg zelf witte en zwarte ruis toe aan het zwart-witbeeld:
   ```python
   r = np.random.rand(*zw.shape)
   ruis = zw.copy()
   ruis[r < 0.02] = 0      # zwarte gaatjes
   ruis[r > 0.98] = 255    # witte kruimels
   ```
2. Maak een trackbar voor de kernelgrootte (alleen oneven waarden: 3, 5, 7, 9, ...) en een trackbar voor de bewerking: opening of closing (`cv2.morphologyEx` met `cv2.MORPH_OPEN` of `cv2.MORPH_CLOSE`).
3. Welke kernel haalt alle kruimels weg zonder de vormen te beschadigen? Vul daarna de gaatjes met closing.
4. Vergelijk de kernelvormen `MORPH_RECT`, `MORPH_ELLIPSE` en `MORPH_CROSS`. Welke houdt de punten van de sterren het best heel?

> Vuistregel: kies de kernel groter dan de ruis en duidelijk kleiner dan het kleinste object dat je wilt houden. Liever één keer een passende kernel dan veel iteraties.

### Opdracht 6: De rand van een object (10 min)

1. Bepaal de rand van elke ster: het zwart-witbeeld min het geërodeerde beeld.
2. Teken de rand in kleur over het originele beeld.

### In de praktijk: een schoon zwart-witbeeld

1. Neem het zwart-witbeeld van je testbeeld van vorige week.
2. Gebruik opening tegen kruimels en stof, en closing tegen gaatjes door glimlicht op het voorwerp.
3. Kies de kleinste kern die het werk doet en sla het resultaat op als PNG.

## Kennisvragen

1. Wat geeft `img[100:200, 50:150]` terug?
2. Waarom is `250 + 10` gelijk aan `4` bij een `uint8`-beeld?
3. Wat betekent BLOB, en waarom wil je dat elke BLOB één voorwerp is?
4. Wanneer gebruik je opening en wanneer closing?
5. Welke kernelvorm kies je voor ronde objecten, en welke voor horizontale lijnen?
