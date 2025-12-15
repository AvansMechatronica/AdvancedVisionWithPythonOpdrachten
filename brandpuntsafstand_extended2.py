# Dictionary met veelgebruikte sensorformaten en hun breedte in millimeters
sensor_size = {
    "1/4 inch": 3.6,
    "1/3 inch": 4.8,
    "1/2 inch": 6.4,
    "1/1.8 inch": 7.1,
    "2/3 inch": 8.8,
    "1 inch": 12.8,
}

# Vraag de gebruiker om de invoerwaarden
beeld_breedte = float(input("Beeldbreedte (mm): "))
werk_afstand = float(input("Werkafstand (mm): "))
brandpunts_afstand = float(input("Brandpuntsafstand (mm): "))

# Bereken de sensorgrootte
# Formule omzetten: sensor_breedte = (beeld_breedte * brandpunts_afstand) / werk_afstand
sensor_breedte = (beeld_breedte * brandpunts_afstand) / werk_afstand

# Zoek het meest overeenkomstige sensorformaat
meest_dicht = min(sensor_size.items(), key=lambda x: abs(x[1] - sensor_breedte))

print(f"\nBerekende sensorgrootte: {sensor_breedte:.2f} mm")
print(f"Meest overeenkomstig sensorformaat: {meest_dicht[0]} ({meest_dicht[1]} mm)")
