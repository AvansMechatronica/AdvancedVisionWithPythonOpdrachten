def minimale_line_rate(verplaatsing_mm_per_s, pixel_resolutie_mm):
    """
    Bereken de minimale line rate van een lijnscancamera.

    verplaatsing_mm_per_s: snelheid van het object in mm/s
    pixel_resolutie_mm: resolutie per pixel in mm/pixel

    Retourneert: line rate in Hz
    """
    line_rate_hz = verplaatsing_mm_per_s / pixel_resolutie_mm
    return line_rate_hz


# Invoer van de gebruiker
v = float(input("Geef de verplaatsingssnelheid in mm/s: "))
r = float(input("Geef de pixelresolutie in mm/pixel: "))

line_rate = minimale_line_rate(v, r)
print(f"Minimale line rate: {line_rate / 1000:.2f} kHz ({line_rate:.0f} Hz)")
