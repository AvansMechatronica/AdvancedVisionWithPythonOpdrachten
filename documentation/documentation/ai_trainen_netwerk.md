# Trainen van een Neuraal Netwerk

## Inleiding
In deze sectie leer je hoe je een neuraal netwerk kunt trainen met behulp van de verzamelde en gelabelde afbeeldingen. We zullen gebruik maken van populaire machine learning bibliotheken zoals TensorFlow of PyTorch om het netwerk te bouwen, trainen en evalueren. We maken gebruik van het YoloV8 model voor deze opdrachten.

Er zijn twee mogelijkheden om een neuraal netwerk te trainen: lokaal op je eigen computer of in de cloud met behulp van een colab notebook. In deze sectie zullen we beide methoden bespreken, zodat je kunt kiezen welke het beste bij jouw situatie past.


## Opdrachten

:::::{card} 

::::{tab-set}

:::{tab-item} Lokaal Trainen

### Opdracht 1: Installeren van Benodigde Software
1. Zorg ervoor dat je Python en pip op je computer hebt geïnstalleerd.  
clone de volgende repository:  
```
git clone https://github.com/AvansMechatronica/yoloV8_training.git
```

In deze repository vind je alle benodigde python scripts om lokaal een YoloV8 model te trainen.
> Je kunt ook een "fork"van de repository maken als je dat prettiger vindt. De beschrijving hiervoor is te vinden op: https://docs.github.com/en/get-started/quickstart/fork-a-repo

In de repository vindt je volgende scripts:
- `requirements.txt`: Installeer alle benodigde python pakketten.Gebruik daarvoor het volgende commando in de terminal:
```
pip install -r requirements.txt
```
> Let op: In onderstaande scripts zul je nog wel wijzigingen moeten aanbrengen om ze te laten werken met jouw dataset.

> Let op: Voor het trainen van een YoloV8 model is een NVIDIA GPU met de juiste CUDA drivers sterk aanbevolen. Zonder GPU kan het trainen van het model erg lang duren.

- `CudaCheck.py`: Script om te controleren of de juiste CUDA drivers zijn geïnstalleerd. Wanneer dit script een foutmelding geeft, dan moet je de juiste CUDA drivers installeren. Zie hiervoor de NVIDIA website: https://developer.nvidia.com/cuda-downloads. Dit werkt alleen met NVIDIA GPU's.


- `TrainModel.py`: Script om het YoloV8 model te trainen met jouw dataset. Na de training zal er een getraind model worden opgeslagen in de map `runs/train/`. Het model heeft de naam `weights/best.pt`. Dit bestand heb je later nodig om het model te testen of te gebruiken in je opdracht.

- `GetDatasetFromRoboflow.py`: Script om de dataset te downloaden van Roboflow. Vul hier jouw API key en dataset informatie in.

- `DetectImageFromTrainingSet.py`: Script om het getrainde model te testen op afbeeldingen uit de trainingsset.

- `DetectImageFromFile.py`: Script om het getrainde met een willekeurige afbeelding van jouw computer te testen.

- `WebcamVideoStream.py`: Script om het getrainde model te testen met de webcam video stream.

:::

:::{tab-item} In de Cloud Trainen

In colab is al een omgeving ingericht om een YoloV8 model te trainen. Volg de onderstaande stappen om aan de slag te gaan: https://drive.google.com/file/d/1M_Fnquk3dmfuBLfpjgMGVwj35Em1-wfP/view?usp=sharing

### Opdracht 1: Openen van het Colab Notebook
1. Open de bovenstaande link naar het colab notebook in je webbrowser.  
2. Maak een kopie van het notebook door naar 'Bestand' > 'Kopie maken' te gaan. Dit zorgt ervoor dat je een eigen versie hebt waarin je wijzigingen kunt aanbrengen.
3. Volg de instructies in het notebook om de benodigde pakketten te installeren, je dataset te uploaden, en het model te trainen.   
4. Na de training zal het getrainde model worden opgeslagen in je Google Drive. Zorg ervoor dat je dit bestand downloadt en bewaart, aangezien je het later nodig zult hebben om het model te testen of te gebruiken in je opdracht.
5. Download het getrainde model (`best.pt`) van je Google Drive naar je lokale computer voor later gebruik.

> Tip: je kunt de runtime van colab instellen op GPU om de training te versnellen. Ga hiervoor naar 'Runtime' > 'Wijzig runtime type' en selecteer 'GPU' als hardware accelerator.


:::

::::

:::::