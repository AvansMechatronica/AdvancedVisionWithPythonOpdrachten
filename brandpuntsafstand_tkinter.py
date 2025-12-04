import tkinter as tk
from tkinter import ttk, messagebox

def bereken_brandpuntsafstand():
    """Haalt de waarden op, voert de berekening uit en toont het resultaat."""
    try:
        # 1. Waarden uit de invoervelden ophalen en converteren naar float
        beeld_breedte = float(entry_beeld_breedte.get())
        sensor_breedte = float(entry_sensor_breedte.get())
        werk_afstand = float(entry_werk_afstand.get())

        # 2. Validatie (voorkom delen door nul en negatieve waarden)
        if beeld_breedte <= 0 or sensor_breedte <= 0 or werk_afstand <= 0:
            messagebox.showerror("Fout", "Alle waarden moeten groter zijn dan nul.")
            return

        # 3. Berekening
        # f = (sensor_breedte * werk_afstand) / beeld_breedte
        brandpunts_afstand = (sensor_breedte * werk_afstand) / beeld_breedte

        # 4. Resultaat in het label tonen
        resultaat_label.config(text=f"Benodigde brandpuntsafstand: {brandpunts_afstand:.2f} mm")

    except ValueError:
        # Foutmelding als de gebruiker geen geldige getallen invoert
        messagebox.showerror("Fout", "Ongeldige invoer. Voer alstublieft alleen getallen in.")
    except Exception as e:
        # Algemene foutafhandeling
        messagebox.showerror("Fout", f"Er is een onverwachte fout opgetreden: {e}")

# --- Hoofdvenster aanmaken ---
root = tk.Tk()
root.title("Lens Brandpuntsafstand Calculator")
root.geometry("400x250") # Stel een vaste grootte in

# Frame voor betere opmaak
main_frame = ttk.Frame(root, padding="10")
main_frame.pack(fill='both', expand=True)

# --- Invoervelden aanmaken ---

# Veld 1: Beeldbreedte
ttk.Label(main_frame, text="Beeldbreedte (mm):").grid(row=0, column=0, sticky='w', pady=5)
entry_beeld_breedte = ttk.Entry(main_frame, width=20)
entry_beeld_breedte.grid(row=0, column=1, pady=5)

# Veld 2: Sensorbreedte
ttk.Label(main_frame, text="Sensorbreedte (mm):").grid(row=1, column=0, sticky='w', pady=5)
entry_sensor_breedte = ttk.Entry(main_frame, width=20)
entry_sensor_breedte.grid(row=1, column=1, pady=5)

# Veld 3: Werkafstand
ttk.Label(main_frame, text="Werkafstand (mm):").grid(row=2, column=0, sticky='w', pady=5)
entry_werk_afstand = ttk.Entry(main_frame, width=20)
entry_werk_afstand.grid(row=2, column=1, pady=5)

# --- Knop voor de berekening ---
bereken_knop = ttk.Button(main_frame, text="Bereken Brandpuntsafstand", command=bereken_brandpuntsafstand)
bereken_knop.grid(row=3, column=0, columnspan=2, pady=15)

# --- Resultaat Label ---
resultaat_label = ttk.Label(main_frame, text="Voer waarden in en klik op Berekenen", font=('Helvetica', 10, 'bold'))
resultaat_label.grid(row=4, column=0, columnspan=2, pady=10)

# Laat het venster draaien
root.mainloop()