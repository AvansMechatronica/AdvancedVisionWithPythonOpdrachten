def bereken_voorwerpsafstand(fov_mm, sensor_mm, brandpuntsafstand_mm):
    """
    fov_mm: Field of View in mm (bijv. breedte of hoogte)
    sensor_mm: Sensorafmeting in dezelfde richting (mm)
    brandpuntsafstand_mm: brandpuntsafstand van de lens (mm)

    Retourneert: voorwerpsafstand D in mm
    """
    D = brandpuntsafstand_mm * (fov_mm / sensor_mm)
    return D


# Voorbeeld invoer
fov_breedte = float(input("Geef de FOV breedte in mm: "))
sensor_breedte = float(input("Geef de sensor breedte in mm: "))
brandpuntsafstand = float(input("Geef de brandpuntsafstand van de lens in mm: "))

D = bereken_voorwerpsafstand(fov_breedte, sensor_breedte, brandpuntsafstand)
print(f"Voorwerpsafstand: {D:.2f} mm")
