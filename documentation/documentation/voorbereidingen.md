# Voorbereidingen voor de Opdrachten

Voordat je aan de opdrachten begint, is het belangrijk om de volgende voorbereidingen te treffen:

- Instaleer Python, zie [Installatie Python](installatie_visual_code_python.md)

## Maken van een projectmap
- Maak een map waarin je alle opdrachten en bijbehorende bestanden opslaat. Sla de map bijvoorbeeld op in je documenten of op een andere gemakkelijk toegankelijke locatie. Geef de map een duidelijke naam, zoals "AdvancedVisionWithPython".
- Open Visual Code en navigeer naar de map die je zojuist hebt gemaakt. Gebruik hier de optie "File -> Open folder" in Visual Code.

:::{note}
Als er gevraag wordt of de map te vertrouwen(trust) is, bevestig dit zodat Visual Code toegang krijgt tot de map.

Let op: Deze mededeling is soms een Popup of soms een banner bovenin Visual Code.
:::

## Maken van een virtuele Python-omgeving
Een Python-environment (omgeving) is eigenlijk een afzonderlijke “werkruimte” voor Python waarin je je programma’s draait en afhankelijkheden (libraries) installeert.

Visual Code maakt gebruik van virtuele environments:
* Een lokaal, geïsoleerd Python-systeem voor één project.
* Je installeert libraries alleen binnen dat environment.

Open de Python-environment selector in Visual Code om de virtuele omgeving te activeren. Kies voor Python 3.12 als je ook andere versies van Python op je systeem hebt geïnstalleerd.

![image](../images/environmet-selector.png)

:::{note}
- Selecteer Python icoontje aan de linkerkant van Visual Code.
- Kies `Custom`
- Bevestig de locatie `.venv`.
- Skip package installation
:::



>Er is nu een map ".venv" in je Project gemaakt

Hierna is de programmeeromgeving gereed voor gebruik. 😃Happy coding !!!

## Maken van je eerste Python-programma

1. Open Visual Code en navigeer naar de map waarin je de virtuele omgeving hebt aangemaakt.
2. Maak een nieuw Python-bestand aan door te klikken op "File -> New File" en sla het bestand op met de extensie `.py`, bijvoorbeeld `main.py`.
3. Copieer de onderstaand voorbeeldcode hieronder in je nieuwe Python-bestand.
4. Je kunt het programma starten met de `RUN` knop bovenin Visual Code of door de sneltoets `Ctrl + F5` te gebruiken.

Voorbeeld van eerste Python-programma:
```python
print("Hello, World!")
```