#SHIELA B. DIZON
#REMOVE DUPLICATES
#github.com/ShielaDizon
#shiela.dizon1231@gmail.com

def byeduplicate ():
    shiela = input ("ENTER NUMBERS:")
    shiela = list (shiela)
    ela = []

    for i in shiela:
        if i not in ela:
            ela.append(i)

    print ela
byeduplicate()
