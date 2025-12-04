import tkinter as tk
from tkinter import ttk, messagebox

# Constante voor 8-bit systeem
P_MAX = 255

def voer_gamma_correctie_uit():
    """Haalt de waarden op, voert de gamma-correctie uit en toont het resultaat."""
    try:
        # 1. Waarden uit de invoervelden ophalen
        pixel_in = float(entry_pixel_in.get())
        gamma = float(entry_gamma.get())

        # 2. Validatie
        if not (0 <= pixel_in <= P_MAX):
            messagebox.showerror("Fout", f"Pixelwaarde moet tussen 0 en {P_MAX} liggen voor een 8-bit systeem.")
            return
        if gamma <= 0:
            messagebox.showerror("Fout", "Gamma-waarde moet positief zijn (> 0).")
            return

        # 3. Gamma Correctie Formule: P_out = P_max * (P_in / P_max) ** gamma
        pixel_out = P_MAX * ((pixel_in / P_MAX) ** gamma)

        # 4. Resultaat in het label tonen
        resultaat_label.config(
            text=f"Nieuwe pixelwaarde na gamma-correctie:\n{pixel_out:.2f}"
        )

    except ValueError:
        # Foutmelding als de gebruiker geen geldige getallen invoert
        messagebox.showerror("Fout", "Ongeldige invoer. Voer alstublieft geldige nummers in.")
    except Exception as e:
        # Algemene foutafhandeling
        messagebox.showerror("Fout", f"Er is een onverwachte fout opgetreden: {e}")

# --- Hoofdvenster aanmaken ---
root = tk.Tk()
root.title("Gamma Correctie Calculator (8-bit)")
root.geometry("350x250")

# Frame voor betere opmaak
main_frame = ttk.Frame(root, padding="15")
main_frame.pack(fill='both', expand=True)

# --- Invoervelden aanmaken ---

# Veld 1: Originele Pixelwaarde (0-255)
ttk.Label(main_frame, text=f"Originele Pixelwaarde (0-{P_MAX}):").grid(row=0, column=0, sticky='w', pady=5)
entry_pixel_in = ttk.Entry(main_frame, width=20)
entry_pixel_in.grid(row=0, column=1, pady=5)

# Veld 2: Gamma Waarde
ttk.Label(main_frame, text="Gamma Waarde (γ):").grid(row=1, column=0, sticky='w', pady=5)
entry_gamma = ttk.Entry(main_frame, width=20)
entry_gamma.grid(row=1, column=1, pady=5)

# Standaardwaarden instellen (voor de gevraagde berekening: 136 en 0.3)
entry_pixel_in.insert(0, "136")
entry_gamma.insert(0, "0.3")

# --- Knop voor de berekening ---
bereken_knop = ttk.Button(main_frame, text="Voer Gamma Correctie Uit", command=voer_gamma_correctie_uit)
bereken_knop.grid(row=2, column=0, columnspan=2, pady=15, sticky='we')

# --- Resultaat Label ---
resultaat_label = ttk.Label(main_frame, text="Druk op de knop om te berekenen.", font=('Helvetica', 10, 'bold'))
resultaat_label.grid(row=3, column=0, columnspan=2, pady=10)

# Start de hoofdloop van het Tkinter venster
root.mainloop()