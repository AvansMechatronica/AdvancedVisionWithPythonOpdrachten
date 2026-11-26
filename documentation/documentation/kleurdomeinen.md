# Werkcollege 6: Kleurdomeinen

Deze opdrachten horen bij **werkcollege 6 - Kleurdomeinen**. In het werkcollege maak je opdracht 1 (stippen zoeken op kleur) en opdracht 2 (compressie meten) in het Colab-notebook *Werkcollege 6 - Kleurdomeinen*. Op deze pagina oefen je hetzelfde lokaal.

In de vision-pipeline zit je bij **voorbewerken** en **segmenteren**: als de kleur het verschil maakt, segmenteer je in HSV in plaats van op helderheid.

## Leerdoelen

Na deze opdrachten kun je:

- uitleggen hoe een camera kleur meet met R, G en B;
- het verschil tussen RGB en HSV benoemen;
- een kleur selecteren met `inRange` in HSV, ook rood;
- uitleggen waarom je in machine vision PNG gebruikt en geen JPEG.

## Opdrachten

### Opdracht 1: Kanalen splitsen (10 min)

1. Lees `kerstballen.bmp` in en splits het in drie kanalen met `b, g, r = cv2.split(img)`. Toon ze als drie grijsbeelden.
2. Zet het beeld om naar HSV met `cv2.cvtColor(img, cv2.COLOR_BGR2HSV)` en splits ook dat in H, S en V.
3. In welk kanaal zie je de rode ballen het duidelijkst?

> In OpenCV loopt H van 0 tot 179 (de halve kleurencirkel van 0 tot 360 graden). S (hoe fel) en V (hoe licht) lopen van 0 tot 255.

### Opdracht 2: Stippen zoeken op kleur (20 min)

1. Lees `damien_hirst_dot.jpg` in en zet het om naar HSV.
2. Maak trackbars voor de ondergrens en bovengrens van H en voor de ondergrens van S:
   ```python
   masker = cv2.inRange(hsv, (h1, s1, 40), (h2, 255, 255))
   ```
3. Zoek alle blauwe stippen. Tel ze met contouren (zie werkcollege 5). Hoeveel zijn het?

> Vuistregel: meet de H van je object op een paar pixels en neem ongeveer 5 tot 10 aan beide kanten. Begin met S vanaf 80 tot 100.

### Opdracht 3: Robuust bij ander licht (10 min)

1. Maak het beeld donkerder, bijvoorbeeld met `cv2.convertScaleAbs(img, alpha=0.5, beta=0)`.
2. Werkt je HSV-selectie nog? Maak dezelfde selectie in BGR met `cv2.inRange(img, ...)` en vergelijk.
3. Welk kanaal verandert het meest als het licht minder wordt?

### Opdracht 4: Rood: de kleur aan twee kanten (10 min)

1. Selecteer de rode stippen. Rood zit aan beide kanten van H: rond 0 en rond 179.
2. Maak twee maskers en combineer ze met `cv2.bitwise_or`.
3. Alternatief: draai H een halve slag (`(h + 90) % 180`), zodat rood in het midden komt te liggen.

### Opdracht 5: Compressie meten (15 min)

1. Sla een testbeeld op als PNG en als JPEG met kwaliteit 90, 50 en 10:
   ```python
   cv2.imwrite("test.jpg", img, [cv2.IMWRITE_JPEG_QUALITY, 10])
   ```
2. Vergelijk de bestandsgroottes.
3. Lees de JPEG's weer in en bereken het verschil met het origineel met `cv2.absdiff`. Tel hoeveel pixels meer dan 10 grijswaarden zijn veranderd.
4. Doe je kleurselectie op de JPEG van kwaliteit 10. Wat gaat er mis?

> Vuistregel: beelden om te meten sla je op als PNG (zonder verlies). JPEG alleen voor opslag of overzicht, met kwaliteit 90 of hoger.

### In de praktijk: sorteren op kleur

1. Zoek één kleur in je testbeeld met HSV.
2. Bepaal de H-, S- en V-grenzen met een paar goede voorbeelden.
3. Combineer kleur met de vormmetingen van werkcollege 5.
4. Sla al je testbeelden op als PNG.

## Kennisvragen

1. Wat betekenen H, S en V?
2. Waarom is HSV robuuster dan RGB bij wisselend licht?
3. Waarom sla je beelden voor machine vision op als PNG?
