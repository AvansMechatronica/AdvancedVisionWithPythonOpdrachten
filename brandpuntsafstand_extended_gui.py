import tkinter as tk
from tkinter import ttk, messagebox

# Dictionary met veelgebruikte sensorformaten en hun breedte in millimeters
SENSOR_SIZE_DATA = {
    "1/4 inch": 3.6,
    "1/3 inch": 4.8,
    "1/2 inch": 6.4,
    "1/1.8 inch": 7.1,
    "2/3 inch": 8.8,
    "1 inch": 12.8,
}
# Maak een lijst van de formaten voor de dropdown
sensor_formaten = list(SENSOR_SIZE_DATA.keys())

def bereken_brandpuntsafstand():
    """Haalt de geselecteerde sensor, invoerwaarden op, voert de berekening uit en toont het resultaat."""
    try:
        # 1. Gekozen sensorformaat en de bijbehorende breedte ophalen
        gekozen_formaat = combo_sensor.get()
        if not gekozen_formaat:
            messagebox.showwarning("Invoer ontbreekt", "Kies alstublieft een sensorformaat.")
            return

        sensor_breedte = SENSOR_SIZE_DATA[gekozen_formaat]

        # 2. Waarden uit de invoervelden ophalen en converteren naar float
        beeld_breedte = float(entry_beeld_breedte.get())
        werk_afstand = float(entry_werk_afstand.get())

        # 3. Validatie
        if beeld_breedte <= 0 or werk_afstand <= 0:
            messagebox.showerror("Fout", "Beeldbreedte en Werkafstand moeten positieve waarden zijn.")
            return

        # 4. Berekening
        # formule: f = (sensor_breedte * werk_afstand) / beeld_breedte
        brandpunts_afstand = (sensor_breedte * werk_afstand) / beeld_breedte

        # 5. Resultaat in het label tonen
        resultaat_label.config(
            text=f"Resultaat: {brandpunts_afstand:.2f} mm\n(Gekozen Sensor: {gekozen_formaat} / {sensor_breedte} mm)"
        )

    except ValueError:
        # Foutmelding als de gebruiker geen geldige getallen invoert
        messagebox.showerror("Fout", "Ongeldige invoer. Voer alstublieft geldige nummers in voor de afstanden.")
    except Exception as e:
        # Algemene foutafhandeling
        messagebox.showerror("Fout", f"Er is een onverwachte fout opgetreden: {e}")

# --- Hoofdvenster aanmaken ---
root = tk.Tk()
root.title("Lens Brandpuntsafstand Calculator")
# Frame voor betere opmaak
main_frame = ttk.Frame(root, padding="15")
main_frame.pack(fill='both', expand=True)

# --- Widgets voor Invoer ---

# Rij 0: Sensor keuze (Dropdown)
ttk.Label(main_frame, text="1. Kies Sensorformaat:").grid(row=0, column=0, sticky='w', pady=5)
combo_sensor = ttk.Combobox(main_frame, values=sensor_formaten, state="readonly", width=25)
combo_sensor.grid(row=0, column=1, pady=5)
# Selecteer de eerste in de lijst als standaard
if sensor_formaten:
    combo_sensor.set(sensor_formaten[0])

# Rij 1: Beeldbreedte (Field of View)
ttk.Label(main_frame, text="2. Beeldbreedte (mm) [FOV]:").grid(row=1, column=0, sticky='w', pady=5)
entry_beeld_breedte = ttk.Entry(main_frame, width=28)
entry_beeld_breedte.grid(row=1, column=1, pady=5)

# Rij 2: Werkafstand (Working Distance)
ttk.Label(main_frame, text="3. Werkafstand (mm) [WD]:").grid(row=2, column=0, sticky='w', pady=5)
entry_werk_afstand = ttk.Entry(main_frame, width=28)
entry_werk_afstand.grid(row=2, column=1, pady=5)

# --- Knop voor de berekening ---
bereken_knop = ttk.Button(main_frame, text="Bereken Brandpuntsafstand (f)", command=bereken_brandpuntsafstand)
bereken_knop.grid(row=3, column=0, columnspan=2, pady=20, sticky='we')

# --- Resultaat Label ---
resultaat_label = ttk.Label(main_frame, text="Voer waarden in en klik op Berekenen", font=('Helvetica', 11, 'bold'))
resultaat_label.grid(row=4, column=0, columnspan=2, pady=10)

# Start de hoofdloop van het Tkinter venster
root.mainloop()