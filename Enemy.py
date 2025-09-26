from time import sleep
import random

Kaj = 100
Jens = 90

print("och stöter på Jens och Kaj\n")
print("fish fight\n")

while True:
    sleep(3)
    Jens_attack = random.randint(1,10)
    Kaj_attack = random.randint(1,10)
    Kaj -= Jens_attack
    Jens -= Kaj_attack
    print(f"Kaj slår Jens för {Kaj_attack}")
    print(f"Jens slår tillbaks med {Jens_attack}\n")
    print(f"Jens har {Jens} liv kvar")
    print(f"Kaj har {Kaj} liv kvar\n")
    if Kaj<=0:
        print ("Å nej Kaj har svimmat")
        break
    elif Jens<=0:
        print ("Å nej Jens har svimmat")
        break


