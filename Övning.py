import random

questions = [
    {
        "fråga": "Vad används för att ge variabler ett värde i Python?",
        "alternativ": ["A: := (kolon lika med)", "B: = (lika med)", "C: == (dubbla lika med)", "D: -> (pil)"],
        "rätt": "B"
    },
    {
        "fråga": "Vilken datatyp används för heltal i Python?",
        "alternativ": ["A: int", "B: str", "C: float", "D: bool"],
        "rätt": "A"
    },
    {
        "fråga": "Hur skriver man en villkorssats som undersöker om x är större än 5?",
        "alternativ": ["A: if x > 5:", "B: if x => 5:", "C: if (x > 5)", "D: if x gt 5:"],
        "rätt": "A"
    },
    {
        "fråga": "Vilken loop används för att upprepa ett bestämt antal gånger?",
        "alternativ": ["A: while-loop", "B: for-loop", "C: repeat-loop", "D: do-while-loop"],
        "rätt": "B"
    },
    {
        "fråga": "Vilken funktion används för att läsa in data från användaren?",
        "alternativ": ["A: print()", "B: input()", "C: read()", "D: scan()"],
        "rätt": "B"
    },
    {
        "fråga": "Hur skriver man ut text till skärmen?",
        "alternativ": ["A: print()", "B: echo()", "C: output()", "D: write()"],
        "rätt": "A"
    },
    {
        "fråga": "Vilken datatyp används för sann/falsk-värden?",
        "alternativ": ["A: bool", "B: int", "C: str", "D: float"],
        "rätt": "A"
    },
    {
        "fråga": "Hur skriver man en loop som kör så länge x är mindre än 10?",
        "alternativ": ["A: while x < 10:", "B: for x < 10:", "C: until x == 10:", "D: repeat x < 10:"],
        "rätt": "A"
    },
    {
        "fråga": "Vilken operator används för att jämföra om två värden är lika?",
        "alternativ": ["A: =", "B: !=", "C: ==", "D: <>"],
        "rätt": "C"
    },
    {
        "fråga": "Hur kan du konvertera ett tal till en sträng i Python?",
        "alternativ": ["A: str()", "B: int()", "C: float()", "D: bool()"],
        "rätt": "A"
    },
    {
        "fråga": "Vad ger uttrycket 5 // 2 i Python?",
        "alternativ": ["A: 2.5", "B: 2", "C: 3", "D: 1"],
        "rätt": "B"
    },
    {
        "fråga": "Vilken funktion används för att räkna längden på en sträng?",
        "alternativ": ["A: length()", "B: count()", "C: size()", "D: len()"],
        "rätt": "D"
    },
    {
        "fråga": "Hur kan du skriva en if-else-sats i Python?",
        "alternativ": ["A: if x: else:", "B: if x then else:", "C: if x: ... else: ...", "D: if x else:"],
        "rätt": "C"
    },
    {
        "fråga": "Vad är resultatet av uttrycket True and False?",
        "alternativ": ["A: True", "B: False", "C: 1", "D: 0"],
        "rätt": "B"
    },
    {
        "fråga": "Vilken datatyp får resultatet av input() om inget konverteras?",
        "alternativ": ["A: int", "B: str", "C: float", "D: bool"],
        "rätt": "B"
    },
    {
        "fråga": "Hur kan man avbryta en while-loop i Python?",
        "alternativ": ["A: continue", "B: return", "C: break", "D: stop"],
        "rätt": "C"
    }
]

while True:
    print("Välkommen till Python-quiz från kapitel 2, 3 och 4!\n")
    poäng = 0

    slumpade_frågor = random.sample(questions, len(questions))

    for i, q in enumerate(slumpade_frågor, 1):
        print(f"Fråga {i}: {q['fråga']}")
        for alt in q["alternativ"]:
            print(alt)
        svar = input("Ditt svar (A, B, C eller D): ").strip().upper()
        if svar == q["rätt"]:
            print("Rätt!\n")
            poäng += 1
        else:
            print(f"Fel! Rätt svar är: {q['rätt']}\n")

    print(f"Quizet är klart! Du fick {poäng} av {len(questions)} poäng.")

    fortsätta = input("Vill du fortsätta? (ja/nej): ").strip().lower()
    if fortsätta != "ja":
        print("Tack för att du spelade!")
        break