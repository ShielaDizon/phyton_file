#SHIELA B. DIZON
#structure
#github.com/ShielaDizon
#shiela.dizon1231@gmail.com

def binary_search(item_list, item):
    ela = 0
    dizon = len(item_list)-1
    bartolo = False
    while(ela<=dizon and not bartolo):
        mid = (ela + dizon)//2
        if item_list[mid] == item:
            bartolo = True
        else:
            if item<item_list[mid]:
                dizon = mid-1
            else:
                ela = mid+1
    return bartolo

print (binary_search([1,2,3,5,8],6))
print (binary_search([1,2,3,5,8],5))
