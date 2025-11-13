'''
Met de f-stop wordt de lensopening aangepast door diafragma te veranderen. Hierdoor wordt de hoeveelheid licht dat de sensor bereikt beïnvloed.
a). Indien het brandpunt van de lens gelijk is aan 8 mm en de lensopening gelijk is aan 2,85 mm, wat is dan de f-stop waarde?
b). Indien een lens met een brandpuntsafstand van 25 mm een zelfde hoeveelheid licht levert op de sensor als het geval is bij vraag (a), wat is dan de f-stop instelling van deze lens?
'''
# f_stop_interactief.py

def f_stop(focal_length_mm, aperture_diameter_mm):
    """Bereken het f-getal (f-stop)"""
    return focal_length_mm / aperture_diameter_mm


def aperture_diameter(focal_length_mm, f_number):
    """Bereken de lensopening (diameter) uit brandpuntsafstand en f-getal"""
    return focal_length_mm / f_number


print("=== Berekening f-stop en lensopening ===\n")

# Vraag gebruiker om gegevens voor lens 1
f1 = float(input("Geef brandpuntsafstand lens 1 (mm): "))
D1 = float(input("Geef lensopening (diameter) van lens 1 (mm): "))

# Bereken f-getal van lens 1
N1 = f_stop(f1, D1)
print(f"\n(a) f = {f1:.2f} mm, D = {D1:.2f} mm → f-stop = f/{N1:.2f}")

# Vraag gebruiker om tweede lens
f2 = float(input("\nGeef brandpuntsafstand van lens 2 (mm): "))

# Zelfde hoeveelheid licht → zelfde f-getal
N2 = N1
D2 = aperture_diameter(f2, N2)
print(f"(b) f = {f2:.2f} mm → zelfde lichtsterkte bij f/{N2:.2f} ⇒ opening = {D2:.2f} mm")

print("\n=== Berekening voltooid ===")
