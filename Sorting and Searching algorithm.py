#SHIELA B. DIZON
#Sorting and Searching Algorithm
#github.com/ShielaDizon
#shiela.dizon1231@gmail.com

def reading_sort(array1, max_val):
    ela = max_val + 1
    count = [0] * ela

    for yro in array1:
        #count occures
        count [yro] += 1
    i = 0
    for yro in range(ela):
        for l in range (count[yro]):
            array1[i] = yro
            i += 1
    return array1

print (reading_sort( [1,2,7,3,2,1,4,2,3,2,5,1,4,5,5,4,6],7))
