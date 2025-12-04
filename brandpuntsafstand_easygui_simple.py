import easygui
import sys


def bereken_brandpuntsafstand(sensor_mm, werk_afstand_mm, beeld_breedte_mm):
    """
    Bereken de brandpuntsafstand (f) in mm.
    Formule: f = (sensor_breedte * werk_afstand) / beeld_breedte
    """
    if beeld_breedte_mm == 0:
        raise ZeroDivisionError("De beeldbreedte (FOV) kan niet nul zijn.")

    return (sensor_mm * werk_afstand_mm) / beeld_breedte_mm


# --- Start het Programma ---
titel = "Brandpuntsafstand Calculator (f)"
easygui.msgbox("Welkom bij de Brandpuntsafstand Calculator.\nWe verzamelen nu drie waarden.", titel)

# --- Invoer Stap 1: Beeldbreedte (FOV) ---
beeld_breedte = easygui.enterbox(
    "1/3. Geef de **Beeldbreedte (FOV)** in mm (bijv. 50):",
    titel,
    default="50"
)
if beeld_breedte is None: sys.exit(0)

# --- Invoer Stap 2: Sensorbreedte ---
sensor_breedte = easygui.enterbox(
    "2/3. Geef de **Sensorbreedte** in mm (bijv. 6.4):",
    titel,
    default="6.4"
)
if sensor_breedte is None: sys.exit(0)

# --- Invoer Stap 3: Werkafstand ---
werk_afstand = easygui.enterbox(
    "3/3. Geef de **Werkafstand** in mm (bijv. 100):",
    titel,
    default="100"
)
if werk_afstand is None: sys.exit(0)

try:
    # 1. Converteer de ingevoerde strings naar floats
    bb = float(beeld_breedte)
    sb = float(sensor_breedte)
    wa = float(werk_afstand)

    # 2. Validatie
    if bb <= 0 or sb <= 0 or wa <= 0:
        raise ValueError("Alle waarden moeten groter zijn dan nul.")

    # 3. Berekening uitvoeren
    f = bereken_brandpuntsafstand(sb, wa, bb)

    # 4. Resultaat tonen
    resultaat_titel = "Resultaat Brandpuntsafstand"
    resultaat_boodschap = f"""
    ✅ Berekening Geslaagd!

    Beeldbreedte: {bb} mm
    Sensorbreedte: {sb} mm
    Werkafstand: {wa} mm

    --------------------------------
    Benodigde Brandpuntsafstand (f): {f:.2f} mm
    """
    easygui.msgbox(resultaat_boodschap, resultaat_titel)

except ValueError:
    easygui.exceptionbox("Ongeldige invoer! Zorg ervoor dat u alleen geldige positieve nummers invoert.",
                         "Fout in Invoer")
except ZeroDivisionError as zde:
    easygui.exceptionbox(str(zde), "Fout in Berekening")
except Exception as e:
    easygui.exceptionbox(f"Er is een onverwachte fout opgetreden: {e}", "Algemene Fout")