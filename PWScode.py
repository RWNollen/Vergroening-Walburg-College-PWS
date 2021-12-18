
#   Dit is een programma geschreven om de waardes van 2 bodemvochtsensoren te vergelijken met de gewenste waardes om te kijken of een sproeisysteem aan moet of niet.

#   De lijn hieronder geeft toegang tot wat extra functies zoals time.sleep() wat gebruikt word om het programma voor een bepaalde tijd te laten pauzeren.
import time

#   Hieronder is de setup. Dit stelt vragen om te kijken wat de waardes zijn die gewenst zijn.
#   Aan het eind van de setup worden alle antwoorden opnieuw weergegeven en wordt er gevraagt of alles klopt. 
#   Als er nee wordt geantwoord begint de setup opnieuw, anders start het programma.
#   Het programma stopt niet automatisch en blijft voor altijd doorgaan zonder dat de setup opnieuw gedaan hoeft te worden.
#   Als de setup aangepast moet worden, moet het programma opnieuw worden opgestart.
setup = str("nee")
while setup == "nee":
    
    print("Wat is het gemiddelde resutaat van de sensor als deze droge grond meet?")
    ValDry = int(float(input("Geef een resultaat: ")))
    print("Het resultaat in droge grond is:", ValDry)

    print("Wat is het gemiddelde resutaat van de sensor als deze hele natte grond meet?")
    ValWet = int(float(input("Geef een resultaat: ")))
    print("Het resultaat in hele natte grond is:", ValWet)

    print("Wat is de optimale relatieve vochtigheid van de grond (RH) in %?")
    desired_RH = int(float(input("Geef een nummer: ")))
    while desired_RH not in range(0,101,1):
        print("Dit nummer zit niet tussen 0 en 100. Vul een nieuw nummer in.")
        desired_RH = int(float(input("Geef een nummer: ")))
    print("De optimale RH is:", desired_RH)

    print("Wat is de toegestane variatie van deze optimale RH? (in %)")
    variation = int(float(input("Geef een nummer: ")))
    while variation not in range(0,101,1):
        print("Dit nummer zit niet tussen 0 en 100. Vul een nieuw nummer in.")
        variation = int(float(input("Geef een nummer: ")))
    print("De toegestane variatie is:", variation)

    print("Hoeveel tijd moet er tussen grondmetingen zitten? (in seconden)")
    delay = int(float(input("Geef een nummer: ")))
    print("Er zitten", delay, "seconden tussen elke grondmeting.")

    print("Hoelang moeten de sproeiers aan gaan wanneer alle grond te droog is? (in seconden)")
    TimeAll = int(float(input("Geef een nummer: ")))
    print("De sproeier gaat voor", TimeAll, "seconden aan wanneer alle grond te droog is.")

    print("Hoelang moeten de sproeiers aan gaan wanneer de bovenste laag grond te droog is? (in seconden)")
    TimeTop = int(float(input("Geef een nummer: ")))
    print("De sproeier gaat voor", TimeTop, "seconden aan wanneer de bovenste laag grond te droog is.")

    print("Hoelang moeten de sproeiers aan gaan wanneer de onderste laag grond te droog is? (in seconden)")
    TimeBottom = int(float(input("Geef een nummer: ")))
    print("De sproeier gaat voor", TimeBottom, "seconden aan wanneer de onderste laag grond te droog is.")
    
    
    time.sleep(1)

    print("")
    print("")
    print("Het resultaat in droge grond is:", ValDry)
    print("Het resultaat in hele natte grond is:", ValWet)
    print("De optimale RH is:", desired_RH)
    print("De toegestane variatie is:", variation)
    print("Er zitten", delay, "seconden tussen elke grondmeting.")
    print("De sproeier gaat voor", TimeAll, "seconden aan wanneer alle grond te droog is.")
    print("De sproeier gaat voor", TimeTop, "seconden aan wanneer de bovenste laag grond te droog is.")
    print("De sproeier gaat voor", TimeBottom, "seconden aan wanneer de onderste laag grond te droog is.")
    setupcheck = str(input("Zijn deze waardes correct? (ja/nee): "))


    while setup is not "ja":
        if setupcheck == "ja":
            setup = "ja"
        elif setupcheck == "nee":
            print("Setup opnieuw beginnen.")
            time.sleep(1)
        else:
            print("Dit is geen mogelijk antwoord, vul ja of nee in")
            setupcheck = str(input("Zijn deze waardes correct? (ja/nee): "))

print("Setup is compleet. Het programma begint nu met werken.")



while True:
    #Dit stuk hieronder word normaal vervangen met de automatische metingen van de vochtsensor. Nu word dit dus handmatig ingevoerd bij elke metingtijd.
    print("Wat is het resultaat van de bovenste sensor? (tussen", ValWet, "en", ValDry,")")
    valTop = int(float(input("Geef een resultaat: ")))
    while valTop not in range(ValWet,ValDry + 1,1):
        print("Dit resultaat zit niet tussen", ValWet, "en", ValDry,". Vul een nieuw resultaat in.")
        valTop = int(float(input("Geef een resultaat: ")))     
    print("het resultaat van de bovenste sensor is:", valTop)

    print("Wat is het resultaat van de onderste sensor? (tussen", ValWet, "en", ValDry,")")
    valBottom = int(float(input("Geef een resultaat: ")))
    while valBottom not in range(ValWet,ValDry + 1,1):
        print("Dit resultaat zit niet tussen", ValWet, "en", ValDry,". Vul een nieuw resultaat in.")
        valBottom = int(float(input("Geef een resultaat: ")))     
    print("Het resultaat van de onderste sensor is:", valBottom)


#   Hieronder worden de waardes van de bovenste en onderste sensor omgezet in 0-100%
    RHtop = int(float((ValWet/valTop)*100))
    RHbottom = int(float((ValWet/valBottom)*100))

    print("De RH van de bovenste sensor is:", RHtop)
    print("De RH van de onderste sensor is:", RHbottom)

#   Hieronder word de toegestane variatie bij de waardes opgeteld, en word gekeken of het onder de gewilde RH is.
#   Als de waarde van de sensor + variatie onder de gewilde RH is word er een nummer opgeteld bij de "situation" variabele.
#   Door de bovenste sensor 1 en de onderste sensor 2 erbij op te laten tellen krijgen de 4 mogelijke situaties allemaal een andere waarde van 0-4.
    if RHtop + variation < desired_RH:
        situation = situation + 1
    if RHbottom + variation < desired_RH:
        situation = situation + 2

#   Met gebruik van de 4 "if" statements kunnen we iets anders laten gebeuren per situatie. Hierna word de variabele weer 0 voor de volgende meting.
    situation = 0
    if situation == 0:
        print("Alle grond is nog nat genoeg. Er gebeurd dus niks")
    if situation == 1:
        print("De bovenste sensor meet dat de grond te droog is, maar de onderste sensor meet dat de grond nat genoeg is. De sproeiers gaan nu voor", TimeTop, "seconden aan.")
        #Hier komt de code die de sproeier aan laat gaan.
        time.sleep(TimeTop)
        #Hier komt de code die de sproeiers uit laat gaan.
    if situation == 2:
        print("De onderste sensor meet dat de grond te droog is, maar de bovenste sensor meet dat de grond nat genoeg is. De sproeiers gaan nu voor", TimeBottom, "seconden aan.")
        #Hier komt de code die de sproeier aan laat gaan.
        time.sleep(TimeBottom)
        #Hier komt de code die de sproeiers uit laat gaan.
    if situation == 3:
        print("Beide sensoren meten dat de grond te droog is. De sproeiers gaan nu voor", TimeAll, "seconden aan.")
        #Hier komt de code die de sproeier aan laat gaan.
        time.sleep(TimeAll)
        #Hier komt de code die de sproeiers uit laat gaan.

    situation = 0

#   Deze lijn hieronder zorgt ervoor dat de loop die we hebben gecreerd niet constant opnieuw start, maar eerst steeds de gewenste tijd wacht.
    time.sleep(delay)
    
