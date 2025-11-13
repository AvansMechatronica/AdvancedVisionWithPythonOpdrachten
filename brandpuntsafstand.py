# Vraag de gebruiker om de beeldbreedte in mm (de breedte van het gezichtsveld op het object)
beeld_breedte = float(input("Beeldbreedte (mm): "))  # bijv. 50 mm

# Vraag de gebruiker om de sensorbreedte in mm (de fysieke breedte van de camerasensor)
sensor_breedte = float(input("Sensorbreedte (mm): "))  # bijv. 6.4 mm

# Vraag de gebruiker om de werkafstand in mm (afstand tussen lens en object)
werk_afstand = float(input("Werkafstand (mm): "))  # bijv. 100 mm

# Bereken de benodigde brandpuntsafstand van de lens met de formule:
# f = (sensor_breedte * werk_afstand) / beeld_breedte
brandpunts_afstand = (sensor_breedte * werk_afstand) / beeld_breedte

# Toon de berekende brandpuntsafstand
print(f"Benodigde brandpuntsafstand: {brandpunts_afstand:.2f} mm")
