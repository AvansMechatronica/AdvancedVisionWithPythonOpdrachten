# Werken met wiskunde in Sphinx

Je kunt wiskundige formules toevoegen aan je documentatie met Sphinx en MathJax.

**Inline voorbeeld:**

De lensformule: $\frac{1}{f} = \frac{1}{u} + \frac{1}{v}$

**Blokvoorbeeld:**

$$
E = mc^2
$$

Gebruik `$...$` voor inline en `$$...$$` voor blokformules in je Markdown-bestanden.

## Voorbeeld: Brandpuntsafstand berekenen

De brandpuntsafstand ($f$) van een lens kan worden berekend met de volgende formule:

$$
f = \frac{\text{sensorbreedte} \times \text{werkafstand}}{\text{beeldbreedte}}
$$

waarbij:
- $f$ = brandpuntsafstand
- sensorbreedte = breedte van de sensor
- werkafstand = afstand tussen lens en object
- beeldbreedte = breedte van het beeld op de sensor

Gebruik deze formule om de juiste lens te kiezen voor je toepassing.