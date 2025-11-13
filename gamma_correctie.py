'''
Voor aanpassen van het contrast kan gebruik worden gemaakt van gamma correctie.
Indien voor een 8 bit video systeem de pixel waarde gelijk is aan 136, wat is dan de nieuwe pixelwaarde na gamma correctie, indien gamma de waarde 0,3 heeft.
'''

# gamma_correctie.py

# Vraag invoer
pixel_in = int(input("Geef originele pixelwaarde (0-255): "))
gamma = float(input("Geef gamma waarde: "))

# Gamma correctie
pixel_out = 255 * ((pixel_in / 255) ** gamma)

print(f"Nieuwe pixelwaarde na gamma-correctie = {pixel_out:.2f}")
