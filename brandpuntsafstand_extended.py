# Dictionary met veelgebruikte sensorformaten en hun breedte in millimeters
sensor_size = {
    "1/4 inch": 3.6,
    "1/3 inch": 4.8,
    "1/2 inch": 6.4,
    "1/1.8 inch": 7.1,
    "2/3 inch": 8.8,
    "1 inch": 12.8,
}

# Maak een lijst van de keys zodat we er met een nummer (index) uit kunnen kiezen
keys = list(sensor_size.keys())

# Toon alle beschikbare sensoren in een overzichtelijke lijst
print("Beschikbare sensorformaten:")
for i, key in enumerate(keys, 1):  # nummering start bij 1
    print(f"{i}. {key} → {sensor_size[key]} mm")

# Vraag de gebruiker om een sensor te kiezen via het nummer in de lijst
keuze_nummer = int(input("Kies sensor door nummer: "))

# Controleer of de keuze geldig is (tussen 1 en het aantal sensoren)
if 1 <= keuze_nummer <= len(keys):
    gekozen_formaat = keys[keuze_nummer - 1]  # index = nummer - 1
    sensor_breedte = sensor_size[gekozen_formaat]
    print(f"Gekozen sensor: {gekozen_formaat} → {sensor_breedte} mm")
else:
    raise ValueError("Ongeldig nummer gekozen!")

# Vraag de gebruiker om de gewenste beeldbreedte (het gezichtsveld op het object)
beeld_breedte = float(input("Beeldbreedte (mm): "))  # bijvoorbeeld 50 mm

# Vraag de werkafstand (afstand tussen lens en object)
werk_afstand = float(input("Werkafstand (mm): "))    # bijvoorbeeld 100 mm

# Bereken de benodigde brandpuntsafstand van de lens:
# formule: f = (sensor_breedte * werk_afstand) / beeld_breedte
brandpunts_afstand = (sensor_breedte * werk_afstand) / beeld_breedte

# Toon het resultaat op het scherm met twee decimalen
print(f"Benodigde brandpuntsafstand: {brandpunts_afstand:.2f} mm")
