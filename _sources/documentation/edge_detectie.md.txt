# Werkcollege 7: Edge detectie

Deze opdrachten horen bij **werkcollege 7 - Edge detectie**. In het werkcollege maak je opdracht 1 (Sobel in x en y) en opdracht 2 (Canny instellen) in het Colab-notebook *Werkcollege 7 - Edge detectie*. Op deze pagina oefen je hetzelfde lokaal.

Met randen vind je beschadigde producten: een rafelige of gebroken rand. Daarmee is je pipeline compleet: opnemen, filteren, segmenteren, meten, beslissen.

## Leerdoelen

Na deze opdrachten kun je:

- uitleggen wat een rand is: een plek waar de helderheid snel verandert;
- randen vinden met Sobel en die vergelijken met Prewitt en Roberts;
- de stappen van Canny benoemen en de twee drempels instellen;
- uitleggen waarom je eerst vervaagt.

De afbeeldingen `dop_goed.jpg` en `dop_fout.jpg` zitten niet in `images.zip`. Download ze apart: [dop_goed.jpg](https://raw.githubusercontent.com/AvansMechatronica/CursusSupport/main/images/dop_goed.jpg) en [dop_fout.jpg](https://raw.githubusercontent.com/AvansMechatronica/CursusSupport/main/images/dop_fout.jpg).

## Opdrachten

### Opdracht 1: Sobel in x en y (15 min)

1. Lees `sudoku.jpg` in als grijsbeeld.
2. Bereken Sobel in x en in y en toon ze naast elkaar:
   ```python
   gx = cv2.Sobel(grijs, cv2.CV_64F, 1, 0)
   gy = cv2.Sobel(grijs, cv2.CV_64F, 0, 1)
   rand = cv2.magnitude(gx, gy)
   cv2.imshow("rand", cv2.convertScaleAbs(rand))
   ```
3. Welke lijnen van de sudoku zie je in het x-beeld, en welke in het y-beeld?

> Vuistregel: standaard `ksize` 3. Ruizig beeld: 5. Groter dan 7 is zelden nodig.

### Opdracht 2: Eerst vervagen (10 min)

1. Herhaal opdracht 1 na `GaussianBlur` met 3, 7 en 11. Gebruik een trackbar voor de kernelgrootte.
2. Wat verandert er aan de randen en aan de ruis?
3. Vergelijk met `cv2.Laplacian`. Welke is gevoeliger voor ruis?

### Opdracht 3: Prewitt en Roberts (10 min, extra)

1. Maak een Prewitt-kernel en een Roberts-kernel en pas ze toe met `cv2.filter2D`.
2. Vergelijk het resultaat met Sobel. Welke geeft de schoonste randen?

> Vuistregel: gebruik Sobel: die zit in OpenCV en dempt ruis het best. Roberts alleen bij schone beelden met heel fijne randen.

### Opdracht 4: Canny instellen (15 min)

1. Lees `pallet.bmp` in als grijsbeeld en vervaag het met `cv2.GaussianBlur(grijs, (5, 5), 0)`.
2. Maak trackbars voor de lage en de hoge drempel van `cv2.Canny(vaag, laag, hoog)`.
3. Zoek de instelling waarbij alle planken zichtbaar zijn en de vloer niet.
4. Wat gebeurt er als je de lage drempel te laag kiest? En als je het vervagen weglaat?

> Vuistregel: begin met `GaussianBlur` 5 x 5. Zie je nog randjes in egale vlakken? Vergroot de kernel.

### Opdracht 5: Goed of fout: randen tellen (15 min)

1. Pas dezelfde Canny-instelling toe op `dop_goed.jpg` en `dop_fout.jpg`.
2. Tel de randpixels met `np.count_nonzero`. Waar zie je het verschil?
3. Kies een grens en zet "goed" in groen of "fout" in rood in het beeld.

### In de praktijk: beschadigde producten vinden

1. Een beschadigd product heeft een rafelige of gebroken rand.
2. Tel de randpixels binnen elke contour van je testbeeld, of vergelijk omtrek en oppervlakte.
3. Meer randen dan bij een goed exemplaar? Teken een rode contour.

## Kennisvragen

1. Wat is een rand, uitgelegd zonder formules?
2. Waarom vervaag je een beeld voordat je randen zoekt?
3. Wat gebeurt er als je de lage drempel van Canny te laag kiest?
