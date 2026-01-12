"""
Optica Rekentool
Een complete tool voor optica-gerelateerde berekeningen voor camerasystemen.
"""

import json
import os
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


def vraag_getal(prompt: str, minimum: float = None, maximum: float = None) -> float:
    """
    Vraag de gebruiker om een getal met validatie.
    
    Args:
        prompt: De tekst die aan de gebruiker wordt getoond
        minimum: Optionele minimumwaarde
        maximum: Optionele maximumwaarde
    
    Returns:
        Het ingevoerde getal
    """
    while True:
        try:
            waarde = float(input(prompt))
            if minimum is not None and waarde < minimum:
                print(f"❌ Waarde moet minimaal {minimum} zijn.")
                continue
            if maximum is not None and waarde > maximum:
                print(f"❌ Waarde mag maximaal {maximum} zijn.")
                continue
            return waarde
        except ValueError:
            print("❌ Ongeldige invoer. Voer een getal in.")


def vraag_keuze(prompt: str, opties: List[str]) -> int:
    """
    Vraag de gebruiker om een keuze uit een lijst.
    
    Args:
        prompt: De tekst die aan de gebruiker wordt getoond
        opties: Lijst met keuzemogelijkheden
    
    Returns:
        Index van de gekozen optie
    """
    print(f"\n{prompt}")
    for i, optie in enumerate(opties, 1):
        print(f"{i}. {optie}")
    
    while True:
        try:
            keuze = int(input("\nKies een optie: "))
            if 1 <= keuze <= len(opties):
                return keuze - 1
            else:
                print(f"❌ Kies een nummer tussen 1 en {len(opties)}.")
        except ValueError:
            print("❌ Ongeldige invoer. Voer een nummer in.")


def bereken_sensorresolutie() -> Dict:
    """
    Opdracht 1: Bereken de benodigde sensorresolutie.
    
    Returns:
        Dictionary met berekeningsresultaten
    """
    print("\n" + "="*60)
    print("OPDRACHT 1: BEREKENING VAN DE SENSORRESOLUTIE")
    print("="*60)
    
    # Vraag field of view
    fov_h = vraag_getal("Field of view horizontaal (mm): ", minimum=0.1)
    fov_v = vraag_getal("Field of view verticaal (mm): ", minimum=0.1)
    
    # Vraag kleinste detail
    detail_h = vraag_getal("Kleinste detail horizontaal (mm): ", minimum=0.001)
    detail_v = vraag_getal("Kleinste detail verticaal (mm): ", minimum=0.001)
    
    # Bereken pixels per mm
    pixels_per_mm_h = 1 / detail_h
    pixels_per_mm_v = 1 / detail_v
    
    # Bereken benodigde resolutie
    benodigde_res_h = fov_h * pixels_per_mm_h
    benodigde_res_v = fov_v * pixels_per_mm_v
    
    resultaten = {
        "fov_horizontaal_mm": fov_h,
        "fov_verticaal_mm": fov_v,
        "kleinste_detail_h_mm": detail_h,
        "kleinste_detail_v_mm": detail_v,
        "pixels_per_mm_h": pixels_per_mm_h,
        "pixels_per_mm_v": pixels_per_mm_v,
        "benodigde_resolutie_h": benodigde_res_h,
        "benodigde_resolutie_v": benodigde_res_v
    }
    
    print("\n📊 RESULTATEN:")
    print(f"  Pixels per mm (horizontaal): {pixels_per_mm_h:.2f} px/mm")
    print(f"  Pixels per mm (verticaal):   {pixels_per_mm_v:.2f} px/mm")
    print(f"  Benodigde resolutie:         {benodigde_res_h:.0f} x {benodigde_res_v:.0f} pixels")
    
    return resultaten


def selecteer_sensor(resultaten: Dict) -> Dict:
    """
    Opdracht 2 & 2a: Selecteer een geschikte sensor en bereken efficiëntie.
    
    Args:
        resultaten: Dictionary met resultaten van opdracht 1
    
    Returns:
        Dictionary met geselecteerde camera en efficiëntie
    """
    print("\n" + "="*60)
    print("OPDRACHT 2: SELECTIE VAN EEN SENSOR")
    print("="*60)
    
    benodigde_res_h = resultaten["benodigde_resolutie_h"]
    benodigde_res_v = resultaten["benodigde_resolutie_v"]
    fov_h = resultaten["fov_horizontaal_mm"]
    fov_v = resultaten["fov_verticaal_mm"]
    
    # Filter geschikte camera's (met 10% marge voor randvervorming)
    marge_factor = 1.1
    geschikte_cameras = []
    
    for camera in CAMERAS:
        if (camera["resolutie_h"] >= benodigde_res_h * marge_factor and
            camera["resolutie_v"] >= benodigde_res_v * marge_factor):
            
            # Bereken efficiëntie (percentage van sensor dat gebruikt wordt)
            gebruikte_pixels_h = benodigde_res_h / camera["resolutie_h"]
            gebruikte_pixels_v = benodigde_res_v / camera["resolutie_v"]
            efficientie = min(gebruikte_pixels_h, gebruikte_pixels_v) * 100
            
            geschikte_cameras.append({
                "camera": camera,
                "efficientie": efficientie
            })
    
    if not geschikte_cameras:
        print("❌ Geen geschikte camera gevonden!")
        print("💡 Probeer een groter kleinste detail of een kleiner field of view.")
        return None
    
    # Sorteer op efficiëntie (hoogste eerst)
    geschikte_cameras.sort(key=lambda x: x["efficientie"], reverse=True)
    
    print("\n✅ GESCHIKTE CAMERA'S (gesorteerd op efficiëntie):")
    print("-" * 80)
    for i, item in enumerate(geschikte_cameras, 1):
        cam = item["camera"]
        eff = item["efficientie"]
        print(f"{i}. {cam['naam']}")
        print(f"   Resolutie: {cam['resolutie_h']} x {cam['resolutie_v']} pixels")
        print(f"   Sensor:    {cam['sensor_breedte']:.2f} x {cam['sensor_hoogte']:.2f} mm")
        print(f"   Efficiëntie: {eff:.1f}%")
        print()
    
    # Laat gebruiker kiezen
    camera_namen = [f"{item['camera']['naam']} (efficiëntie: {item['efficientie']:.1f}%)" 
                    for item in geschikte_cameras]
    keuze = vraag_keuze("Selecteer een camera:", camera_namen)
    
    gekozen_camera = geschikte_cameras[keuze]["camera"]
    efficientie = geschikte_cameras[keuze]["efficientie"]
    
    # Bereken werkelijke FOV op de sensor
    pixels_per_mm_h = gekozen_camera["resolutie_h"] / gekozen_camera["sensor_breedte"]
    pixels_per_mm_v = gekozen_camera["resolutie_v"] / gekozen_camera["sensor_hoogte"]
    
    # Bereken benodigde sensor afmetingen voor het FOV
    benodigde_sensor_h = fov_h / fov_h * gekozen_camera["sensor_breedte"]
    benodigde_sensor_v = fov_v / fov_v * gekozen_camera["sensor_hoogte"]
    
    print(f"\n✅ Gekozen camera: {gekozen_camera['naam']}")
    print(f"   Sensor efficiëntie: {efficientie:.1f}%")
    
    return {
        "camera": gekozen_camera,
        "efficientie": efficientie,
        "pixels_per_mm_h": pixels_per_mm_h,
        "pixels_per_mm_v": pixels_per_mm_v
    }


def bereken_lens_gebaseerd(camera: Dict, fov_h: float, fov_v: float) -> Dict:
    """
    Opdracht 4: Berekening op basis van gekozen lens.
    
    Args:
        camera: Gekozen camera dictionary
        fov_h: Field of view horizontaal (mm)
        fov_v: Field of view verticaal (mm)
    
    Returns:
        Dictionary met berekeningsresultaten
    """
    print("\n" + "="*60)
    print("OPDRACHT 4: BEREKENING OP BASIS VAN GEKOZEN LENS")
    print("="*60)
    
    # Toon beschikbare lenzen
    lens_namen = [f"{lens['naam']} (f={lens['brandpuntsafstand']}mm, F{lens['max_aperture']})" 
                  for lens in LENZEN]
    keuze = vraag_keuze("Selecteer een lens:", lens_namen)
    gekozen_lens = LENZEN[keuze]
    
    f = gekozen_lens["brandpuntsafstand"]  # brandpuntsafstand
    
    # Bereken beeldafstand (image distance)
    # Voor de sensor is de beeldafstand de flange focal distance
    v = camera["flange_focal_distance"]  # beeldafstand (mm)
    
    # Gebruik de lensformule: 1/f = 1/u + 1/v
    # waarbij u = voorwerpsafstand, v = beeldafstand, f = brandpuntsafstand
    # Dus: 1/u = 1/f - 1/v
    # u = 1 / (1/f - 1/v)
    
    if f >= v:
        print("⚠️  Waarschuwing: Deze lens configuratie werkt niet goed voor deze camera.")
        print("    De brandpuntsafstand moet kleiner zijn dan de flange focal distance.")
    
    # Bereken vergroting (magnification)
    # M = v / u = sensor_size / object_size
    M_h = camera["sensor_breedte"] / fov_h
    M_v = camera["sensor_hoogte"] / fov_v
    M = min(M_h, M_v)  # Gebruik kleinste om binnen FOV te blijven
    
    # Uit M = v/u volgt: u = v/M
    u = v / M  # voorwerpsafstand
    
    # Verificatie met lensformule
    f_check = 1 / (1/u + 1/v)
    
    resultaten = {
        "lens": gekozen_lens,
        "brandpuntsafstand_mm": f,
        "voorwerpsafstand_mm": u,
        "beeldafstand_mm": v,
        "vergroting": M,
        "werkelijke_fov_h": camera["sensor_breedte"] / M,
        "werkelijke_fov_v": camera["sensor_hoogte"] / M
    }
    
    print("\n📊 RESULTATEN:")
    print(f"  Gekozen lens: {gekozen_lens['naam']}")
    print(f"  Brandpuntsafstand: {f} mm")
    print(f"  Voorwerpsafstand:  {u:.2f} mm ({u/10:.2f} cm)")
    print(f"  Beeldafstand:      {v:.2f} mm")
    print(f"  Vergroting:        {M:.4f}x")
    print(f"  Werkelijk FOV:     {resultaten['werkelijke_fov_h']:.2f} x {resultaten['werkelijke_fov_v']:.2f} mm")
    
    return resultaten


def bereken_afstand_gebaseerd(camera: Dict, fov_h: float, fov_v: float) -> Dict:
    """
    Opdracht 5: Berekening op basis van vastgestelde voorwerpsafstand.
    
    Args:
        camera: Gekozen camera dictionary
        fov_h: Field of view horizontaal (mm)
        fov_v: Field of view verticaal (mm)
    
    Returns:
        Dictionary met berekeningsresultaten
    """
    print("\n" + "="*60)
    print("OPDRACHT 5: BEREKENING OP BASIS VAN VOORWERPSAFSTAND")
    print("="*60)
    
    # Vraag voorwerpsafstand
    u = vraag_getal("Voorwerpsafstand (mm): ", minimum=10)
    
    # Beeldafstand is flange focal distance
    v = camera["flange_focal_distance"]
    
    # Bereken benodigde brandpuntsafstand met lensformule
    # 1/f = 1/u + 1/v
    f = 1 / (1/u + 1/v)
    
    # Bereken vergroting
    M = v / u
    
    # Bereken werkelijk FOV bij deze configuratie
    werkelijk_fov_h = camera["sensor_breedte"] / M
    werkelijk_fov_v = camera["sensor_hoogte"] / M
    
    # Zoek meest geschikte lens
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
    
    print("\n📊 BEREKENDE SPECIFICATIES:")
    print(f"  Benodigde brandpuntsafstand: {f:.2f} mm")
    print(f"  Voorwerpsafstand:            {u:.2f} mm ({u/10:.2f} cm)")
    print(f"  Beeldafstand:                {v:.2f} mm")
    print(f"  Vergroting:                  {M:.4f}x")
    print(f"  Werkelijk FOV:               {werkelijk_fov_h:.2f} x {werkelijk_fov_v:.2f} mm")
    
    print("\n🔍 AANBEVOLEN LENZEN (gesorteerd op geschiktheid):")
    print("-" * 80)
    for i, item in enumerate(geschikte_lenzen[:5], 1):
        lens = item["lens"]
        print(f"{i}. {lens['naam']}")
        print(f"   Brandpuntsafstand: {lens['brandpuntsafstand']} mm (verschil: {item['verschil_mm']:.2f} mm, {item['verschil_percentage']:.1f}%)")
        print(f"   Max aperture: F{lens['max_aperture']}")
        print()
    
    # Laat gebruiker kiezen
    lens_namen = [f"{item['lens']['naam']} (f={item['lens']['brandpuntsafstand']}mm)" 
                  for item in geschikte_lenzen]
    keuze = vraag_keuze("Selecteer een lens:", lens_namen)
    gekozen_lens = geschikte_lenzen[keuze]["lens"]
    
    # Herbereken met gekozen lens
    f_werkelijk = gekozen_lens["brandpuntsafstand"]
    # Met gekozen lens: herbereken voorwerpsafstand voor gewenst FOV
    M_gewenst = camera["sensor_breedte"] / fov_h
    u_aangepast = v / M_gewenst
    
    resultaten = {
        "lens": gekozen_lens,
        "berekende_brandpuntsafstand_mm": f,
        "werkelijke_brandpuntsafstand_mm": f_werkelijk,
        "voorwerpsafstand_mm": u,
        "aangepaste_voorwerpsafstand_mm": u_aangepast,
        "beeldafstand_mm": v,
        "vergroting": M,
        "werkelijke_fov_h": werkelijk_fov_h,
        "werkelijke_fov_v": werkelijk_fov_v
    }
    
    print(f"\n✅ Gekozen lens: {gekozen_lens['naam']} (f={f_werkelijk}mm)")
    if abs(u - u_aangepast) > 1:
        print(f"💡 Tip: Voor optimaal FOV, pas voorwerpsafstand aan naar {u_aangepast:.2f} mm")
    
    return resultaten


def toon_samenvatting(alle_resultaten: Dict):
    """
    Opdracht 6: Presenteer alle resultaten overzichtelijk.
    
    Args:
        alle_resultaten: Dictionary met alle berekeningsresultaten
    """
    print("\n" + "="*60)
    print("COMPLETE SAMENVATTING VAN ALLE BEREKENINGEN")
    print("="*60)
    
    if "sensorresolutie" in alle_resultaten:
        res = alle_resultaten["sensorresolutie"]
        print("\n📐 FIELD OF VIEW EN RESOLUTIE:")
        print(f"  FOV:                {res['fov_horizontaal_mm']:.2f} x {res['fov_verticaal_mm']:.2f} mm")
        print(f"  Kleinste detail:    {res['kleinste_detail_h_mm']:.3f} x {res['kleinste_detail_v_mm']:.3f} mm")
        print(f"  Pixels per mm:      {res['pixels_per_mm_h']:.2f} x {res['pixels_per_mm_v']:.2f} px/mm")
        print(f"  Benodigde resolutie: {res['benodigde_resolutie_h']:.0f} x {res['benodigde_resolutie_v']:.0f} pixels")
    
    if "sensor" in alle_resultaten:
        sens = alle_resultaten["sensor"]
        cam = sens["camera"]
        print("\n📷 GEKOZEN CAMERA:")
        print(f"  Model:      {cam['naam']}")
        print(f"  Resolutie:  {cam['resolutie_h']} x {cam['resolutie_v']} pixels")
        print(f"  Sensor:     {cam['sensor_breedte']:.2f} x {cam['sensor_hoogte']:.2f} mm")
        print(f"  Efficiëntie: {sens['efficientie']:.1f}%")
    
    if "optiek" in alle_resultaten:
        opt = alle_resultaten["optiek"]
        lens = opt["lens"]
        print("\n🔍 GEKOZEN LENS:")
        print(f"  Model:              {lens['naam']}")
        print(f"  Brandpuntsafstand:  {lens['brandpuntsafstand']} mm")
        print(f"  Max aperture:       F{lens['max_aperture']}")
        
        print("\n📏 OPTISCHE BEREKENINGEN:")
        if "voorwerpsafstand_mm" in opt:
            print(f"  Voorwerpsafstand:   {opt['voorwerpsafstand_mm']:.2f} mm ({opt['voorwerpsafstand_mm']/10:.2f} cm)")
        if "aangepaste_voorwerpsafstand_mm" in opt:
            print(f"  Aangepaste afstand: {opt['aangepaste_voorwerpsafstand_mm']:.2f} mm ({opt['aangepaste_voorwerpsafstand_mm']/10:.2f} cm)")
        if "beeldafstand_mm" in opt:
            print(f"  Beeldafstand:       {opt['beeldafstand_mm']:.2f} mm")
        if "vergroting" in opt:
            print(f"  Vergroting:         {opt['vergroting']:.4f}x")
        if "werkelijke_fov_h" in opt:
            print(f"  Werkelijk FOV:      {opt['werkelijke_fov_h']:.2f} x {opt['werkelijke_fov_v']:.2f} mm")
    
    print("\n" + "="*60)


def sla_op_als_json(alle_resultaten: Dict, bestandsnaam: str = "optica_berekeningen.json"):
    """
    Opdracht 8: Sla resultaten op in JSON-bestand.
    
    Args:
        alle_resultaten: Dictionary met alle berekeningsresultaten
        bestandsnaam: Naam van het JSON-bestand
    """
    print("\n" + "="*60)
    print("RESULTATEN OPSLAAN")
    print("="*60)
    
    # Converteer naar serialiseerbare vorm
    serialiseerbare_resultaten = {}
    
    for key, value in alle_resultaten.items():
        if isinstance(value, dict):
            serialiseerbare_resultaten[key] = value.copy()
        else:
            serialiseerbare_resultaten[key] = value
    
    # Sla op in JSON
    with open(bestandsnaam, 'w', encoding='utf-8') as f:
        json.dump(serialiseerbare_resultaten, f, indent=4, ensure_ascii=False)
    
    # Verkrijg absolute pad
    abs_pad = os.path.abspath(bestandsnaam)
    
    print(f"✅ Resultaten opgeslagen in: {abs_pad}")
    print(f"   Bestandsgrootte: {os.path.getsize(bestandsnaam)} bytes")


def hoofdmenu():
    """
    Hoofdprogramma met menu-structuur.
    """
    print("\n" + "="*60)
    print("  OPTICA REKENTOOL")
    print("  Camera en Lens Berekeningsprogramma")
    print("="*60)
    
    # Opdracht 7: Dictionary om alle resultaten op te slaan
    alle_resultaten = {}
    
    # Opdracht 1: Bereken sensorresolutie
    resultaten_res = bereken_sensorresolutie()
    alle_resultaten["sensorresolutie"] = resultaten_res
    
    # Opdracht 2 & 2a: Selecteer sensor
    resultaten_sensor = selecteer_sensor(resultaten_res)
    if resultaten_sensor is None:
        print("\n❌ Kan niet verder zonder geschikte camera.")
        return
    alle_resultaten["sensor"] = resultaten_sensor
    
    # Opdracht 3: Kies berekeningspaden
    print("\n" + "="*60)
    print("OPDRACHT 3: KIES BEREKENINGSMETHODE")
    print("="*60)
    
    methodes = [
        "Berekening op basis van gekozen lens",
        "Berekening op basis van vastgestelde voorwerpsafstand"
    ]
    keuze_methode = vraag_keuze("Kies een berekeningsmethode:", methodes)
    
    camera = resultaten_sensor["camera"]
    fov_h = resultaten_res["fov_horizontaal_mm"]
    fov_v = resultaten_res["fov_verticaal_mm"]
    
    # Opdracht 4 of 5: Uitvoeren van gekozen methode
    if keuze_methode == 0:
        resultaten_optiek = bereken_lens_gebaseerd(camera, fov_h, fov_v)
    else:
        resultaten_optiek = bereken_afstand_gebaseerd(camera, fov_h, fov_v)
    
    alle_resultaten["optiek"] = resultaten_optiek
    alle_resultaten["berekeningsmethode"] = methodes[keuze_methode]
    
    # Opdracht 6: Toon samenvatting
    toon_samenvatting(alle_resultaten)
    
    # Opdracht 8: Optioneel opslaan als JSON
    print("\n💾 Wilt u de resultaten opslaan?")
    opslaan = input("Opslaan als JSON? (j/n): ").lower().strip()
    
    if opslaan == 'j' or opslaan == 'ja' or opslaan == 'y' or opslaan == 'yes':
        bestandsnaam = input("Bestandsnaam (laat leeg voor standaard): ").strip()
        if not bestandsnaam:
            bestandsnaam = "optica_berekeningen.json"
        elif not bestandsnaam.endswith('.json'):
            bestandsnaam += '.json'
        
        sla_op_als_json(alle_resultaten, bestandsnaam)
    
    print("\n✅ Programma voltooid!")
    print("="*60)


if __name__ == "__main__":
    try:
        hoofdmenu()
    except KeyboardInterrupt:
        print("\n\n⚠️  Programma afgebroken door gebruiker.")
    except Exception as e:
        print(f"\n❌ Er is een fout opgetreden: {e}")
        import traceback
        traceback.print_exc()
