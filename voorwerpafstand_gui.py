import tkinter as tk
from tkinter import ttk, messagebox


def bereken_voorwerpsafstand(fov_mm, sensor_mm, brandpuntsafstand_mm):
    """
    Bereken de voorwerpsafstand D (werkafstand) in mm.

    De formule is afgeleid van de vergroting (M)
    M = sensor_mm / fov_mm
    M = brandpuntsafstand_mm / D (voor werkafstand D)
    Daaruit volgt: D = brandpuntsafstand_mm * (fov_mm / sensor_mm)

    Retourneert: voorwerpsafstand D in mm
    """
    # Controleer of de sensormaat niet nul is om delen door nul te voorkomen
    if sensor_mm == 0:
        raise ZeroDivisionError("Sensorafmeting kan niet nul zijn.")

    # Berekening
    D = brandpuntsafstand_mm * (fov_mm / sensor_mm)
    return D


def voer_berekening_uit():
    """Haalt de waarden op uit de GUI en voert de berekening uit."""
    try:
        # 1. Waarden uit de invoervelden ophalen
        fov = float(entry_fov.get())
        sensor = float(entry_sensor.get())
        brandpuntsafstand = float(entry_brandpunt.get())

        # 2. Validatie
        if fov <= 0 or sensor <= 0 or brandpuntsafstand <= 0:
            messagebox.showerror("Fout", "Alle waarden (FOV, Sensor, Brandpuntsafstand) moeten positief zijn (> 0).")
            return

        # 3. Berekening uitvoeren
        D = bereken_voorwerpsafstand(fov, sensor, brandpuntsafstand)

        # 4. Resultaat in het label tonen
        resultaat_label.config(
            text=f"Benodigde Werkafstand (D):\n{D:.2f} mm",
            foreground="darkblue"
        )

    except ValueError:
        messagebox.showerror("Fout", "Ongeldige invoer. Voer alstublieft geldige nummers in.")
    except ZeroDivisionError as zde:
        messagebox.showerror("Fout", str(zde))
    except Exception as e:
        messagebox.showerror("Fout", f"Er is een onverwachte fout opgetreden: {e}")


# --- Hoofdvenster aanmaken ---
root = tk.Tk()
root.title("Werkafstand Calculator (D)")
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

# Veld 2: Sensor Breedte/Hoogte (mm)
ttk.Label(main_frame, text="2. Sensor Afmeting (mm):").grid(row=1, column=0, sticky='w', pady=5)
entry_sensor = ttk.Entry(main_frame, width=20)
entry_sensor.grid(row=1, column=1, pady=5)
entry_sensor.insert(0, "6.4")  # Voorbeeldwaarde: 1/2" sensor breedte

# Veld 3: Brandpuntsafstand (f)
ttk.Label(main_frame, text="3. Brandpuntsafstand (f) in mm:").grid(row=2, column=0, sticky='w', pady=5)
entry_brandpunt = ttk.Entry(main_frame, width=20)
entry_brandpunt.grid(row=2, column=1, pady=5)
entry_brandpunt.insert(0, "8")  # Voorbeeldwaarde

# --- Knop voor de berekening ---
bereken_knop = ttk.Button(main_frame, text="Bereken Werkafstand D", command=voer_berekening_uit)
bereken_knop.grid(row=3, column=0, columnspan=2, pady=15, sticky='we')

# --- Resultaat Label ---
resultaat_label = ttk.Label(main_frame, text="Voer waarden in en bereken.", font=('Helvetica', 11, 'bold'))
resultaat_label.grid(row=4, column=0, columnspan=2, pady=10)

# Start de hoofdloop van het Tkinter venster
root.mainloop()