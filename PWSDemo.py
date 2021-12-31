#De volgende vier regels importeren meer functies
import time
from w1thermsensor import W1ThermSensor, Unit
from gpiozero import LED
import RPi.GPIO as GPIO
#Deze drie regels laten het programma weten wat voor sensor het is en waar de LED lampjes zitten.
red = LED(18)
green = LED(24)
sensor = W1ThermSensor()


setup = str("nee")
while setup == "nee":

    print("Stop de sensor in ijskoud water. Zit de sensor in ijskoud water? (ja/nee)")
    IceLoop = str(input("(ja/nee)?: " ))
    while IceLoop != "ja":
        print("Stop de sensor in ijskoud water. Zit de sensor in ijskoud water? (ja/nee)")
        IceLoop = str(input("(ja/nee)?: "))
    print("De sensor gaat nu de temperatuur meten. Dit kan even duren.")
    time.sleep(10)
    ValIce = int(float(sensor.get_temperature(Unit.DEGREES_C)))
    print("De temperatuur gemeten in ijskoud water is", ValIce, "Celcius")
    time.sleep(1)

    print("Stop de sensor in super warm water. Zit de sensor in super warm water? (ja/nee)")
    WarmLoop = str(input("(ja/nee)?: " ))
    while WarmLoop != "ja":
        print("Stop de sensor in super warm water. Zit de sensor in super warm water? (ja/nee)")
        WarmLoop = str(input("(ja/nee)?: "))
    print("De sensor gaat nu de temperatuur meten. Dit kan even duren.")
    time.sleep(10)
    ValWarm = int(float(sensor.get_temperature(Unit.DEGREES_C)))
    print("De temperatuur gemeten in super warm water is", ValWarm, "Celcius")
    time.sleep(1)

    print("Wat is de optimale temperatuur? (in Celcius)")
    OptTemp = int(float(input("Geef een nummer: ")))
    while OptTemp not in range(ValIce, ValWarm + 1, 1):
        print("Wat is de optimale temperatuur? (in Celcius)")
        OptTemp = int(float(input("Geef een nummer: ")))
    print("De optimale temperatuur is:",  OptTemp, "Celcius")
    time.sleep(1)

    print("Wat is de toegestane variatie van deze optimale temperatuur? (in %)")
    variation = int(float(input("Geef een nummer: ")))
    while variation not in range(0,101,1):
        print("Wat is de toegestane variatie van deze optimale temperatuur? (in %)")
        variation = int(float(input("Geef een nummer: ")))
    print("De toegestane variatie is:", variation,"%")
    time.sleep(1)

    print("Hoelang moet er tussen metingen zitten? (in seconden)")
    delay = int(float(input("Geef een nummer: ")))
    print("Er zitten", delay, "seconden tussen metingen.")
    time.sleep(2)

    print("De temperatuur gemeten in ijskoud water is", ValIce, "Celcius")
    print("De temperatuur gemeten in super warm water is", ValWarm, "Celcius")
    print("De optimale temperatuur is:",  OptTemp, "Celcius")
    print("De toegestane variatie is:", variation,"%")
    print("Er zitten", delay, "seconden tussen metingen.")
    setupcheck = str(input("Zijn deze waardes correct? (ja/nee)"))

    while setup != "ja":
        if setupcheck == "ja":
            setup = "ja"
        elif setupcheck == "nee":
            print("Setup opnieuw beginnen.")
            time.sleep(1)
            break
        else:
            print("Dit is geen mogelijk antwoord, vul ja of nee in")
            setupcheck = str(input("Zijn deze waardes correct? (ja/nee)"))

print("Setup is compleet. Het programma begint nu met werken.")
                     

while True:
    temp = int(float(sensor.get_temperature(Unit.DEGREES_C)))
    print(temp, "Celcius")

    RT = int(float((ValWarm/temp)*100))
    print("RT is:", RT, "%")

    if RT + variation < OptTemp:
        green.on()
    else:
        red.on()

    time.sleep(5)
    green.off()
    red.off()
    time.sleep(delay)





#green.off()
#while True:
#    temp = int(float(sensor.get_temperature(Unit.DEGREES_C)))
#    print(temp, "Celcius")
#    if temp > 25:
#            green.on()
#            red.off()
#    time.sleep(1)



