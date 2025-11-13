beeld_breedte = float(input("Beeldbreedte: ")) # 50
sensor_breedte = float(input("Sensorbreedte: ")) # 6.4
werk_afstand = float(input("Werkafstand: ")) # 100

brandpunts_afstand  = (sensor_breedte*werk_afstand)/beeld_breedte
print(brandpunts_afstand)