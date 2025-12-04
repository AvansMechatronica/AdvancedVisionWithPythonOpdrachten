import tkinter as tk
from tkinter import ttk, messagebox
import math


def minimale_sensor_pixels(fov_mm, kleinste_kenmerk_mm, pixels_per_kenmerk):
    """
    Bereken de minimale sensorafmeting in pixels op basis van de resolutie-eis.

    Args:
        fov_mm (float): Field of View (gezichtsveld) in mm.
        kleinste_kenmerk_mm (float): Kleinste detail dat moet worden geregistreerd in mm.
        pixels_per_kenmerk (int): Minimaal aantal pixels per kleinste kenmerk.

    Returns:
        int: De minimaal vereiste sensorafmeting in pixels.
    """
    # 1. Berekenen hoeveel 'kleinste kenmerken' er in de FOV passen
    # Dit is de benodigde ruimtelijke resolutie (resolutie in lijnen)
    aantal_kenmerken = fov_mm / kleinste_kenmerk_mm

    # 2. Toepassen van de bemonsteringsregel (pixels per kenmerk)
    min_pixels = aantal_kenmerken * pixels_per_kenmerk

    # We ronden het resultaat omhoog af naar de dichtstbijzijnde integer, 
    # omdat je geen fractionele pixel kunt hebben.
    return math.ceil(min_pixels)


def voer_berekening_uit():
    """Haalt de waarden op uit de GUI en voert de berekening uit."""
    try:
        # 1. Waarden uit de invoervelden ophalen
        fov = float(entry_fov.get())
        kleinste_kenmerk = float(entry_kenmerk.get())
        pixels_per_detail = int(entry_pixels_detail.get())

        # 2. Validatie
        if fov <= 0 or kleinste_kenmerk <= 0 or pixels_per_detail <= 0:
            messagebox.showerror("Fout", "Alle waarden moeten groter zijn dan nul.")
            return

        # 3. Berekening uitvoeren
        min_pixels = minimale_sensor_pixels(fov, kleinste_kenmerk, pixels_per_detail)

        # 4. Resultaat in het label tonen
        resultaat_label.config(
            text=f"Minimaal vereiste sensorafmeting:\n{min_pixels} pixels",
            foreground="darkgreen"
        )

    except ValueError:
        messagebox.showerror("Fout", "Ongeldige invoer. Voer alstublieft geldige nummers in.")
    except Exception as e:
        messagebox.showerror("Fout", f"Er is een onverwachte fout opgetreden: {e}")


# --- Hoofdvenster aanmaken ---
root = tk.Tk()
root.title("Minimale Sensorresolutie Calculator")
root.geometry("400x250")

# Frame voor betere opmaak
main_frame = ttk.Frame(root, padding="15")
main_frame.pack(fill='both', expand=True)

# --- Invoervelden aanmaken ---

# Veld 1: FOV
ttk.Label(main_frame, text="1. Field of View (FOV) in mm:").grid(row=0, column=0, sticky='w', pady=5)
entry_fov = ttk.Entry(main_frame, width=20)
entry_fov.grid(row=0, column=1, pady=5)
entry_fov.insert(0, "50")  # Voorbeeldwaarde

# Veld 2: Kleinste Kenmerk
ttk.Label(main_frame, text="2. Kleinste detail (mm):").grid(row=1, column=0, sticky='w', pady=5)
entry_kenmerk = ttk.Entry(main_frame, width=20)
entry_kenmerk.grid(row=1, column=1, pady=5)
entry_kenmerk.insert(0, "0.1")  # Voorbeeldwaarde

# Veld 3: Pixels per Detail
ttk.Label(main_frame, text="3. Min. pixels per detail (meestal 2):").grid(row=2, column=0, sticky='w', pady=5)
entry_pixels_detail = ttk.Entry(main_frame, width=20)
entry_pixels_detail.grid(row=2, column=1, pady=5)
entry_pixels_detail.insert(0, "2")  # Standaardwaarde (Nyquist-criterium)

# --- Knop voor de berekening ---
bereken_knop = ttk.Button(main_frame, text="Bereken Minimale Pixels", command=voer_berekening_uit)
bereken_knop.grid(row=3, column=0, columnspan=2, pady=15, sticky='we')

# --- Resultaat Label ---
resultaat_label = ttk.Label(main_frame, text="Voer waarden in en bereken.", font=('Helvetica', 11, 'bold'))
resultaat_label.grid(row=4, column=0, columnspan=2, pady=10)

# Start de hoofdloop van het Tkinter venster
root.mainloop()