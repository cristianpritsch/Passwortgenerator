import random
import string

print("=== Passwortgenerator ===")

while True:

    while True:
        try:
            length = int(input("Wie lang soll das Passwort sein? (mindestens 8 Zeichen): "))

            if length < 8:
                print("Bitte mindestens 8 Zeichen eingeben.\n")
                continue

            break

        except ValueError:
            print("Bitte eine gültige Zahl eingeben.\n")

    characters = string.ascii_letters + string.digits + string.punctuation

    password = "".join(random.choice(characters) for _ in range(length))

    print("\nDein Passwort lautet:\n")
    print(password)

    erneut = input("\nMöchtest du ein weiteres Passwort erstellen? (j/n): ").lower()

    if erneut != "j":
        print("\nDanke für die Nutzung des Passwortgenerators!")
        break
