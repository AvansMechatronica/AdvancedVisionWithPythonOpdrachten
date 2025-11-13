sensor_size = {
    "1/4 inch": 3.6,
    "1/3 inch": 4.8,
    "1/2 inch": 6.4,
    "1/1.8 inch": 7.1,
    "2/3 inch": 8.8,
    "1 inch": 12.8,
}

# Maak een lijst van de keys zodat we op index kunnen kiezen
keys = list(sensor_size.keys())

print("Beschikbare sensorformaten:")
for i, key in enumerate(keys, 1):
    print(f"{i}. {key} → {sensor_size[key]} mm")

# Kies via nummer
keuze_nummer = int(input("Kies sensor door nummer: "))

# Controleer of nummer geldig is
if 1 <= keuze_nummer <= len(keys):
    gekozen_formaat = keys[keuze_nummer - 1]  # index = nummer - 1
    sensor_breedte = sensor_size[gekozen_formaat]
    print(f"Gekozen sensor: {gekozen_formaat} → {sensor_breedte} mm")
else:
    raise ValueError("Ongeldig nummer gekozen!")

beeld_breedte = float(input("Beeldbreedte (mm): "))  # bv. 50
werk_afstand = float(input("Werkafstand (mm): "))    # bv. 100

# Bereken brandpuntsafstand
brandpunts_afstand = (sensor_breedte * werk_afstand) / beeld_breedte
print(f"Benodigde brandpuntsafstand: {brandpunts_afstand:.2f} mm")
