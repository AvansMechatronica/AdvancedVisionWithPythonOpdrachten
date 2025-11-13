# Functie om minimale sensorafmeting in pixels te berekenen
def minimale_sensor_pixels(fov_mm, kleinste_kenmerk_mm, pixels_per_kenmerk=2):
    """
    fov_mm: Field of View in mm
    kleinste_kenmerk_mm: kleinste detail dat moet worden geregistreerd in mm
    pixels_per_kenmerk: minimaal aantal pixels per kleinste kenmerk (standaard = 2)
    """
    aantal_kenmerken = fov_mm / kleinste_kenmerk_mm
    min_pixels = aantal_kenmerken * pixels_per_kenmerk
    return int(min_pixels)

# Voorbeeld: invoer van de gebruiker
fov = float(input("Geef de FOV in mm: "))
kleinste_kenmerk = float(input("Geef het kleinste kenmerk in mm: "))
pixels_per_detail = int(input("Minimaal aantal pixels per kleinste detail (standaard 2): ") or 2)

min_pixels = minimale_sensor_pixels(fov, kleinste_kenmerk, pixels_per_detail)
print(f"Minimale sensorafmeting: {min_pixels} pixels")
