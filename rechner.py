print("\t\t\t\tWillkommen im Taschenrechner\n")

antwort1 = input("Gib die erste Zahl ein:\n")
zeichen = input("Gib das Rechenzeichen ein (+, -, *, %, /):\n")
antwort2 = input("Gib die zweite Zahl ein:\n")

antwort1 = int(antwort1)
antwort2 = int(antwort2)
#56rr
if zeichen == "+":
    print("Ergebnis:", antwort1 + antwort2)
elif zeichen == "*":
    print("Ergebnis:", antwort1 * antwort2)
elif zeichen == "%":
    print("Ergebnis:", antwort1 % antwort2)
elif zeichen == "-":
    print("Ergebnis:", antwort1 - antwort2)
elif zeichen == "/":
    if antwort2 == 0:
        print("Fehler: Division durch Null ist nicht erlaubt.")
    else:
        print("Ergebnis:", antwort1 / antwort2)
else:
    print("Ungültiges Rechenzeichen.")
    exit()
#56rr