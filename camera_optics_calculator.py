"""
camera_optics_calculator_input.py

Interactieve rekenhulp voor camera-optica.
Alle invoer gebeurt via input() en resultaten worden overzichtelijk weergegeven.
Eenheden: mm (millimeter), nm (nanometer voor golflengte).
"""

import math

# ---- BASISFUNCTIES ----
def image_distance(f, s):
    """Bereken afbeeldingsafstand s' volgens de dunne-lensformule: 1/f = 1/s + 1/s'."""
    denom = (1.0 / f) - (1.0 / s)
    if abs(denom) < 1e-12:
        return float('inf')
    return 1.0 / denom


def magnification(s_prime, s):
    """Bereken de vergroting M = s' / s."""
    return s_prime / s


def fov_deg(f, sensor_dim):
    """Bereken de beeldhoek (Field of View) in graden."""
    return 2.0 * math.degrees(math.atan(sensor_dim / (2.0 * f)))


def diagonal(w, h):
    """Bereken de diagonale afmeting van de sensor."""
    return math.sqrt(w*w + h*h)


def hyperfocal(f, N, c):
    """Bereken de hyperfocale afstand (H)."""
    return (f*f) / (N * c) + f


def dof_near_far(s, f, N, c):
    """Bereken de scherptediepte (Depth of Field) en de nabije en verre grenzen."""
    H = hyperfocal(f, N, c)
    near = (H * s) / (H + (s - f))
    denom_far = (H - (s - f))
    if denom_far <= 0:
        far = float('inf')
    else:
        far = (H * s) / denom_far
    dof = None if math.isinf(far) else (far - near)
    return H, near, far, dof


def airy_disk_diameter_mm(wavelength_nm, N):
    """Bereken de diameter van de Airy-schijf (diffractielimiet)."""
    lam_mm = wavelength_nm * 1e-6
    return 2.44 * lam_mm * N


def airy_disk_in_pixels(airy_mm, pixel_size_mm):
    """Bereken hoeveel pixels breed de Airy-schijf is."""
    if pixel_size_mm <= 0:
        return float('nan')
    return airy_mm / pixel_size_mm


def aperture_diameter(f, N):
    """Bereken de effectieve lensopening (diameter in mm)."""
    return f / N


# ---- INTERACTIEVE VERSIE ----
if __name__ == "__main__":
    print("=== CAMERA OPTICS CALCULATOR ===")
    print("Voer waarden in (voorbeeldwaarden tussen haakjes).")

    # Gebruikersinvoer
    f = float(input("Brandpuntsafstand f (mm) [bijv. 25]: ") or 25)
    sensor_w = float(input("Sensorbreedte (mm) [bijv. 6.4]: ") or 6.4)
    sensor_h = float(input("Sensorhoogte (mm) [bijv. 4.8]: ") or 4.8)
    s = float(input("Objectafstand s (mm) [bijv. 500]: ") or 500)
    N = float(input("Diafragma (f-getal) N [bijv. 4.0]: ") or 4.0)
    c = float(input("Cirkeltje van verwarring c (mm) [bijv. 0.02]: ") or 0.02)
    wavelength_nm = float(input("Golflengte (nm) [bijv. 550]: ") or 550)
    pixel_size_mm = float(input("Pixelgrootte (mm) [bijv. 0.0022]: ") or 0.0022)

    # ---- BEREKENINGEN ----
    s_prime = image_distance(f, s)
    M = magnification(s_prime, s)
    fov_h = fov_deg(f, sensor_w)
    fov_v = fov_deg(f, sensor_h)
    fov_d = fov_deg(f, diagonal(sensor_w, sensor_h))
    H, near, far, dof = dof_near_far(s, f, N, c)
    airy_mm = airy_disk_diameter_mm(wavelength_nm, N)
    airy_px = airy_disk_in_pixels(airy_mm, pixel_size_mm)
    aperture_mm = aperture_diameter(f, N)

    # ---- RESULTATEN WEERGEVEN ----
    print("\n=== RESULTATEN ===")
    print(f"Afbeeldingsafstand s' = {s_prime:.2f} mm")
    print(f"Vergroting M = {M:.4f}")
    print(f"Beeldhoek horizontaal = {fov_h:.2f}°")
    print(f"Beeldhoek verticaal   = {fov_v:.2f}°")
    print(f"Beeldhoek diagonaal   = {fov_d:.2f}°")
    print(f"Hyperfocale afstand H = {H:.2f} mm")
    print(f"Nabije grens scherpte = {near:.2f} mm")
    if math.isinf(far):
        print(f"Verre grens scherpte  = ∞ (oneindig)")
    else:
        print(f"Verre grens scherpte  = {far:.2f} mm")
    print(f"Scherptediepte (DOF)  = {'oneindig' if dof is None else f'{dof:.2f} mm'}")
    print(f"Airy-schijf diameter  = {airy_mm*1000:.2f} µm")
    print(f"Airy-schijf in pixels = {airy_px:.2f} px")
    print(f"Lensopening (diameter) = {aperture_mm:.2f} mm")

    print("\n--- Berekening voltooid ---")
