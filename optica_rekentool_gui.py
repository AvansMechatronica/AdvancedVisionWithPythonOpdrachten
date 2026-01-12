"""
Optica Rekentool - GUI Versie
Een complete tool voor optica-gerelateerde berekeningen voor camerasystemen met grafische interface.
"""

import json
import os
import tkinter as tk
from tkinter import ttk, messagebox, filedialog, scrolledtext
from typing import Dict, List, Tuple, Optional


# Database van camera's met hun eigenschappen
CAMERAS = [
    {
        "naam": "Basler acA1920-40uc",
        "resolutie_h": 1920,
        "resolutie_v": 1200,
        "sensor_breedte": 11.26,  # mm
        "sensor_hoogte": 7.05,    # mm
        "flange_focal_distance": 17.526  # mm - afstand van lens mount tot sensor
    },
    {
        "naam": "FLIR Blackfly S BFS-U3-31S4M",
        "resolutie_h": 2048,
        "resolutie_v": 1536,
        "sensor_breedte": 11.26,
        "sensor_hoogte": 8.45,
        "flange_focal_distance": 17.526
    },
    {
        "naam": "Allied Vision Mako G-234",
        "resolutie_h": 1936,
        "resolutie_v": 1216,
        "sensor_breedte": 11.35,
        "sensor_hoogte": 7.13,
        "flange_focal_distance": 17.526
    },
    {
        "naam": "IDS uEye CP",
        "resolutie_h": 1280,
        "resolutie_v": 1024,
        "sensor_breedte": 6.78,
        "sensor_hoogte": 5.43,
        "flange_focal_distance": 17.526
    },
    {
        "naam": "Sony IMX264",
        "resolutie_h": 2448,
        "resolutie_v": 2048,
        "sensor_breedte": 11.26,
        "sensor_hoogte": 9.42,
        "flange_focal_distance": 17.526
    }
]

# Database van lenzen met hun eigenschappen
LENZEN = [
    {
        "naam": "Computar M0814-MP2",
        "brandpuntsafstand": 8,  # mm
        "max_aperture": 1.4,
        "mount": "C-mount"
    },
    {
        "naam": "Kowa LM12HC",
        "brandpuntsafstand": 12,
        "max_aperture": 1.4,
        "mount": "C-mount"
    },
    {
        "naam": "Edmund Optics 16mm",
        "brandpuntsafstand": 16,
        "max_aperture": 1.8,
        "mount": "C-mount"
    },
    {
        "naam": "Fujinon HF25SA-1",
        "brandpuntsafstand": 25,
        "max_aperture": 1.4,
        "mount": "C-mount"
    },
    {
        "naam": "Computar M3514-MP2",
        "brandpuntsafstand": 35,
        "max_aperture": 1.4,
        "mount": "C-mount"
    },
    {
        "naam": "Kowa LM50HC",
        "brandpuntsafstand": 50,
        "max_aperture": 2.8,
        "mount": "C-mount"
    }
]


class OpticaRekenToolGUI:
    """Hoofdapplicatie voor de Optica Rekentool met GUI."""
    
    def __init__(self, root):
        self.root = root
        self.root.title("Optica Rekentool - Camera & Lens Calculator")
        self.root.geometry("1000x800")
        
        # Resultaten opslaan
        self.alle_resultaten = {}
        self.gekozen_camera = None
        self.gekozen_lens = None
        self.geschikte_cameras = []
        
        # Maak notebook (tabbladen)
        self.notebook = ttk.Notebook(root)
        self.notebook.pack(fill='both', expand=True, padx=10, pady=10)
        
        # Maak tabbladen
        self.maak_tab_sensorresolutie()
        self.maak_tab_sensor_selectie()
        self.maak_tab_optiek_berekening()
        self.maak_tab_resultaten()
        
        # Status bar
        self.status_var = tk.StringVar()
        self.status_var.set("Klaar om te beginnen...")
        status_bar = ttk.Label(root, textvariable=self.status_var, relief=tk.SUNKEN, anchor=tk.W)
        status_bar.pack(side=tk.BOTTOM, fill=tk.X)
    
    def maak_tab_sensorresolutie(self):
        """Opdracht 1: Tab voor sensorresolutie berekening."""
        tab = ttk.Frame(self.notebook)
        self.notebook.add(tab, text="1. Sensorresolutie")
        
        # Titel
        ttk.Label(tab, text="Berekening van de Sensorresolutie", 
                 font=('Arial', 16, 'bold')).pack(pady=10)
        
        # Frame voor invoer
        input_frame = ttk.LabelFrame(tab, text="Field of View en Kleinste Detail", padding=20)
        input_frame.pack(fill='x', padx=20, pady=10)
        
        # FOV Horizontaal
        ttk.Label(input_frame, text="Field of View Horizontaal (mm):").grid(row=0, column=0, sticky='w', pady=5)
        self.fov_h_var = tk.StringVar(value="100")
        ttk.Entry(input_frame, textvariable=self.fov_h_var, width=15).grid(row=0, column=1, pady=5, padx=10)
        
        # FOV Verticaal
        ttk.Label(input_frame, text="Field of View Verticaal (mm):").grid(row=1, column=0, sticky='w', pady=5)
        self.fov_v_var = tk.StringVar(value="80")
        ttk.Entry(input_frame, textvariable=self.fov_v_var, width=15).grid(row=1, column=1, pady=5, padx=10)
        
        # Detail Horizontaal
        ttk.Label(input_frame, text="Kleinste Detail Horizontaal (mm):").grid(row=2, column=0, sticky='w', pady=5)
        self.detail_h_var = tk.StringVar(value="0.1")
        ttk.Entry(input_frame, textvariable=self.detail_h_var, width=15).grid(row=2, column=1, pady=5, padx=10)
        
        # Detail Verticaal
        ttk.Label(input_frame, text="Kleinste Detail Verticaal (mm):").grid(row=3, column=0, sticky='w', pady=5)
        self.detail_v_var = tk.StringVar(value="0.1")
        ttk.Entry(input_frame, textvariable=self.detail_v_var, width=15).grid(row=3, column=1, pady=5, padx=10)
        
        # Bereken knop
        ttk.Button(input_frame, text="Bereken Resolutie", 
                  command=self.bereken_sensorresolutie).grid(row=4, column=0, columnspan=2, pady=15)
        
        # Resultaten frame
        result_frame = ttk.LabelFrame(tab, text="Resultaten", padding=20)
        result_frame.pack(fill='both', expand=True, padx=20, pady=10)
        
        self.res_text = scrolledtext.ScrolledText(result_frame, height=10, width=70, font=('Courier', 10))
        self.res_text.pack(fill='both', expand=True)
        
        # Volgende stap knop
        ttk.Button(tab, text="Ga naar Sensor Selectie →", 
                  command=lambda: self.notebook.select(1)).pack(pady=10)
    
    def maak_tab_sensor_selectie(self):
        """Opdracht 2 & 2a: Tab voor sensor selectie."""
        tab = ttk.Frame(self.notebook)
        self.notebook.add(tab, text="2. Sensor Selectie")
        
        # Titel
        ttk.Label(tab, text="Selectie van een Sensor", 
                 font=('Arial', 16, 'bold')).pack(pady=10)
        
        # Knop om geschikte cameras te zoeken
        ttk.Button(tab, text="Zoek Geschikte Camera's", 
                  command=self.zoek_geschikte_cameras).pack(pady=10)
        
        # Listbox met camera's
        list_frame = ttk.LabelFrame(tab, text="Beschikbare Camera's", padding=10)
        list_frame.pack(fill='both', expand=True, padx=20, pady=10)
        
        # Scrollbar en listbox
        scrollbar = ttk.Scrollbar(list_frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        self.camera_listbox = tk.Listbox(list_frame, yscrollcommand=scrollbar.set, 
                                         font=('Courier', 9), height=10)
        self.camera_listbox.pack(side=tk.LEFT, fill='both', expand=True)
        scrollbar.config(command=self.camera_listbox.yview)
        
        self.camera_listbox.bind('<<ListboxSelect>>', self.toon_camera_details)
        
        # Camera details
        detail_frame = ttk.LabelFrame(tab, text="Camera Details & Efficiëntie", padding=10)
        detail_frame.pack(fill='x', padx=20, pady=10)
        
        self.camera_detail_text = tk.Text(detail_frame, height=6, width=70, font=('Courier', 9))
        self.camera_detail_text.pack(fill='x')
        
        # Selecteer camera knop
        ttk.Button(tab, text="Selecteer Deze Camera", 
                  command=self.selecteer_camera).pack(pady=10)
        
        # Volgende stap knop
        ttk.Button(tab, text="Ga naar Optiek Berekening →", 
                  command=lambda: self.notebook.select(2)).pack(pady=5)
    
    def maak_tab_optiek_berekening(self):
        """Opdracht 3, 4 & 5: Tab voor optiek berekeningen."""
        tab = ttk.Frame(self.notebook)
        self.notebook.add(tab, text="3. Optiek Berekening")
        
        # Titel
        ttk.Label(tab, text="Optische Berekeningen", 
                 font=('Arial', 16, 'bold')).pack(pady=10)
        
        # Keuze methode
        method_frame = ttk.LabelFrame(tab, text="Berekeningsmethode", padding=15)
        method_frame.pack(fill='x', padx=20, pady=10)
        
        self.methode_var = tk.StringVar(value="lens")
        ttk.Radiobutton(method_frame, text="Berekening op basis van gekozen lens", 
                       variable=self.methode_var, value="lens",
                       command=self.wissel_methode).pack(anchor='w', pady=5)
        ttk.Radiobutton(method_frame, text="Berekening op basis van voorwerpsafstand", 
                       variable=self.methode_var, value="afstand",
                       command=self.wissel_methode).pack(anchor='w', pady=5)
        
        # Frame voor lens-gebaseerde berekening
        self.lens_frame = ttk.LabelFrame(tab, text="Lens Selectie", padding=15)
        self.lens_frame.pack(fill='x', padx=20, pady=10)
        
        ttk.Label(self.lens_frame, text="Selecteer een lens:").pack(anchor='w', pady=5)
        self.lens_combo = ttk.Combobox(self.lens_frame, state='readonly', width=40)
        lens_namen = [f"{lens['naam']} (f={lens['brandpuntsafstand']}mm, F{lens['max_aperture']})" 
                      for lens in LENZEN]
        self.lens_combo['values'] = lens_namen
        self.lens_combo.pack(fill='x', pady=5)
        self.lens_combo.current(0)
        
        ttk.Button(self.lens_frame, text="Bereken met Gekozen Lens", 
                  command=self.bereken_lens_gebaseerd).pack(pady=10)
        
        # Frame voor afstand-gebaseerde berekening
        self.afstand_frame = ttk.LabelFrame(tab, text="Voorwerpsafstand", padding=15)
        
        ttk.Label(self.afstand_frame, text="Voorwerpsafstand (mm):").pack(anchor='w', pady=5)
        self.voorwerpsafstand_var = tk.StringVar(value="300")
        ttk.Entry(self.afstand_frame, textvariable=self.voorwerpsafstand_var, width=15).pack(anchor='w', pady=5)
        
        ttk.Button(self.afstand_frame, text="Bereken Benodigde Lens", 
                  command=self.bereken_afstand_gebaseerd).pack(pady=10)
        
        # Resultaten van optiek berekening
        optiek_result_frame = ttk.LabelFrame(tab, text="Berekende Specificaties", padding=10)
        optiek_result_frame.pack(fill='both', expand=True, padx=20, pady=10)
        
        self.optiek_text = scrolledtext.ScrolledText(optiek_result_frame, height=12, width=70, font=('Courier', 9))
        self.optiek_text.pack(fill='both', expand=True)
        
        # Volgende stap knop
        ttk.Button(tab, text="Ga naar Resultaten →", 
                  command=lambda: self.notebook.select(3)).pack(pady=10)
    
    def maak_tab_resultaten(self):
        """Opdracht 6, 7 & 8: Tab voor complete resultaten en export."""
        tab = ttk.Frame(self.notebook)
        self.notebook.add(tab, text="4. Resultaten")
        
        # Titel
        ttk.Label(tab, text="Complete Samenvatting", 
                 font=('Arial', 16, 'bold')).pack(pady=10)
        
        # Knoppen frame
        button_frame = ttk.Frame(tab)
        button_frame.pack(fill='x', padx=20, pady=10)
        
        ttk.Button(button_frame, text="🔄 Toon Complete Samenvatting", 
                  command=self.toon_samenvatting).pack(side=tk.LEFT, padx=5)
        ttk.Button(button_frame, text="💾 Opslaan als JSON", 
                  command=self.opslaan_als_json).pack(side=tk.LEFT, padx=5)
        ttk.Button(button_frame, text="📋 Kopieer naar Clipboard", 
                  command=self.kopieer_naar_clipboard).pack(side=tk.LEFT, padx=5)
        
        # Resultaten tekstgebied
        result_frame = ttk.LabelFrame(tab, text="Volledige Resultaten", padding=10)
        result_frame.pack(fill='both', expand=True, padx=20, pady=10)
        
        self.samenvatting_text = scrolledtext.ScrolledText(result_frame, height=20, width=80, font=('Courier', 9))
        self.samenvatting_text.pack(fill='both', expand=True)
    
    def wissel_methode(self):
        """Wissel tussen lens- en afstand-gebaseerde berekening."""
        if self.methode_var.get() == "lens":
            self.lens_frame.pack(fill='x', padx=20, pady=10)
            self.afstand_frame.pack_forget()
        else:
            self.afstand_frame.pack(fill='x', padx=20, pady=10)
            self.lens_frame.pack_forget()
    
    def bereken_sensorresolutie(self):
        """Bereken de benodigde sensorresolutie."""
        try:
            fov_h = float(self.fov_h_var.get())
            fov_v = float(self.fov_v_var.get())
            detail_h = float(self.detail_h_var.get())
            detail_v = float(self.detail_v_var.get())
            
            if fov_h <= 0 or fov_v <= 0 or detail_h <= 0 or detail_v <= 0:
                messagebox.showerror("Fout", "Alle waarden moeten groter dan 0 zijn!")
                return
            
            # Bereken pixels per mm
            pixels_per_mm_h = 1 / detail_h
            pixels_per_mm_v = 1 / detail_v
            
            # Bereken benodigde resolutie
            benodigde_res_h = fov_h * pixels_per_mm_h
            benodigde_res_v = fov_v * pixels_per_mm_v
            
            # Sla resultaten op
            self.alle_resultaten["sensorresolutie"] = {
                "fov_horizontaal_mm": fov_h,
                "fov_verticaal_mm": fov_v,
                "kleinste_detail_h_mm": detail_h,
                "kleinste_detail_v_mm": detail_v,
                "pixels_per_mm_h": pixels_per_mm_h,
                "pixels_per_mm_v": pixels_per_mm_v,
                "benodigde_resolutie_h": benodigde_res_h,
                "benodigde_resolutie_v": benodigde_res_v
            }
            
            # Toon resultaten
            resultaat_text = f"""
╔════════════════════════════════════════════════════════════╗
║                    BEREKENDE RESULTATEN                    ║
╚════════════════════════════════════════════════════════════╝

Field of View:
  • Horizontaal:  {fov_h:.2f} mm
  • Verticaal:    {fov_v:.2f} mm

Kleinste Detail:
  • Horizontaal:  {detail_h:.3f} mm
  • Verticaal:    {detail_v:.3f} mm

Pixels per mm:
  • Horizontaal:  {pixels_per_mm_h:.2f} px/mm
  • Verticaal:    {pixels_per_mm_v:.2f} px/mm

Benodigde Sensorresolutie:
  • {benodigde_res_h:.0f} x {benodigde_res_v:.0f} pixels
  • Totaal:       {benodigde_res_h * benodigde_res_v / 1_000_000:.2f} Megapixels

✅ Berekening succesvol! Ga naar de volgende tab.
"""
            
            self.res_text.delete(1.0, tk.END)
            self.res_text.insert(1.0, resultaat_text)
            
            self.status_var.set("Sensorresolutie berekend. Ga naar Sensor Selectie.")
            messagebox.showinfo("Succes", "Sensorresolutie succesvol berekend!")
            
        except ValueError:
            messagebox.showerror("Fout", "Voer geldige numerieke waarden in!")
    
    def zoek_geschikte_cameras(self):
        """Zoek geschikte camera's op basis van berekende resolutie."""
        if "sensorresolutie" not in self.alle_resultaten:
            messagebox.showwarning("Waarschuwing", "Bereken eerst de sensorresolutie in tab 1!")
            return
        
        res = self.alle_resultaten["sensorresolutie"]
        benodigde_res_h = res["benodigde_resolutie_h"]
        benodigde_res_v = res["benodigde_resolutie_v"]
        
        # Filter geschikte camera's (met 10% marge voor randvervorming)
        marge_factor = 1.1
        self.geschikte_cameras = []
        
        for camera in CAMERAS:
            if (camera["resolutie_h"] >= benodigde_res_h * marge_factor and
                camera["resolutie_v"] >= benodigde_res_v * marge_factor):
                
                # Bereken efficiëntie
                gebruikte_pixels_h = benodigde_res_h / camera["resolutie_h"]
                gebruikte_pixels_v = benodigde_res_v / camera["resolutie_v"]
                efficientie = min(gebruikte_pixels_h, gebruikte_pixels_v) * 100
                
                self.geschikte_cameras.append({
                    "camera": camera,
                    "efficientie": efficientie
                })
        
        if not self.geschikte_cameras:
            messagebox.showerror("Geen resultaten", 
                               "Geen geschikte camera's gevonden!\n\n" +
                               "Probeer een groter kleinste detail of kleiner FOV.")
            return
        
        # Sorteer op efficiëntie
        self.geschikte_cameras.sort(key=lambda x: x["efficientie"], reverse=True)
        
        # Vul listbox
        self.camera_listbox.delete(0, tk.END)
        for item in self.geschikte_cameras:
            cam = item["camera"]
            eff = item["efficientie"]
            text = f"{cam['naam']:30s} {cam['resolutie_h']}x{cam['resolutie_v']:4d} px  Eff: {eff:5.1f}%"
            self.camera_listbox.insert(tk.END, text)
        
        self.status_var.set(f"{len(self.geschikte_cameras)} geschikte camera's gevonden.")
        messagebox.showinfo("Succes", f"✅ {len(self.geschikte_cameras)} geschikte camera's gevonden!")
    
    def toon_camera_details(self, event):
        """Toon details van geselecteerde camera."""
        selection = self.camera_listbox.curselection()
        if not selection:
            return
        
        idx = selection[0]
        item = self.geschikte_cameras[idx]
        cam = item["camera"]
        eff = item["efficientie"]
        
        details = f"""
Camera:      {cam['naam']}
Resolutie:   {cam['resolutie_h']} x {cam['resolutie_v']} pixels
Sensor:      {cam['sensor_breedte']:.2f} x {cam['sensor_hoogte']:.2f} mm
Pixel size:  {cam['sensor_breedte']/cam['resolutie_h']:.3f} x {cam['sensor_hoogte']/cam['resolutie_v']:.3f} µm
Efficiëntie: {eff:.1f}%
"""
        
        self.camera_detail_text.delete(1.0, tk.END)
        self.camera_detail_text.insert(1.0, details)
    
    def selecteer_camera(self):
        """Selecteer de huidige camera."""
        selection = self.camera_listbox.curselection()
        if not selection:
            messagebox.showwarning("Waarschuwing", "Selecteer eerst een camera!")
            return
        
        idx = selection[0]
        item = self.geschikte_cameras[idx]
        self.gekozen_camera = item["camera"]
        
        # Sla op in resultaten
        self.alle_resultaten["sensor"] = {
            "camera": self.gekozen_camera,
            "efficientie": item["efficientie"]
        }
        
        messagebox.showinfo("Succes", 
                          f"✅ Camera geselecteerd:\n{self.gekozen_camera['naam']}\n\n" +
                          f"Ga naar tab 3 voor optiek berekeningen.")
        self.status_var.set(f"Camera geselecteerd: {self.gekozen_camera['naam']}")
    
    def bereken_lens_gebaseerd(self):
        """Berekening op basis van gekozen lens."""
        if self.gekozen_camera is None:
            messagebox.showwarning("Waarschuwing", "Selecteer eerst een camera in tab 2!")
            return
        
        if "sensorresolutie" not in self.alle_resultaten:
            messagebox.showwarning("Waarschuwing", "Bereken eerst de sensorresolutie in tab 1!")
            return
        
        # Haal gekozen lens op
        idx = self.lens_combo.current()
        gekozen_lens = LENZEN[idx]
        
        camera = self.gekozen_camera
        res = self.alle_resultaten["sensorresolutie"]
        fov_h = res["fov_horizontaal_mm"]
        fov_v = res["fov_verticaal_mm"]
        
        f = gekozen_lens["brandpuntsafstand"]
        v = camera["flange_focal_distance"]
        
        # Bereken vergroting
        M_h = camera["sensor_breedte"] / fov_h
        M_v = camera["sensor_hoogte"] / fov_v
        M = min(M_h, M_v)
        
        # Bereken voorwerpsafstand
        u = v / M
        
        # Sla resultaten op
        self.alle_resultaten["optiek"] = {
            "lens": gekozen_lens,
            "brandpuntsafstand_mm": f,
            "voorwerpsafstand_mm": u,
            "beeldafstand_mm": v,
            "vergroting": M,
            "werkelijke_fov_h": camera["sensor_breedte"] / M,
            "werkelijke_fov_v": camera["sensor_hoogte"] / M
        }
        self.alle_resultaten["berekeningsmethode"] = "Lens-gebaseerd"
        
        # Toon resultaten
        resultaat = f"""
╔════════════════════════════════════════════════════════════╗
║           BEREKENING OP BASIS VAN GEKOZEN LENS             ║
╚════════════════════════════════════════════════════════════╝

Gekozen Lens:
  • Model:            {gekozen_lens['naam']}
  • Brandpuntsafstand: {f} mm
  • Max Aperture:     F{gekozen_lens['max_aperture']}

Berekende Waarden:
  • Voorwerpsafstand:  {u:.2f} mm ({u/10:.2f} cm)
  • Beeldafstand:      {v:.2f} mm
  • Vergroting:        {M:.4f}x

Werkelijk Field of View:
  • {self.alle_resultaten['optiek']['werkelijke_fov_h']:.2f} x {self.alle_resultaten['optiek']['werkelijke_fov_v']:.2f} mm

✅ Berekening voltooid! Bekijk resultaten in tab 4.
"""
        
        self.optiek_text.delete(1.0, tk.END)
        self.optiek_text.insert(1.0, resultaat)
        
        self.status_var.set(f"Optiek berekend met {gekozen_lens['naam']}")
        messagebox.showinfo("Succes", "✅ Optische berekening voltooid!")
    
    def bereken_afstand_gebaseerd(self):
        """Berekening op basis van voorwerpsafstand."""
        if self.gekozen_camera is None:
            messagebox.showwarning("Waarschuwing", "Selecteer eerst een camera in tab 2!")
            return
        
        if "sensorresolutie" not in self.alle_resultaten:
            messagebox.showwarning("Waarschuwing", "Bereken eerst de sensorresolutie in tab 1!")
            return
        
        try:
            u = float(self.voorwerpsafstand_var.get())
            if u <= 0:
                messagebox.showerror("Fout", "Voorwerpsafstand moet groter dan 0 zijn!")
                return
        except ValueError:
            messagebox.showerror("Fout", "Voer een geldige voorwerpsafstand in!")
            return
        
        camera = self.gekozen_camera
        res = self.alle_resultaten["sensorresolutie"]
        fov_h = res["fov_horizontaal_mm"]
        fov_v = res["fov_verticaal_mm"]
        
        v = camera["flange_focal_distance"]
        
        # Bereken benodigde brandpuntsafstand
        f = 1 / (1/u + 1/v)
        
        # Bereken vergroting
        M = v / u
        
        # Bereken werkelijk FOV
        werkelijk_fov_h = camera["sensor_breedte"] / M
        werkelijk_fov_v = camera["sensor_hoogte"] / M
        
        # Zoek beste lens
        geschikte_lenzen = []
        for lens in LENZEN:
            verschil = abs(lens["brandpuntsafstand"] - f)
            percentage = (verschil / f) * 100
            geschikte_lenzen.append({
                "lens": lens,
                "verschil_mm": verschil,
                "verschil_percentage": percentage
            })
        
        geschikte_lenzen.sort(key=lambda x: x["verschil_mm"])
        beste_lens = geschikte_lenzen[0]["lens"]
        
        # Sla resultaten op
        self.alle_resultaten["optiek"] = {
            "lens": beste_lens,
            "berekende_brandpuntsafstand_mm": f,
            "werkelijke_brandpuntsafstand_mm": beste_lens["brandpuntsafstand"],
            "voorwerpsafstand_mm": u,
            "beeldafstand_mm": v,
            "vergroting": M,
            "werkelijke_fov_h": werkelijk_fov_h,
            "werkelijke_fov_v": werkelijk_fov_v
        }
        self.alle_resultaten["berekeningsmethode"] = "Afstand-gebaseerd"
        
        # Toon resultaten
        resultaat = f"""
╔════════════════════════════════════════════════════════════╗
║        BEREKENING OP BASIS VAN VOORWERPSAFSTAND            ║
╚════════════════════════════════════════════════════════════╝

Gegeven:
  • Voorwerpsafstand:  {u:.2f} mm ({u/10:.2f} cm)

Berekende Waarden:
  • Benodigde brandpuntsafstand: {f:.2f} mm
  • Beeldafstand:                {v:.2f} mm
  • Vergroting:                  {M:.4f}x
  • Werkelijk FOV:               {werkelijk_fov_h:.2f} x {werkelijk_fov_v:.2f} mm

Aanbevolen Lenzen:
"""
        
        for i, item in enumerate(geschikte_lenzen[:3], 1):
            lens = item["lens"]
            resultaat += f"\n  {i}. {lens['naam']}"
            resultaat += f"\n     f={lens['brandpuntsafstand']}mm (verschil: {item['verschil_mm']:.2f}mm, {item['verschil_percentage']:.1f}%)\n"
        
        resultaat += f"\n✅ Beste match: {beste_lens['naam']} (f={beste_lens['brandpuntsafstand']}mm)"
        resultaat += "\n\n✅ Berekening voltooid! Bekijk resultaten in tab 4."
        
        self.optiek_text.delete(1.0, tk.END)
        self.optiek_text.insert(1.0, resultaat)
        
        self.status_var.set(f"Optiek berekend met voorwerpsafstand {u:.2f}mm")
        messagebox.showinfo("Succes", "✅ Optische berekening voltooid!")
    
    def toon_samenvatting(self):
        """Toon complete samenvatting van alle berekeningen."""
        if not self.alle_resultaten:
            messagebox.showwarning("Waarschuwing", "Voer eerst berekeningen uit!")
            return
        
        samenvatting = """
╔════════════════════════════════════════════════════════════╗
║          COMPLETE SAMENVATTING VAN ALLE BEREKENINGEN       ║
╚════════════════════════════════════════════════════════════╝

"""
        
        # Sensorresolutie
        if "sensorresolutie" in self.alle_resultaten:
            res = self.alle_resultaten["sensorresolutie"]
            samenvatting += f"""
┌─ FIELD OF VIEW EN RESOLUTIE ────────────────────────────────┐
│                                                              │
│  FOV:                 {res['fov_horizontaal_mm']:.2f} x {res['fov_verticaal_mm']:.2f} mm
│  Kleinste detail:     {res['kleinste_detail_h_mm']:.3f} x {res['kleinste_detail_v_mm']:.3f} mm
│  Pixels per mm:       {res['pixels_per_mm_h']:.2f} x {res['pixels_per_mm_v']:.2f} px/mm
│  Benodigde resolutie: {res['benodigde_resolutie_h']:.0f} x {res['benodigde_resolutie_v']:.0f} pixels
│                                                              │
└──────────────────────────────────────────────────────────────┘
"""
        
        # Sensor
        if "sensor" in self.alle_resultaten:
            sens = self.alle_resultaten["sensor"]
            cam = sens["camera"]
            samenvatting += f"""
┌─ GEKOZEN CAMERA ─────────────────────────────────────────────┐
│                                                              │
│  Model:       {cam['naam']:48s} │
│  Resolutie:   {cam['resolutie_h']} x {cam['resolutie_v']} pixels
│  Sensor:      {cam['sensor_breedte']:.2f} x {cam['sensor_hoogte']:.2f} mm
│  Efficiëntie: {sens['efficientie']:.1f}%
│                                                              │
└──────────────────────────────────────────────────────────────┘
"""
        
        # Optiek
        if "optiek" in self.alle_resultaten:
            opt = self.alle_resultaten["optiek"]
            lens = opt["lens"]
            samenvatting += f"""
┌─ GEKOZEN LENS ───────────────────────────────────────────────┐
│                                                              │
│  Model:              {lens['naam']:42s} │
│  Brandpuntsafstand:  {lens['brandpuntsafstand']} mm
│  Max aperture:       F{lens['max_aperture']}
│                                                              │
└──────────────────────────────────────────────────────────────┘

┌─ OPTISCHE BEREKENINGEN ──────────────────────────────────────┐
│                                                              │
│  Berekeningsmethode:  {self.alle_resultaten.get('berekeningsmethode', 'N/A'):42s} │
"""
            if "voorwerpsafstand_mm" in opt:
                samenvatting += f"│  Voorwerpsafstand:    {opt['voorwerpsafstand_mm']:.2f} mm ({opt['voorwerpsafstand_mm']/10:.2f} cm)\n"
            if "beeldafstand_mm" in opt:
                samenvatting += f"│  Beeldafstand:        {opt['beeldafstand_mm']:.2f} mm\n"
            if "vergroting" in opt:
                samenvatting += f"│  Vergroting:          {opt['vergroting']:.4f}x\n"
            if "werkelijke_fov_h" in opt:
                samenvatting += f"│  Werkelijk FOV:       {opt['werkelijke_fov_h']:.2f} x {opt['werkelijke_fov_v']:.2f} mm\n"
            
            samenvatting += "│                                                              │\n"
            samenvatting += "└──────────────────────────────────────────────────────────────┘\n"
        
        samenvatting += "\n" + "="*62 + "\n"
        
        self.samenvatting_text.delete(1.0, tk.END)
        self.samenvatting_text.insert(1.0, samenvatting)
        
        self.status_var.set("Complete samenvatting weergegeven.")
    
    def opslaan_als_json(self):
        """Sla resultaten op als JSON bestand."""
        if not self.alle_resultaten:
            messagebox.showwarning("Waarschuwing", "Geen resultaten om op te slaan!")
            return
        
        filename = filedialog.asksaveasfilename(
            defaultextension=".json",
            filetypes=[("JSON files", "*.json"), ("All files", "*.*")],
            initialfile="optica_berekeningen.json"
        )
        
        if not filename:
            return
        
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(self.alle_resultaten, f, indent=4, ensure_ascii=False)
            
            messagebox.showinfo("Succes", 
                              f"✅ Resultaten opgeslagen!\n\n{filename}\n\n" +
                              f"Bestandsgrootte: {os.path.getsize(filename)} bytes")
            self.status_var.set(f"Resultaten opgeslagen: {os.path.basename(filename)}")
        except Exception as e:
            messagebox.showerror("Fout", f"Kon bestand niet opslaan:\n{e}")
    
    def kopieer_naar_clipboard(self):
        """Kopieer samenvatting naar clipboard."""
        tekst = self.samenvatting_text.get(1.0, tk.END)
        self.root.clipboard_clear()
        self.root.clipboard_append(tekst)
        messagebox.showinfo("Succes", "✅ Samenvatting gekopieerd naar clipboard!")
        self.status_var.set("Samenvatting gekopieerd naar clipboard.")


def main():
    """Start de GUI applicatie."""
    root = tk.Tk()
    app = OpticaRekenToolGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()
