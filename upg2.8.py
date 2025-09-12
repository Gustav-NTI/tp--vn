svar = "Ja"
while svar == "Ja":
    import random
    print ('Tärningarna är kastad')
    n1 = random.randint (1,6)
    n2 = random.randint (1,6)
    print ('Du fick' , n1,'och',n2 )
    print ('Summan är' , n1+n2)
    print ('Vill du kasta igen')
    svar=input ('Ja/Nej: ')
    if svar=='Nej':
        break

        
