import tkinter as tk
from tkinter import ttk, messagebox

def f_stop_berekenen(focal_length_mm, aperture_diameter_mm):
    """Bereken het f-getal (f-stop)."""
    if focal_length_mm <= 0 or aperture_diameter_mm <= 0:
        raise ValueError("Brandpuntsafstand en lensopening moeten positief zijn.")
    return focal_length_mm / aperture_diameter_mm

def aperture_diameter_berekenen(focal_length_mm, f_number):
    """Bereken de lensopening (diameter) uit brandpuntsafstand en f-getal."""
    if focal_length_mm <= 0 or f_number <= 0:
        raise ValueError("Brandpuntsafstand en f-stop moeten positief zijn.")
    return focal_length_mm / f_number

def voer_berekening_uit():
    """Haalt de waarden op uit de GUI en voert de f-stop berekeningen uit."""
    try:
        # --- Gegevens Lens 1 ophalen ---
        f1_str = entry_f1.get()
        D1_str = entry_D1.get()

        if not f1_str or not D1_str:
            messagebox.showwarning("Invoerfout", "Vul alstublieft brandpuntsafstand en lensopening voor lens 1 in.")
            return

        f1 = float(f1_str)
        D1 = float(D1_str)

        # --- Berekening (a): f-stop voor lens 1 ---
        N1 = f_stop_berekenen(f1, D1)
        result_a_label.config(text=f"a). f-stop Lens 1: f/{N1:.2f}")

        # --- Gegevens Lens 2 ophalen ---
        f2_str = entry_f2.get()

        if not f2_str:
            messagebox.showwarning("Invoerfout", "Vul alstublieft de brandpuntsafstand voor lens 2 in.")
            return

        f2 = float(f2_str)

        # --- Berekening (b): Lensopening voor lens 2 met zelfde f-stop ---
        # Zelfde hoeveelheid licht betekent zelfde f-stop (N2 = N1)
        N2 = N1
        D2 = aperture_diameter_berekenen(f2, N2)
        result_b_label.config(text=f"b). Lens 2 (f={f2:.2f}mm): Zelfde lichtsterkte bij f/{N2:.2f} → Opening = {D2:.2f} mm")

    except ValueError as ve:
        messagebox.showerror("Invoerfout", f"Ongeldige invoer: {ve}\nVoer alstublieft geldige getallen in.")
    except Exception as e:
        messagebox.showerror("Fout", f"Er is een onverwachte fout opgetreden: {e}")

# --- Hoofdvenster aanmaken ---
root = tk.Tk()
root.title("F-stop & Lensopening Calculator")

# Frame voor betere opmaak
main_frame = ttk.Frame(root, padding="15")
main_frame.pack(fill='both', expand=True)

# --- Sectie voor Lens 1 ---
ttk.Label(main_frame, text="Gegevens Lens 1 (voor vraag a):", font=('Helvetica', 10, 'bold')).grid(row=0, column=0, columnspan=2, sticky='w', pady=(0, 10))

ttk.Label(main_frame, text="Brandpuntsafstand f1 (mm):").grid(row=1, column=0, sticky='w', pady=5)
entry_f1 = ttk.Entry(main_frame, width=20)
entry_f1.grid(row=1, column=1, pady=5)

ttk.Label(main_frame, text="Lensopening D1 (mm):").grid(row=2, column=0, sticky='w', pady=5)
entry_D1 = ttk.Entry(main_frame, width=20)
entry_D1.grid(row=2, column=1, pady=5)

result_a_label = ttk.Label(main_frame, text="a). f-stop Lens 1: ", font=('Helvetica', 10, 'italic'))
result_a_label.grid(row=3, column=0, columnspan=2, sticky='w', pady=(10, 15))


# --- Sectie voor Lens 2 ---
ttk.Label(main_frame, text="Gegevens Lens 2 (voor vraag b):", font=('Helvetica', 10, 'bold')).grid(row=4, column=0, columnspan=2, sticky='w', pady=(0, 10))

ttk.Label(main_frame, text="Brandpuntsafstand f2 (mm):").grid(row=5, column=0, sticky='w', pady=5)
entry_f2 = ttk.Entry(main_frame, width=20)
entry_f2.grid(row=5, column=1, pady=5)

result_b_label = ttk.Label(main_frame, text="b). Lens 2 (f=?mm): Zelfde lichtsterkte bij f/? → Opening = ? mm", font=('Helvetica', 10, 'italic'))
result_b_label.grid(row=6, column=0, columnspan=2, sticky='w', pady=(10, 15))


# --- Knop voor de berekening ---
bereken_knop = ttk.Button(main_frame, text="Voer Berekening Uit", command=voer_berekening_uit)
bereken_knop.grid(row=7, column=0, columnspan=2, pady=20, sticky='we')

# Start de hoofdloop van het Tkinter venster
root.mainloop()