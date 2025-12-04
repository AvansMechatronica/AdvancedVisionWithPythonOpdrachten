import easygui
import sys  # Nodig voor het netjes afsluiten als de gebruiker op Annuleren klikt


def bereken_voorwerpsafstand(fov_mm, sensor_mm, brandpuntsafstand_mm):
    """
    Bereken de voorwerpsafstand D (werkafstand) in mm.
    Formule: D = brandpuntsafstand_mm * (fov_mm / sensor_mm)
    """
    if sensor_mm == 0:
        # Dit voorkomt een onverwachte crash door delen door nul
        raise ZeroDivisionError("Sensorafmeting kan niet nul zijn.")
    return brandpuntsafstand_mm * (fov_mm / sensor_mm)


# --- Instellen van het dialoogvenster ---
titel = "Werkafstand Calculator (D)"
boodschap = "Voer de parameters in om de benodigde werkafstand te berekenen."
veldsnamen = ["1. Field of View (FOV) in mm:", "2. Sensor Afmeting (mm):", "3. Brandpuntsafstand (f) in mm:"]
standaardwaarden = ["50", "6.4", "8"]  # Voorbeeldwaarden

# --- Invoer verzamelen ---
output = easygui.multenterbox(boodschap, titel, veldsnamen, standaardwaarden)

# Controleer of de gebruiker op Annuleren heeft geklikt
if output is None:
    sys.exit(0)

try:
    # 1. Waarden uit de lijst halen en converteren naar float
    fov = float(output[0])
    sensor = float(output[1])
    brandpuntsafstand = float(output[2])

    # 2. Validatie
    if fov <= 0 or sensor <= 0 or brandpuntsafstand <= 0:
        raise ValueError("Alle waarden moeten positief zijn (> 0).")

    # 3. Berekening uitvoeren
    D = bereken_voorwerpsafstand(fov, sensor, brandpuntsafstand)

    # 4. Resultaat tonen
    resultaat_titel = "Resultaat Berekening"
    resultaat_boodschap = f"""
    ✅ Berekening Geslaagd!

    FOV: {fov} mm
    Sensor: {sensor} mm
    Brandpunt (f): {brandpuntsafstand} mm

    --------------------------------
    Benodigde Werkafstand (D): {D:.2f} mm
    """
    easygui.msgbox(resultaat_boodschap, resultaat_titel)

except ValueError:
    easygui.exceptionbox("Ongeldige invoer! Zorg ervoor dat u alleen geldige nummers invoert.", "Fout in Invoer")
except ZeroDivisionError as zde:
    easygui.exceptionbox(str(zde), "Fout in Berekening")
except Exception as e:
    easygui.exceptionbox(f"Er is een onverwachte fout opgetreden: {e}", "Algemene Fout")