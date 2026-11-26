# Werkcollege 2: Histogram en contrast

Deze opdrachten horen bij **werkcollege 2 - Histogram en contrast**. In het werkcollege maak je opdracht 1 (gamma met een schuifregelaar) en opdracht 2 (munten drempelen) in het Colab-notebook *Werkcollege 2 - Histogram en contrast*. Op deze pagina doe je hetzelfde lokaal, met schuifregelaars in een OpenCV-venster.

In de vision-pipeline zit je bij **voorbewerken** (contrast verbeteren zodat details zichtbaar worden) en **segmenteren** (met een drempel scheid je voorwerp en achtergrond).

## Leerdoelen

Na deze opdrachten kun je:

- een histogram lezen en zien of een beeld te donker, te licht of te vlak is;
- contrast verbeteren met gamma-correctie en histogram-egalisatie;
- een drempelwaarde kiezen uit het histogram en zo een binair beeld maken;
- Otsu automatisch een drempel laten kiezen.

## Schuifregelaars lokaal: trackbars

In Colab gebruik je `interact`. Lokaal maak je een schuifregelaar met `cv2.createTrackbar`. Dit patroon gebruik je in alle volgende werkcolleges:

```python
import cv2

grijs = cv2.imread("images/pennies.jpg", cv2.IMREAD_GRAYSCALE)

cv2.namedWindow("drempel")
cv2.createTrackbar("t", "drempel", 128, 255, lambda x: None)

while True:
    t = cv2.getTrackbarPos("t", "drempel")
    _, zw = cv2.threshold(grijs, t, 255, cv2.THRESH_BINARY_INV)
    cv2.imshow("drempel", zw)
    if cv2.waitKey(30) & 0xFF == 27:   # Esc om te stoppen
        break
cv2.destroyAllWindows()
```

> Een trackbar kent alleen gehele getallen. Wil je gamma van 0,2 tot 3,0 instellen? Laat de trackbar lopen van 2 tot 30 en deel door 10.

## Opdrachten

### Opdracht 1: Histogram lezen (10 min)

1. Lees `weinig contrast.jpg` en `veel contrast.jpg` in als grijsbeeld.
2. Bereken van beide het histogram met `cv2.calcHist([grijs], [0], None, [256], [0, 256])` en teken het met `matplotlib`.
3. Waar ligt de berg? Hoe breed is hij? Hoe zie je aan het histogram dat een beeld weinig contrast heeft?

### Opdracht 2: Gamma met een trackbar (15 min)

1. Lees `horse.jpg` in als grijsbeeld.
2. Maak een gamma-tabel (LUT) en pas die toe met `cv2.LUT`:
   ```python
   tabel = np.array([(i / 255) ** g * 255 for i in range(256)]).astype("uint8")
   uit = cv2.LUT(grijs, tabel)
   ```
3. Maak een trackbar voor gamma van 0,2 tot 3,0. Zoek de gamma waarbij je het hoofdstel van het paard het best ziet.
4. Toon voor en na het histogram. Wat is er veranderd? Blijven zwart (0) en wit (255) gelijk?

> Vuistregel: donkere details zichtbaar maken: gamma onder 1. Overbelicht beeld: gamma boven 1. Begin rond 0,5 of 1,5.

### Opdracht 3: Egalisatie (10 min)

1. Pas `cv2.equalizeHist` toe op `weinig contrast.jpg`.
2. Vergelijk het histogram voor en na. Wordt nu het hele bereik van 0 tot 255 gebruikt?
3. Pas egalisatie ook toe op `horse.jpg`. Werkt gamma of egalisatie hier beter?

### Opdracht 4: Munten drempelen (15 min)

1. Lees `pennies.jpg` in als grijsbeeld en teken het histogram.
2. Kies zelf een drempel met een trackbar (zie het voorbeeld hierboven). Leg de drempel in het dal tussen de twee bergen.
3. Laat Otsu een drempel kiezen:
   ```python
   t, zw = cv2.threshold(grijs, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
   print("Otsu kiest", t)
   ```
   Hoeveel scheelt het met jouw keuze?

> Vuistregel: leg de drempel in het dal van het histogram. Twijfel? Gebruik Otsu en print welke waarde hij kiest.

### Opdracht 5: Als Otsu niet werkt (10 min)

1. Probeer Otsu op `weinig contrast.jpg`. Wat gaat er mis?
2. Los het op met egalisatie vóór het drempelen, of met `cv2.adaptiveThreshold`.
3. Maak trackbars voor `blockSize` en `C` van de adaptieve drempel en zoek een goede instelling.

> Vuistregel: `blockSize` groter dan het object (maar niet het halve beeld), en altijd oneven: 11, 31, 51. Veel spikkels in egale vlakken? Verhoog `C` met stappen van 2 tot 5.

### In de praktijk: voorwerp los van de achtergrond

1. Teken het histogram van je testbeeld uit werkcollege 1.
2. Zie je twee bergen? Zo niet: kies een achtergrond met meer contrast. Een donker voorwerp op wit papier geeft de beste scheiding.
3. Maak een binair beeld en bewaar het als PNG: dat is de basis voor volgende week.

## Kennisvragen

1. Hoe zie je aan een histogram dat een beeld weinig contrast heeft?
2. Wat doet een gamma kleiner dan 1?
3. Wanneer werkt Otsu goed en wanneer niet?
