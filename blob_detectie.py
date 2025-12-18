"""
Blob Detectie - Opdrachten 1 t/m 8
Detecteert blobs in afbeeldingen met verschillende methoden
"""

import cv2
import numpy as np
import easygui
from matplotlib import pyplot as plt
from scipy import ndimage


def selecteer_afbeelding():
    """Opdracht 1: Laat gebruiker een afbeelding selecteren"""
    bestandspad = easygui.fileopenbox(
        msg="Selecteer een afbeelding (bijv. pills-in-strip.jpg)",
        title="Afbeelding selecteren",
        filetypes=["*.jpg", "*.jpeg", "*.png", "*.bmp"]
    )
    return bestandspad


def toon_afbeelding(titel, afbeelding):
    """Hulpfunctie om afbeelding te tonen"""
    cv2.imshow(titel, afbeelding)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def opdracht_1_en_2(bestandspad):
    """Opdracht 1 & 2: Afbeelding inlezen en grijswaarden conversie"""
    # Opdracht 1: Afbeelding inlezen
    afbeelding = cv2.imread(bestandspad)
    if afbeelding is None:
        print("Fout: Afbeelding kan niet worden geladen")
        return None, None
    
    print("Opdracht 1: Afbeelding ingelezen")
    toon_afbeelding("Originele afbeelding", afbeelding)
    
    # Opdracht 2: Grijswaarden conversie
    grijswaarden = cv2.cvtColor(afbeelding, cv2.COLOR_BGR2GRAY)
    print("Opdracht 2: Grijswaarden conversie uitgevoerd")
    toon_afbeelding("Grijswaarden afbeelding", grijswaarden)
    
    return afbeelding, grijswaarden


def opdracht_3_simpleblobdetector(afbeelding, grijswaarden):
    """Opdracht 3: Blob detectie met SimpleBlobDetector"""
    print("\n=== Opdracht 3: SimpleBlobDetector ===")
    
    # Setup SimpleBlobDetector parameters
    params = cv2.SimpleBlobDetector_Params()
    
    # Thresholds
    params.minThreshold = 10
    params.maxThreshold = 200
    
    # Filter by Area
    params.filterByArea = True
    params.minArea = 100
    params.maxArea = 5000
    
    # Filter by Circularity
    params.filterByCircularity = True
    params.minCircularity = 0.1
    
    # Filter by Convexity
    params.filterByConvexity = True
    params.minConvexity = 0.5
    
    # Filter by Inertia
    params.filterByInertia = True
    params.minInertiaRatio = 0.01
    
    # Create detector
    detector = cv2.SimpleBlobDetector_create(params)
    
    # Detect blobs
    keypoints = detector.detect(grijswaarden)
    
    print(f"Aantal gedetecteerde blobs: {len(keypoints)}")
    
    # Draw detected blobs
    afbeelding_blobs = cv2.drawKeypoints(
        afbeelding, 
        keypoints, 
        np.array([]), 
        (0, 0, 255),
        cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS
    )
    
    toon_afbeelding("SimpleBlobDetector - Gedetecteerde Blobs", afbeelding_blobs)
    
    return keypoints, afbeelding_blobs


def opdracht_3a_parameters(afbeelding, grijswaarden):
    """Opdracht 3a: Parameterafstemming SimpleBlobDetector"""
    print("\n=== Opdracht 3a: Parameterafstemming ===")
    
    # Verschillende parametersets testen
    parametersets = [
        {
            "naam": "Strenge filters",
            "minThreshold": 50,
            "maxThreshold": 200,
            "minArea": 200,
            "maxArea": 3000,
            "minCircularity": 0.7
        },
        {
            "naam": "Losse filters",
            "minThreshold": 10,
            "maxThreshold": 200,
            "minArea": 50,
            "maxArea": 10000,
            "minCircularity": 0.1
        },
        {
            "naam": "Alleen grote blobs",
            "minThreshold": 10,
            "maxThreshold": 200,
            "minArea": 1000,
            "maxArea": 20000,
            "minCircularity": 0.1
        }
    ]
    
    resultaten = []
    
    for param_set in parametersets:
        params = cv2.SimpleBlobDetector_Params()
        params.minThreshold = param_set["minThreshold"]
        params.maxThreshold = param_set["maxThreshold"]
        params.filterByArea = True
        params.minArea = param_set["minArea"]
        params.maxArea = param_set["maxArea"]
        params.filterByCircularity = True
        params.minCircularity = param_set["minCircularity"]
        
        detector = cv2.SimpleBlobDetector_create(params)
        keypoints = detector.detect(grijswaarden)
        
        afb_result = cv2.drawKeypoints(
            afbeelding.copy(), 
            keypoints, 
            np.array([]), 
            (0, 255, 0),
            cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS
        )
        
        print(f"{param_set['naam']}: {len(keypoints)} blobs gedetecteerd")
        resultaten.append((param_set['naam'], afb_result, len(keypoints)))
    
    # Toon alle resultaten
    fig, axes = plt.subplots(1, 3, figsize=(15, 5))
    for idx, (naam, afb, aantal) in enumerate(resultaten):
        axes[idx].imshow(cv2.cvtColor(afb, cv2.COLOR_BGR2RGB))
        axes[idx].set_title(f'{naam}\n{aantal} blobs')
        axes[idx].axis('off')
    plt.tight_layout()
    plt.show()


def opdracht_3b_overlay(afbeelding, grijswaarden):
    """Opdracht 3b: Overlay van gedetecteerde blobs"""
    print("\n=== Opdracht 3b: Blob Overlay ===")
    
    params = cv2.SimpleBlobDetector_Params()
    params.minThreshold = 10
    params.maxThreshold = 200
    params.filterByArea = True
    params.minArea = 100
    params.maxArea = 5000
    params.filterByCircularity = True
    params.minCircularity = 0.1
    
    detector = cv2.SimpleBlobDetector_create(params)
    keypoints = detector.detect(grijswaarden)
    
    # Maak overlay met verschillende kleuren op basis van grootte
    afbeelding_overlay = afbeelding.copy()
    
    for kp in keypoints:
        x, y = int(kp.pt[0]), int(kp.pt[1])
        grootte = int(kp.size)
        
        # Kleur op basis van grootte: klein=groen, medium=geel, groot=rood
        if grootte < 20:
            kleur = (0, 255, 0)  # Groen
        elif grootte < 40:
            kleur = (0, 255, 255)  # Geel
        else:
            kleur = (0, 0, 255)  # Rood
        
        cv2.circle(afbeelding_overlay, (x, y), grootte, kleur, 2)
        cv2.circle(afbeelding_overlay, (x, y), 2, (255, 0, 255), -1)
    
    print(f"Overlay gemaakt met {len(keypoints)} blobs")
    toon_afbeelding("Blob Overlay (kleur op basis van grootte)", afbeelding_overlay)
    
    return afbeelding_overlay


def opdracht_3c_eigenschappen(afbeelding, grijswaarden):
    """Opdracht 3c: Blob eigenschappen weergeven"""
    print("\n=== Opdracht 3c: Blob Eigenschappen ===")
    
    params = cv2.SimpleBlobDetector_Params()
    params.minThreshold = 10
    params.maxThreshold = 200
    params.filterByArea = True
    params.minArea = 100
    params.maxArea = 5000
    
    detector = cv2.SimpleBlobDetector_create(params)
    keypoints = detector.detect(grijswaarden)
    
    afbeelding_info = afbeelding.copy()
    
    print(f"\nGedetecteerde {len(keypoints)} blobs:")
    print(f"{'Nr':<5} {'X':<8} {'Y':<8} {'Grootte':<10}")
    print("-" * 35)
    
    for idx, kp in enumerate(keypoints[:20]):  # Toon eerste 20 blobs
        x, y = kp.pt
        grootte = kp.size
        
        print(f"{idx+1:<5} {x:<8.1f} {y:<8.1f} {grootte:<10.1f}")
        
        # Teken nummer op afbeelding
        cv2.putText(
            afbeelding_info, 
            str(idx+1), 
            (int(x)+5, int(y)+5),
            cv2.FONT_HERSHEY_SIMPLEX, 
            0.5, 
            (255, 0, 0), 
            1
        )
        cv2.circle(afbeelding_info, (int(x), int(y)), int(grootte), (0, 255, 0), 2)
    
    if len(keypoints) > 20:
        print(f"... en nog {len(keypoints) - 20} blobs meer")
    
    toon_afbeelding("Blob Eigenschappen (eerste 20 genummerd)", afbeelding_info)


def opdracht_3d_zwaartepunt(afbeelding, grijswaarden):
    """Opdracht 3d: Zwaartepunt van blobs bepalen"""
    print("\n=== Opdracht 3d: Zwaartepunten ===")
    
    params = cv2.SimpleBlobDetector_Params()
    params.minThreshold = 10
    params.maxThreshold = 200
    params.filterByArea = True
    params.minArea = 100
    params.maxArea = 5000
    
    detector = cv2.SimpleBlobDetector_create(params)
    keypoints = detector.detect(grijswaarden)
    
    afbeelding_zwaartepunt = afbeelding.copy()
    
    zwaartepunten = []
    for kp in keypoints:
        x, y = kp.pt
        zwaartepunten.append((x, y))
        
        # Teken blob omtrek
        cv2.circle(afbeelding_zwaartepunt, (int(x), int(y)), int(kp.size), (0, 255, 0), 2)
        
        # Teken zwaartepunt als kruis
        cv2.drawMarker(
            afbeelding_zwaartepunt, 
            (int(x), int(y)), 
            (0, 0, 255),
            cv2.MARKER_CROSS, 
            20, 
            2
        )
    
    # Bereken gemiddeld zwaartepunt van alle blobs
    if len(zwaartepunten) > 0:
        gemiddeld_x = np.mean([p[0] for p in zwaartepunten])
        gemiddeld_y = np.mean([p[1] for p in zwaartepunten])
        
        print(f"Gemiddeld zwaartepunt van alle blobs: ({gemiddeld_x:.1f}, {gemiddeld_y:.1f})")
        
        # Teken gemiddeld zwaartepunt
        cv2.drawMarker(
            afbeelding_zwaartepunt,
            (int(gemiddeld_x), int(gemiddeld_y)),
            (255, 0, 255),
            cv2.MARKER_STAR,
            30,
            3
        )
        cv2.putText(
            afbeelding_zwaartepunt,
            "Gemiddeld",
            (int(gemiddeld_x)+15, int(gemiddeld_y)+15),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.6,
            (255, 0, 255),
            2
        )
    
    print(f"Zwaartepunten van {len(zwaartepunten)} blobs berekend")
    toon_afbeelding("Zwaartepunten (rood kruis per blob, paarse ster = gemiddelde)", afbeelding_zwaartepunt)


def opdracht_4_log(afbeelding, grijswaarden):
    """Opdracht 4: Laplacian of Gaussian (LoG)"""
    print("\n=== Opdracht 4: Laplacian of Gaussian (LoG) ===")
    
    # Gaussian blur toepassen
    blurred = cv2.GaussianBlur(grijswaarden, (5, 5), 0)
    
    # Laplacian operator toepassen
    laplacian = cv2.Laplacian(blurred, cv2.CV_64F)
    laplacian = np.uint8(np.absolute(laplacian))
    
    # Threshold om lokale maxima te vinden
    _, binary = cv2.threshold(laplacian, 30, 255, cv2.THRESH_BINARY)
    
    # Vind contouren (blobs)
    contours, _ = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    afbeelding_log = afbeelding.copy()
    
    # Filter contouren op grootte en teken ze
    blob_count = 0
    for contour in contours:
        area = cv2.contourArea(contour)
        if area > 100 and area < 5000:  # Filter op grootte
            M = cv2.moments(contour)
            if M["m00"] != 0:
                cx = int(M["m10"] / M["m00"])
                cy = int(M["m01"] / M["m00"])
                
                # Bereken radius
                radius = int(np.sqrt(area / np.pi))
                
                cv2.circle(afbeelding_log, (cx, cy), radius, (255, 0, 0), 2)
                blob_count += 1
    
    print(f"LoG methode: {blob_count} blobs gedetecteerd")
    toon_afbeelding("Laplacian of Gaussian (LoG)", afbeelding_log)
    
    # Toon ook de Laplacian zelf
    toon_afbeelding("Laplacian (tussenresultaat)", laplacian)
    
    return afbeelding_log


def opdracht_5_dog(afbeelding, grijswaarden):
    """Opdracht 5: Difference of Gaussian (DoG)"""
    print("\n=== Opdracht 5: Difference of Gaussian (DoG) ===")
    
    # Twee verschillende sigma waarden
    sigma1 = 1.0
    sigma2 = 2.0
    
    # Gaussian blur met twee verschillende sigma's
    blur1 = cv2.GaussianBlur(grijswaarden, (0, 0), sigma1)
    blur2 = cv2.GaussianBlur(grijswaarden, (0, 0), sigma2)
    
    # Verschil berekenen
    dog = cv2.subtract(blur2, blur1)
    
    # Threshold om blobs te vinden
    _, binary = cv2.threshold(dog, 20, 255, cv2.THRESH_BINARY)
    
    # Vind contouren
    contours, _ = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    afbeelding_dog = afbeelding.copy()
    
    # Filter en teken contouren
    blob_count = 0
    for contour in contours:
        area = cv2.contourArea(contour)
        if area > 100 and area < 5000:
            M = cv2.moments(contour)
            if M["m00"] != 0:
                cx = int(M["m10"] / M["m00"])
                cy = int(M["m01"] / M["m00"])
                radius = int(np.sqrt(area / np.pi))
                
                cv2.circle(afbeelding_dog, (cx, cy), radius, (0, 255, 255), 2)
                blob_count += 1
    
    print(f"DoG methode: {blob_count} blobs gedetecteerd")
    toon_afbeelding("Difference of Gaussian (DoG)", afbeelding_dog)
    
    # Toon ook het DoG resultaat
    toon_afbeelding("DoG (tussenresultaat)", dog)
    
    return afbeelding_dog


def opdracht_6_doh(afbeelding, grijswaarden):
    """Opdracht 6: Determinant of Hessian (DoH)"""
    print("\n=== Opdracht 6: Determinant of Hessian (DoH) ===")
    
    # Converteer naar float
    img_float = grijswaarden.astype(np.float64)
    
    # Bereken gradiënten
    Ix = ndimage.sobel(img_float, axis=1)
    Iy = ndimage.sobel(img_float, axis=0)
    
    # Bereken tweede afgeleiden
    Ixx = ndimage.sobel(Ix, axis=1)
    Iyy = ndimage.sobel(Iy, axis=0)
    Ixy = ndimage.sobel(Ix, axis=0)
    
    # Bereken Hessian determinant
    det_hessian = (Ixx * Iyy) - (Ixy ** 2)
    
    # Normaliseer
    det_hessian = np.abs(det_hessian)
    det_hessian = (det_hessian - det_hessian.min()) / (det_hessian.max() - det_hessian.min()) * 255
    det_hessian = det_hessian.astype(np.uint8)
    
    # Threshold
    _, binary = cv2.threshold(det_hessian, 50, 255, cv2.THRESH_BINARY)
    
    # Vind contouren
    contours, _ = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    afbeelding_doh = afbeelding.copy()
    
    # Filter en teken contouren
    blob_count = 0
    for contour in contours:
        area = cv2.contourArea(contour)
        if area > 100 and area < 5000:
            M = cv2.moments(contour)
            if M["m00"] != 0:
                cx = int(M["m10"] / M["m00"])
                cy = int(M["m01"] / M["m00"])
                radius = int(np.sqrt(area / np.pi))
                
                cv2.circle(afbeelding_doh, (cx, cy), radius, (255, 255, 0), 2)
                blob_count += 1
    
    print(f"DoH methode: {blob_count} blobs gedetecteerd")
    toon_afbeelding("Determinant of Hessian (DoH)", afbeelding_doh)
    
    # Toon ook de Hessian determinant
    toon_afbeelding("Hessian Determinant (tussenresultaat)", det_hessian)
    
    return afbeelding_doh


def opdracht_7_vergelijking(afb_simple, afb_log, afb_dog, afb_doh):
    """Opdracht 7: Vergelijking van blobdetectiemethoden"""
    print("\n=== Opdracht 7: Vergelijking van methoden ===")
    
    print("\n1. SimpleBlobDetector:")
    print("   + Gemakkelijk te gebruiken met ingebouwde parameters")
    print("   + Kan filteren op specifieke eigenschappen (circulariteit, area, etc.)")
    print("   + Snelle detectie")
    print("   - Minder flexibel voor complexe vormen")
    
    print("\n2. Laplacian of Gaussian (LoG):")
    print("   + Goede detectie van blob-achtige structuren")
    print("   + Schaal-invariant door Gaussian blur")
    print("   + Robuust tegen ruis")
    print("   - Kan valse positieven geven bij randen")
    print("   - Parameter tuning vereist")
    
    print("\n3. Difference of Gaussian (DoG):")
    print("   + Sneller dan LoG")
    print("   + Goede detectie bij verschillende schalen")
    print("   + Benadert LoG efficiënt")
    print("   - Gevoelig voor sigma waarden")
    print("   - Kan kleine details missen")
    
    print("\n4. Determinant of Hessian (DoH):")
    print("   + Zeer goed voor blob-detectie")
    print("   + Gevoelig voor structuur")
    print("   + Robuust tegen rotatie")
    print("   - Rekenintensief")
    print("   - Gevoelig voor ruis")
    
    print("\nConclusie voor pills-in-strip.jpg:")
    print("SimpleBlobDetector werkt het beste voor deze afbeelding omdat:")
    print("- De pillen duidelijk afgebakende, ronde vormen hebben")
    print("- De parameters kunnen worden afgestemd op grootte en vorm")
    print("- Snelle detectie met goede nauwkeurigheid")
    
    # Toon alle resultaten
    fig, axes = plt.subplots(2, 2, figsize=(12, 12))
    
    axes[0, 0].imshow(cv2.cvtColor(afb_simple, cv2.COLOR_BGR2RGB))
    axes[0, 0].set_title('SimpleBlobDetector')
    axes[0, 0].axis('off')
    
    axes[0, 1].imshow(cv2.cvtColor(afb_log, cv2.COLOR_BGR2RGB))
    axes[0, 1].set_title('Laplacian of Gaussian (LoG)')
    axes[0, 1].axis('off')
    
    axes[1, 0].imshow(cv2.cvtColor(afb_dog, cv2.COLOR_BGR2RGB))
    axes[1, 0].set_title('Difference of Gaussian (DoG)')
    axes[1, 0].axis('off')
    
    axes[1, 1].imshow(cv2.cvtColor(afb_doh, cv2.COLOR_BGR2RGB))
    axes[1, 1].set_title('Determinant of Hessian (DoH)')
    axes[1, 1].axis('off')
    
    plt.tight_layout()
    plt.show()


def opdracht_8_eigen_afbeeldingen():
    """Opdracht 8: Blob detectie op eigen afbeeldingen"""
    print("\n=== Opdracht 8: Blob detectie op eigen afbeeldingen ===")
    
    doorgaan = True
    while doorgaan:
        bestand = easygui.fileopenbox(
            msg="Selecteer een eigen afbeelding voor blob detectie",
            title="Eigen afbeelding",
            filetypes=["*.jpg", "*.jpeg", "*.png", "*.bmp"]
        )
        
        if not bestand:
            break
        
        # Lees afbeelding in
        afbeelding = cv2.imread(bestand)
        grijswaarden = cv2.cvtColor(afbeelding, cv2.COLOR_BGR2GRAY)
        
        print(f"\nAnalyse van: {bestand.split('/')[-1]}")
        
        # Test alle vier de methoden
        print("\n1. SimpleBlobDetector...")
        _, afb_simple = opdracht_3_simpleblobdetector(afbeelding, grijswaarden)
        
        print("\n2. Laplacian of Gaussian...")
        afb_log = opdracht_4_log(afbeelding, grijswaarden)
        
        print("\n3. Difference of Gaussian...")
        afb_dog = opdracht_5_dog(afbeelding, grijswaarden)
        
        print("\n4. Determinant of Hessian...")
        afb_doh = opdracht_6_doh(afbeelding, grijswaarden)
        
        # Vergelijking weergeven
        opdracht_7_vergelijking(afb_simple, afb_log, afb_dog, afb_doh)
        
        # Vraag of gebruiker nog een afbeelding wil analyseren
        antwoord = easygui.ynbox(
            "Wil je nog een afbeelding analyseren?",
            "Doorgaan?",
            choices=["Ja", "Nee"]
        )
        doorgaan = antwoord


def main():
    """Hoofdprogramma"""
    print("=== Blob Detectie Opdrachten ===\n")
    
    # Opdrachten 1 & 2
    bestandspad = selecteer_afbeelding()
    if not bestandspad:
        print("Geen afbeelding geselecteerd. Programma wordt afgesloten.")
        return
    
    afbeelding, grijswaarden = opdracht_1_en_2(bestandspad)
    if afbeelding is None:
        return
    
    # Menu voor opdracht selectie
    while True:
        keuze = easygui.buttonbox(
            msg="Welke opdracht wil je uitvoeren?",
            title="Blob Detectie Menu",
            choices=[
                "Opdracht 3: SimpleBlobDetector",
                "Opdracht 3a: Parameters afstemmen",
                "Opdracht 3b: Overlay",
                "Opdracht 3c: Eigenschappen",
                "Opdracht 3d: Zwaartepunt",
                "Opdracht 4: LoG",
                "Opdracht 5: DoG",
                "Opdracht 6: DoH",
                "Opdracht 7: Vergelijking",
                "Opdracht 8: Eigen afbeeldingen",
                "Alle opdrachten uitvoeren",
                "Afsluiten"
            ]
        )
        
        if keuze == "Opdracht 3: SimpleBlobDetector":
            opdracht_3_simpleblobdetector(afbeelding, grijswaarden)
        elif keuze == "Opdracht 3a: Parameters afstemmen":
            opdracht_3a_parameters(afbeelding, grijswaarden)
        elif keuze == "Opdracht 3b: Overlay":
            opdracht_3b_overlay(afbeelding, grijswaarden)
        elif keuze == "Opdracht 3c: Eigenschappen":
            opdracht_3c_eigenschappen(afbeelding, grijswaarden)
        elif keuze == "Opdracht 3d: Zwaartepunt":
            opdracht_3d_zwaartepunt(afbeelding, grijswaarden)
        elif keuze == "Opdracht 4: LoG":
            opdracht_4_log(afbeelding, grijswaarden)
        elif keuze == "Opdracht 5: DoG":
            opdracht_5_dog(afbeelding, grijswaarden)
        elif keuze == "Opdracht 6: DoH":
            opdracht_6_doh(afbeelding, grijswaarden)
        elif keuze == "Opdracht 7: Vergelijking":
            _, afb_simple = opdracht_3_simpleblobdetector(afbeelding, grijswaarden)
            afb_log = opdracht_4_log(afbeelding, grijswaarden)
            afb_dog = opdracht_5_dog(afbeelding, grijswaarden)
            afb_doh = opdracht_6_doh(afbeelding, grijswaarden)
            opdracht_7_vergelijking(afb_simple, afb_log, afb_dog, afb_doh)
        elif keuze == "Opdracht 8: Eigen afbeeldingen":
            opdracht_8_eigen_afbeeldingen()
        elif keuze == "Alle opdrachten uitvoeren":
            print("\n=== Alle opdrachten uitvoeren ===")
            _, afb_simple = opdracht_3_simpleblobdetector(afbeelding, grijswaarden)
            opdracht_3a_parameters(afbeelding, grijswaarden)
            opdracht_3b_overlay(afbeelding, grijswaarden)
            opdracht_3c_eigenschappen(afbeelding, grijswaarden)
            opdracht_3d_zwaartepunt(afbeelding, grijswaarden)
            afb_log = opdracht_4_log(afbeelding, grijswaarden)
            afb_dog = opdracht_5_dog(afbeelding, grijswaarden)
            afb_doh = opdracht_6_doh(afbeelding, grijswaarden)
            opdracht_7_vergelijking(afb_simple, afb_log, afb_dog, afb_doh)
        else:  # Afsluiten
            break
    
    print("\nProgramma beëindigd.")


if __name__ == "__main__":
    main()
