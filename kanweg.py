# Voorbeeld van hoe input en output eruit kunnen zien in easygui
import easygui
import sys

# Vraag de gebruiker om de beeldbreedte in te voeren
beeld_breedte = easygui.enterbox(
    "Voer de **Beeldbreedte** in (mm of cm):",
    "Invoer Beeldbreedte"
)

easygui.msgbox(f"Beeldbreedte: {beeld_breedte}", "Invoer Bevestigd")