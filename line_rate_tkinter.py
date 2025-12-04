import tkinter as tk
from tkinter import ttk, messagebox


def minimale_line_rate_berekenen(verplaatsing_mm_per_s, pixel_resolutie_mm):
    """
    Bereken de minimale line rate van een lijnscancamera.

    Args:
        verplaatsing_mm_per_s (float): Snelheid van het object in mm/s.
        pixel_resolutie_mm (float): Resolutie per pixel in mm/pixel.

    Returns:
        float: line rate in Hz.
    """
    # De formule: Line Rate (Hz) = Snelheid (mm/s) / Pixel Resolutie (mm/pixel)
    return verplaatsing_mm_per_s / pixel_resolutie_mm


def voer_berekening_uit():
    """Haalt de waarden op uit de GUI en voert de berekening uit."""
    try:
        # 1. Waarden uit de invoervelden ophalen
        v = float(entry_snelheid.get())
        r = float(entry_resolutie.get())

        # 2. Validatie
        if v <= 0 or r <= 0:
            messagebox.showerror("Fout", "Snelheid en resolutie moeten positief zijn (> 0).")
            return

        # 3. Berekening uitvoeren
        line_rate_hz = minimale_line_rate_berekenen(v, r)
        line_rate_khz = line_rate_hz / 1000

        # 4. Resultaat in het label tonen
        resultaat_label.config(
            text=f"Minimale Line Rate:\n{line_rate_khz:.2f} kHz ({line_rate_hz:.0f} Hz)",
            foreground="darkblue"
        )

    except ValueError:
        messagebox.showerror("Fout", "Ongeldige invoer. Voer alstublieft geldige nummers in.")
    except Exception as e:
        messagebox.showerror("Fout", f"Er is een onverwachte fout opgetreden: {e}")


# --- Hoofdvenster aanmaken ---
root = tk.Tk()
root.title("Line Rate Calculator (Lijnscancamera)")
root.geometry("400x230")

# Frame voor betere opmaak
main_frame = ttk.Frame(root, padding="15")
main_frame.pack(fill='both', expand=True)

# --- Invoervelden aanmaken ---

# Veld 1: Verplaatsingssnelheid (v)
ttk.Label(main_frame, text="Verplaatsingssnelheid (mm/s):").grid(row=0, column=0, sticky='w', pady=5)
entry_snelheid = ttk.Entry(main_frame, width=20)
entry_snelheid.grid(row=0, column=1, pady=5)
entry_snelheid.insert(0, "1000")  # Voorbeeldwaarde: 1 meter per seconde

# Veld 2: Pixelresolutie (r)
ttk.Label(main_frame, text="Pixelresolutie (mm/pixel):").grid(row=1, column=0, sticky='w', pady=5)
entry_resolutie = ttk.Entry(main_frame, width=20)
entry_resolutie.grid(row=1, column=1, pady=5)
entry_resolutie.insert(0, "0.1")  # Voorbeeldwaarde: 100 µm/pixel

# --- Knop voor de berekening ---
bereken_knop = ttk.Button(main_frame, text="Bereken Line Rate", command=voer_berekening_uit)
bereken_knop.grid(row=2, column=0, columnspan=2, pady=15, sticky='we')

# --- Resultaat Label ---
resultaat_label = ttk.Label(main_frame, text="Voer waarden in en bereken.", font=('Helvetica', 11, 'bold'))
resultaat_label.grid(row=3, column=0, columnspan=2, pady=10)

# Start de hoofdloop van het Tkinter venster
root.mainloop()