# Werkcollege 1: Python en OpenCV

Deze opdrachten horen bij **werkcollege 1 - Python en OpenCV**. In het werkcollege maak je opdracht 1 (kerstballen) en opdracht 2 (Sammy schalen en labelen) in het Colab-notebook *Werkcollege 1 - Python en OpenCV*. Met de opdrachten op deze pagina oefen je dezelfde stof lokaal op je eigen computer, in Visual Studio Code.

In de vision-pipeline (beeld opnemen, voorbewerken, segmenteren, meten, beslissen) zit je nu bij de eerste stap: **een beeld in Python krijgen** en begrijpen wat er in het geheugen staat.

## Leerdoelen

Na deze opdrachten kun je:

- een afbeelding inlezen, tonen en opslaan met OpenCV;
- uitleggen dat een afbeelding een tabel met getallen van 0 tot 255 is;
- de grootte opvragen, het beeld schalen en omzetten naar grijs;
- vormen en tekst in een beeld tekenen en het resultaat opslaan.

## Voorbereiding: van Colab naar lokaal

1. Zorg dat Python en Visual Studio Code klaarstaan, zie [Voorbereidingen](voorbereidingen.md).
2. Installeer in je virtuele omgeving de bibliotheken:
   ```bash
   pip install opencv-python numpy matplotlib
   ```
3. Maak in je projectmap een map `images`. Download [images.zip](https://raw.githubusercontent.com/AvansMechatronica/CursusSupport/main/images/images.zip) en pak het uit in die map. Dit zijn dezelfde testbeelden als in de werkcolleges.

De code uit de notebooks werkt lokaal bijna één op één. Er zijn drie verschillen:

| In Colab | Lokaal |
|---|---|
| `cv2_imshow(img)` | `cv2.imshow("naam", img)` gevolgd door `cv2.waitKey(0)` |
| `interact(...)` met een schuifregelaar | `cv2.createTrackbar(...)` in een OpenCV-venster, zie werkcollege 2 |
| `/content/sammy.jpg` | `images/sammy.jpg` (pad vanaf je projectmap) |

Een minimaal lokaal script ziet er zo uit:

```python
import cv2

img = cv2.imread("images/kerstballen.bmp")
if img is None:
    print("Bestand niet gevonden: controleer het pad")
    exit()

cv2.imshow("kerstballen", img)
cv2.waitKey(0)            # wacht op een toets
cv2.destroyAllWindows()
```

> Klopt het pad niet, dan geeft `cv2.imread` `None` terug en **geen** foutmelding. Controleer daarom altijd of `img is None`.

## Opdrachten

### Opdracht 1: Een beeld is een tabel met getallen (10 min)

Maak een script `wc1_beeld.py`.

1. Lees `kerstballen.bmp` in en toon het in een venster.
2. Print `img.shape` en `img.dtype`. Hoeveel pixels heeft het beeld, en hoeveel getallen staan er in het geheugen?
3. Lees de pixel op rij 50, kolom 100 uit met `b, g, r = img[50, 100]`. Let op: eerst de rij (y), dan de kolom (x).
4. Kies zelf een pixel midden op een rode bal. Is de rode waarde hoog en zijn blauw en groen laag?

> OpenCV gebruikt de volgorde **BGR**, niet RGB.

### Opdracht 2: De vlag van imread (10 min)

1. Lees `sammy.jpg` twee keer in: met `cv2.IMREAD_COLOR` en met `cv2.IMREAD_GRAYSCALE`.
2. Vergelijk de `shape` van beide. Hoeveel lagen heeft elk beeld?
3. Maak ook een grijze versie met `cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)`. Is het resultaat gelijk aan direct grijs inlezen?

> Vuistregel: ga je alleen helderheid meten of drempelen? Lees dan meteen in als grijs: drie keer minder data.

### Opdracht 3: Schalen en interpolatie (15 min)

1. Verklein `sammy.jpg` naar 25% met `cv2.resize(img, None, fx=0.25, fy=0.25, interpolation=...)`. Doe dit met `cv2.INTER_NEAREST` en met `cv2.INTER_AREA` en toon beide naast elkaar.
2. Snij een uitsnede van het oog uit (bijvoorbeeld `img[y1:y2, x1:x2]`) en vergroot die 8 keer met `INTER_NEAREST`, `INTER_LINEAR` en `INTER_CUBIC`.
3. Beschrijf in een paar zinnen wat je ziet. Welke interpolatie kies je bij verkleinen en welke bij vergroten?

> Vuistregel: verkleinen met `INTER_AREA`. Vergroten met `INTER_LINEAR` of `INTER_CUBIC`. `INTER_NEAREST` alleen voor maskers en labels.

### Opdracht 4: Overlays tekenen (15 min)

1. Maak een kopie: `uit = img.copy()`.
2. Teken op `kerstballen.bmp` een rechthoek (`cv2.rectangle`) om een kerstbal, een cirkel (`cv2.circle`) om een andere bal en een lijn (`cv2.line`).
3. Zet bij elke vorm een label met `cv2.putText`. Speel met `fontScale` en de dikte.
4. Punten zijn `(x, y)` vanaf linksboven, kleuren zijn `(B, G, R)`. Teken één vorm in rood, één in groen en één in wit.

> Vuistregel: teken altijd op `uit = img.copy()`. Anders meet je straks je eigen kaders en tekst mee.

### Opdracht 5: Opslaan als PNG en JPG (10 min)

1. Sla je beeld met overlays op als `kerstballen_label.png` en als `kerstballen_label.jpg` met `cv2.imwrite`.
2. Vergelijk de bestandsgrootte met `os.path.getsize`. Welk bestand is kleiner, en waarom?
3. Maak van opdracht 1 een functie `print_image_info(img)` die je in de volgende werkcolleges hergebruikt.

### In de praktijk: je eerste testbeeld

Kies uit de testbeelden een beeld met losse voorwerpen op een effen ondergrond, zoals `euromunten.jpg` of `TestShapes.jpg`.

1. Lees het in, bekijk de `shape` en sla een grijze versie op als PNG.
2. Noteer wat je wilt vinden: hoeveel voorwerpen, welke kleur, welke vorm.

Dit beeld gebruik je de komende werkcolleges als testbeeld.

## Kennisvragen

1. Waarom heeft een kleurenbeeld drie getallen per pixel, en in welke volgorde staan ze in OpenCV?
2. Wat betekent `img.shape = (480, 640, 3)`?
3. Welke interpolatie kies je bij verkleinen, en waarom?
