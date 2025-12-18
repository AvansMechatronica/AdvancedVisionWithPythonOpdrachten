"""
Feature Detectie - Opdrachten 1 t/m 8
Detecteert features in afbeeldingen met Harris, SIFT en ORB methoden
"""

import cv2
import numpy as np
import easygui
from matplotlib import pyplot as plt


def selecteer_afbeelding():
    """Opdracht 1: Laat gebruiker een afbeelding selecteren"""
    bestandspad = easygui.fileopenbox(
        msg="Selecteer een afbeelding",
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


def opdracht_3_harris(afbeelding, grijswaarden):
    """Opdracht 3: Harris Corner Detection"""
    # Harris corner detection parameters
    afbeelding_float = np.float32(grijswaarden)
    harris_respons = cv2.cornerHarris(afbeelding_float, blockSize=2, ksize=3, k=0.04)
    
    # Dilate om hoeken te markeren
    harris_respons = cv2.dilate(harris_respons, None)
    
    # Markeer hoeken op originele afbeelding (rode stippen)
    afbeelding_harris = afbeelding.copy()
    afbeelding_harris[harris_respons > 0.01 * harris_respons.max()] = [0, 0, 255]
    
    print(f"Opdracht 3: Harris Corner Detection - {np.sum(harris_respons > 0.01 * harris_respons.max())} hoeken gedetecteerd")
    toon_afbeelding("Harris Corner Detection", afbeelding_harris)
    
    return afbeelding_harris


def opdracht_4_sift(afbeelding, grijswaarden):
    """Opdracht 4: SIFT Feature Detection"""
    # SIFT detector aanmaken
    sift = cv2.SIFT_create()
    
    # Keypoints en descriptors detecteren
    keypoints, descriptors = sift.detectAndCompute(grijswaarden, None)
    
    # Teken keypoints op afbeelding
    afbeelding_sift = cv2.drawKeypoints(
        afbeelding, 
        keypoints, 
        None, 
        flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS
    )
    
    print(f"Opdracht 4: SIFT - {len(keypoints)} keypoints gedetecteerd")
    toon_afbeelding("SIFT Feature Detection", afbeelding_sift)
    
    return keypoints, descriptors, afbeelding_sift


def opdracht_5_orb(afbeelding, grijswaarden):
    """Opdracht 5: ORB Feature Detection"""
    # ORB detector aanmaken
    orb = cv2.ORB_create()
    
    # Keypoints en descriptors detecteren
    keypoints, descriptors = orb.detectAndCompute(grijswaarden, None)
    
    # Teken keypoints op afbeelding
    afbeelding_orb = cv2.drawKeypoints(
        afbeelding, 
        keypoints, 
        None, 
        color=(0, 255, 0),
        flags=0
    )
    
    print(f"Opdracht 5: ORB - {len(keypoints)} keypoints gedetecteerd")
    toon_afbeelding("ORB Feature Detection", afbeelding_orb)
    
    return keypoints, descriptors, afbeelding_orb


def opdracht_6_vergelijking(afb_harris, afb_sift, afb_orb):
    """Opdracht 6: Vergelijking van Feature Detection Methoden"""
    print("\n=== Opdracht 6: Vergelijking van methoden ===")
    print("\nHarris Corner Detection:")
    print("+ Snel en efficiënt")
    print("+ Goed voor hoeken en scherpe randen")
    print("- Niet schaal-invariant")
    print("- Minder robuust bij rotatie")
    
    print("\nSIFT (Scale-Invariant Feature Transform):")
    print("+ Schaal-invariant")
    print("+ Robuust tegen rotatie en belichting")
    print("+ Hoge nauwkeurigheid")
    print("- Trager dan andere methoden")
    print("- Beschermd door patenten (vroeger)")
    
    print("\nORB (Oriented FAST and Rotated BRIEF):")
    print("+ Zeer snel")
    print("+ Robuust tegen rotatie")
    print("+ Open source en gratis")
    print("- Minder robuust dan SIFT bij schaalveranderingen")
    print("- Lagere nauwkeurigheid bij extreme transformaties")
    
    print("\nConclusie voor pills-in-strip.jpg:")
    print("SIFT werkt het beste voor deze afbeelding vanwege:")
    print("- Goede detectie van pillen met verschillende groottes")
    print("- Robuust tegen variaties in belichting")
    print("- Hoge nauwkeurigheid voor kleine details")
    
    # Toon alle resultaten naast elkaar met matplotlib
    fig, axes = plt.subplots(1, 3, figsize=(15, 5))
    axes[0].imshow(cv2.cvtColor(afb_harris, cv2.COLOR_BGR2RGB))
    axes[0].set_title('Harris Corner Detection')
    axes[0].axis('off')
    
    axes[1].imshow(cv2.cvtColor(afb_sift, cv2.COLOR_BGR2RGB))
    axes[1].set_title('SIFT Feature Detection')
    axes[1].axis('off')
    
    axes[2].imshow(cv2.cvtColor(afb_orb, cv2.COLOR_BGR2RGB))
    axes[2].set_title('ORB Feature Detection')
    axes[2].axis('off')
    
    plt.tight_layout()
    plt.show()


def opdracht_7_matching():
    """Opdracht 7: Feature Matching tussen twee afbeeldingen"""
    print("\n=== Opdracht 7: Feature Matching ===")
    
    # Selecteer eerste afbeelding
    print("Selecteer de eerste afbeelding...")
    bestand1 = easygui.fileopenbox(
        msg="Selecteer de eerste afbeelding",
        title="Eerste afbeelding",
        filetypes=["*.jpg", "*.jpeg", "*.png", "*.bmp"]
    )
    if not bestand1:
        print("Geen afbeelding geselecteerd")
        return
    
    # Selecteer tweede afbeelding
    print("Selecteer de tweede afbeelding...")
    bestand2 = easygui.fileopenbox(
        msg="Selecteer de tweede afbeelding",
        title="Tweede afbeelding",
        filetypes=["*.jpg", "*.jpeg", "*.png", "*.bmp"]
    )
    if not bestand2:
        print("Geen afbeelding geselecteerd")
        return
    
    # Lees afbeeldingen in
    img1 = cv2.imread(bestand1)
    img2 = cv2.imread(bestand2)
    gray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
    gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
    
    # Gebruik SIFT voor feature detection
    sift = cv2.SIFT_create()
    kp1, des1 = sift.detectAndCompute(gray1, None)
    kp2, des2 = sift.detectAndCompute(gray2, None)
    
    print(f"Afbeelding 1: {len(kp1)} keypoints")
    print(f"Afbeelding 2: {len(kp2)} keypoints")
    
    # Brute Force Matcher
    bf = cv2.BFMatcher(cv2.NORM_L2, crossCheck=True)
    matches = bf.match(des1, des2)
    
    # Sorteer matches op afstand (beste matches eerst)
    matches = sorted(matches, key=lambda x: x.distance)
    
    print(f"Aantal matches: {len(matches)}")
    
    # Teken de beste 50 matches
    img_matches = cv2.drawMatches(
        img1, kp1, img2, kp2, matches[:50], None,
        flags=cv2.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS
    )
    
    toon_afbeelding("Feature Matching (SIFT + BFMatcher)", img_matches)
    
    # Probeer ook met ORB
    print("\nProbeer ook ORB matching...")
    orb = cv2.ORB_create()
    kp1_orb, des1_orb = orb.detectAndCompute(gray1, None)
    kp2_orb, des2_orb = orb.detectAndCompute(gray2, None)
    
    # BFMatcher met Hamming distance voor ORB
    bf_orb = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
    matches_orb = bf_orb.match(des1_orb, des2_orb)
    matches_orb = sorted(matches_orb, key=lambda x: x.distance)
    
    print(f"ORB matches: {len(matches_orb)}")
    
    img_matches_orb = cv2.drawMatches(
        img1, kp1_orb, img2, kp2_orb, matches_orb[:50], None,
        flags=cv2.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS
    )
    
    toon_afbeelding("Feature Matching (ORB + BFMatcher)", img_matches_orb)


def opdracht_8_eigen_afbeeldingen():
    """Opdracht 8: Feature Detectie op eigen afbeeldingen"""
    print("\n=== Opdracht 8: Feature Detectie op eigen afbeeldingen ===")
    
    doorgaan = True
    while doorgaan:
        bestand = easygui.fileopenbox(
            msg="Selecteer een eigen afbeelding voor feature detectie",
            title="Eigen afbeelding",
            filetypes=["*.jpg", "*.jpeg", "*.png", "*.bmp"]
        )
        
        if not bestand:
            break
        
        # Lees afbeelding in
        afbeelding = cv2.imread(bestand)
        grijswaarden = cv2.cvtColor(afbeelding, cv2.COLOR_BGR2GRAY)
        
        print(f"\nAnalyse van: {bestand.split('/')[-1]}")
        
        # Test alle drie de methoden
        print("\n1. Harris Corner Detection...")
        afb_harris = opdracht_3_harris(afbeelding, grijswaarden)
        
        print("\n2. SIFT Feature Detection...")
        kp_sift, des_sift, afb_sift = opdracht_4_sift(afbeelding, grijswaarden)
        
        print("\n3. ORB Feature Detection...")
        kp_orb, des_orb, afb_orb = opdracht_5_orb(afbeelding, grijswaarden)
        
        # Vergelijking weergeven
        opdracht_6_vergelijking(afb_harris, afb_sift, afb_orb)
        
        # Vraag of gebruiker nog een afbeelding wil analyseren
        antwoord = easygui.ynbox(
            "Wil je nog een afbeelding analyseren?",
            "Doorgaan?",
            choices=["Ja", "Nee"]
        )
        doorgaan = antwoord


def main():
    """Hoofdprogramma"""
    print("=== Feature Detectie Opdrachten ===\n")
    
    # Opdrachten 1 & 2
    bestandspad = selecteer_afbeelding()
    if not bestandspad:
        print("Geen afbeelding geselecteerd. Programma wordt afgesloten.")
        return
    
    afbeelding, grijswaarden = opdracht_1_en_2(bestandspad)
    if afbeelding is None:
        return
    
    # Opdracht 3: Harris
    afb_harris = opdracht_3_harris(afbeelding, grijswaarden)
    
    # Opdracht 4: SIFT
    kp_sift, des_sift, afb_sift = opdracht_4_sift(afbeelding, grijswaarden)
    
    # Opdracht 5: ORB
    kp_orb, des_orb, afb_orb = opdracht_5_orb(afbeelding, grijswaarden)
    
    # Opdracht 6: Vergelijking
    opdracht_6_vergelijking(afb_harris, afb_sift, afb_orb)
    
    # Menu voor opdrachten 7 en 8
    keuze = easygui.buttonbox(
        msg="Welke opdracht wil je uitvoeren?",
        title="Keuze menu",
        choices=["Opdracht 7: Feature Matching", "Opdracht 8: Eigen afbeeldingen", "Afsluiten"]
    )
    
    if keuze == "Opdracht 7: Feature Matching":
        opdracht_7_matching()
    elif keuze == "Opdracht 8: Eigen afbeeldingen":
        opdracht_8_eigen_afbeeldingen()
    
    print("\nProgramma beëindigd.")


if __name__ == "__main__":
    main()
