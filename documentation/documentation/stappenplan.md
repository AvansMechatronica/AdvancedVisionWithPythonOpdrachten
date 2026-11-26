# Recap en stappenplan machine vision

Deze pagina hoort bij de presentatie **Recap en stappenplan machine vision**. Elk vision-vraagstuk doorloopt dezelfde vijf stappen: beeld opnemen, voorbewerken, segmenteren, meten en beslissen. Elk werkcollege vulde één of meer van die stappen in.

| Werkcollege | Onderwerp | Wat je ermee kunt | Pipeline-stap |
|---|---|---|---|
| 1 | Python en OpenCV | Beeld inlezen, tonen, schalen, tekenen | Beeld opnemen |
| 2 | Histogram en contrast | Contrast verbeteren, drempelen (Otsu) | Voorbewerken, segmenteren |
| 3 | NumPy en morfologie | ROI, maskers, ruis opruimen in zwart-wit | Voorbewerken, segmenteren |
| 4 | Filters en convolutie | Ruis wegfilteren met blur, Gauss, mediaan | Voorbewerken |
| 5 | Blobs en segmentatie | Objecten vinden, meten, scheiden | Segmenteren, meten, beslissen |
| 6 | Kleurdomeinen | Selecteren op kleur, PNG of JPEG | Voorbewerken, segmenteren |
| 7 | Edge detectie | Randen vinden met Sobel en Canny | Voorbewerken, meten |

## Het stappenplan in zes stappen

1. **Vraag.** Wat is goed, wat is fout? Maak het meetbaar, bijvoorbeeld: oppervlakte kleiner dan 7000 pixels is afkeur.
2. **Beelden.** Verzamel minstens 10 goede en 10 foute voorbeelden, met vast licht, vaste afstand en een achtergrond die contrasteert. Sla op als PNG.
3. **Voorbewerken.** Grijs als alleen helderheid telt, HSV als kleur telt. Filter tegen ruis, snij een ROI uit.
4. **Segmenteren.** Een zwart-witbeeld met wit is object: drempel met Otsu of `inRange` in HSV, daarna opening en closing. Raken objecten elkaar? Watershed.
5. **Meten.** `findContours`, kruimels wegfilteren op oppervlakte, en de maat kiezen die bij je vraag past.
6. **Beslissen.** Kies de grens tussen de goede en foute waarden in, teken goed groen en fout rood en test op álle beelden.

Werkt het niet? Ga een stap terug. Bijna altijd zit de oorzaak eerder in de keten dan je denkt.

## Welke techniek kies je?

| Probleem | Techniek | OpenCV | Werkcollege |
|---|---|---|---|
| Te donker of weinig contrast | Gamma, egalisatie | `cv2.LUT`, `cv2.equalizeHist` | 2 |
| Korrelige ruis | Gauss-filter | `cv2.GaussianBlur` | 4 |
| Losse witte en zwarte stipjes | Mediaanfilter | `cv2.medianBlur` | 4 |
| Object anders van helderheid | Drempelen met Otsu | `cv2.threshold` | 2 |
| Object anders van kleur | HSV en inRange | `cv2.cvtColor`, `cv2.inRange` | 6 |
| Kruimels of gaatjes in zwart-wit | Opening, closing | `cv2.morphologyEx` | 3 |
| Objecten raken elkaar | Watershed | `cv2.distanceTransform`, `cv2.watershed` | 5 |
| Rafelige of gebroken rand | Canny, randen tellen | `cv2.Canny` | 7 |

## Opdrachten

### Opdracht 1: Het uitgewerkte voorbeeld lokaal (20 min)

In de presentatie worden augurken op grootte gesorteerd. Werk dit voorbeeld lokaal uit met `augurken.bmp` (in `images.zip`):

```python
img = cv2.imread("images/augurken.bmp")             # 2 beelden
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)          # 3 voorbewerken
blauw = cv2.inRange(hsv, (95, 60, 40), (135, 255, 255))
zw = cv2.bitwise_not(blauw)                         # 4 segmenteren
k = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (9, 9))
zw = cv2.morphologyEx(zw, cv2.MORPH_OPEN, k)
zw = cv2.morphologyEx(zw, cv2.MORPH_CLOSE, k)
cnts, _ = cv2.findContours(zw, cv2.RETR_EXTERNAL,   # 5 meten
                           cv2.CHAIN_APPROX_SIMPLE)
```

1. Maak het script af: teken elke augurk die te klein is rood en de rest groen (stap 6). In de presentatie ligt de grens op 7000 pixels. Print eerst de oppervlaktes: past die grens ook bij jouw beeld, of moet je hem aanpassen?
2. Toon na elke stap het tussenbeeld. Bij welke stap zie je het meeste verschil?
3. Verander de grens en de kleurgrenzen. Hoe gevoelig is het resultaat?

### Opdracht 2: Het stappenplan op je testbeeld (30 min)

Pas de zes stappen toe op het testbeeld dat je sinds werkcollege 1 gebruikt.

1. Schrijf eerst stap 1 op: wat is goed en fout, uitgedrukt in een getal?
2. Maak één script waarin elke regel bij een stap van het plan hoort, net als in het voorbeeld.
3. Print de meetwaarden van je goede en foute voorbeelden naast elkaar en kies de grens.

## Checklist

1. Wat is goed en fout, uitgedrukt in een getal?
2. Genoeg testbeelden, met vast licht?
3. Klopt het zwart-witbeeld voordat ik meet?
4. Welke maat en grens scheiden goed en fout?
5. Hoeveel fouten op de hele testset?
