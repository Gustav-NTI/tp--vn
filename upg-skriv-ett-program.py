
namn=input ("Vad vill du bli kallad? ")

while True:
    print(f"Toppen {namn}, wreh.")

    val=input("wreh, vill du? ")

    if val.lower() == "vet inte":
        print(f"Okej {namn}.")
    elif val.lower() == "jag vill ha kai":
        print("Mitt förslag är att fråga Jens")
        break
        
        

    else:
        print("Jag förstod inte")

while True:
    val=input("Jens: vad vill du fråga?")
    if val.lower() == "kai":
        print("🤕")
    elif val.lower() == "gör något coolt":
        print("Jens gör en backflip och börjar dansa")
    