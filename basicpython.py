def swapList(brandList):
    size = len(brandList)

    temp= brandList[0]
    brandList[0] = brandList[size - 1]
    brandList[size - 1] = temp 

    return brandList

brandList = [12, 13, 81, 82, "hj"]

print(swapList(brandList))

def swapList(newList):
    newList[0], newList[-1] = newList[-1], newList[0]

    return newList

newList=  [12, 13, 81, 82, "hj"]
print (swapList(newList))

    
def swapList(list):

    get = list[-1], list[0]

    list[-1], list[2] = get

    return list

list= [12, 13, 81, 82, "hj"]
print (swapList(list))

    

