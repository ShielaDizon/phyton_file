#SHIELA B. DIZON
#DICTIONARY
#github.com/ShielaDizon
#shiela.dizon1231@gmail.com

print ("\n\t\t KOREAN ACTORS BIBLIOGRAPHY\n\t\t\tQUICK FACTS \n\n 1. Kang Ha-Neul \t\t 2. Lee Jong-Suk \n 3. Lee Dong-Wook \t\t 4. Park Hyung-Sik \n 5. Lee Min-Ho \t\t\t 6. Song Joong-Ki \n 7. Goong Yoo \t\t\t 8. Kim Soo-Hyun \n 9. Ji Chang-Wook \t\t 10. Lee Joon-Gi \n")
def ela():

    shiela = {"1": " Name: Kang Ha-Neul \n Age: 28 Years \n Birth Date: February 21, 1990 \n Sun Sign: Pisces \n Height: 1.82 m \n Born in: Busan, South Korea \n Net worth: $60 million as of Jan 31, 2017 ", "2" : " Name: Lee Jong-Suk \n Age: 28 Years \n Birth Date: September 14, 1989 \n Sun Sign: Virgo \n Height: 1.86 m \n Born in: Suwon, South Korea ", "3" : " Name: Lee Dong-Wook \n Age: 36 Years \n Birth Date: November 6, 1981 \n Sun Sign: Scorpio \n Height: 1.84 m \n Born in: Seoul, South Korea \n Net worth: $3 Million as of Jan 31, 2017 ", "4" : " Name: Park Hyung-Sik \n Age: 26 Years \n Birth Date: November 16, 1991 \n Sun Sign: Scorpio \n Born in: Yongin, South Korea ", "5" : " Name: Lee Min-Ho \n Age: 30 Years \n Birth Date: June 22, 1987 \n Sun Sign: Cancer \n Born in: Seoul, South Korea ", "6" : " Name: Song Joong-Ki \n Age: 32 Years \n Birth Date: September 19, 1985 \n Sun Sign: Virgo \n Height: 1.78 m \n Born in: Secheon-dong, Daejeon, South Korea ", "7" : " Name: Goong Yoo \n Age: 38 Years \n Birth Date: July 10, 1979 \n Sun Sign: Cancer \n Height: 1.84 m \n Born in: Busan, South Korea \n Net worth: $2 million as of Jan 2017 ", "8" : " Name: Kim Soo-Hyun \n Age: 30 Years \n Birth Date: February 16, 1988 \n Sun Sign: Aquarius \n Height: 1.8 m \n Born in: Seoul, South Korea \n Net worth: $1 million as of jan 2017 ", "9" : " Name: Ji Chang-Wook \n Age: 30 Years \n Birth Date: July 5, 1987 \n Sun Sign: Cancer \n Height: 1.82 m \n Born in: Anyang, South Korea ", "10" : " Name: Lee Joon-Gi \n Age: 35 Years \n Birth Date: May 17, 1982 \n Sun Sign: Taurus \n Born in: Busan, South Korea ",}

    yroy = input("\n NO.  ")
    if yroy == 1:
        print shiela["1"]
    elif yroy == 2:
        print shiela["2"]
    elif yroy == 3:
        print shiela["3"]
    elif yroy == 4:
        print shiela["4"]
    elif yroy == 5:
        print shiela["5"]
    elif yroy == 6:
        print shiela["6"]
    elif yroy == 7:
        print shiela["7"]
    elif yroy == 8:
        print shiela["8"]
    elif yroy == 9:
        print shiela["9"]
    elif yroy == 10:
        print shiela["10"]
    else:
        print ("No name matched with the no. you've entered!!!")
        return ela()
    return ela()

    
ela()
