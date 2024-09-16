import math

def minMax(currDeapth, node, isMaximizer, leafNodes, treeDeapth, darkMagicCost):
  if (currDeapth==treeDeapth):
    return leafNodes[node], False

  if (isMaximizer):
    noDarkMagic1 = minMax(currDeapth+1, node*2, False, leafNodes, treeDeapth, darkMagicCost)
    noDarkMagic2 = minMax(currDeapth+1, node*2+1, False, leafNodes, treeDeapth, darkMagicCost)
    
    noDarkMagicVal1 = noDarkMagic1[0]
    noDarkMagicVal2 = noDarkMagic2[0]
    
    noDarkMagicVal = max(noDarkMagicVal1, noDarkMagicVal2)
    isDarkMagicUsed = noDarkMagic1[1] and noDarkMagic2[1]
    
    if (currDeapth == 0):
        wentLeft = noDarkMagicVal1 > noDarkMagicVal2
        return noDarkMagicVal, isDarkMagicUsed, wentLeft
    else:
        return noDarkMagicVal, isDarkMagicUsed
    
  else:
    noDarkMagic1 = minMax(currDeapth+1, node*2, True, leafNodes, treeDeapth, darkMagicCost)
    noDarkMagic2 = minMax(currDeapth+1, node*2+1, True, leafNodes, treeDeapth, darkMagicCost)
    
    noDarkMagicVal1 = noDarkMagic1[0]
    noDarkMagicVal2 = noDarkMagic2[0]
    
    noDarkMagic = min(noDarkMagicVal1, noDarkMagicVal2)
    darkMagic = max(noDarkMagicVal1, noDarkMagicVal2) - darkMagicCost
    if (darkMagic <= noDarkMagic):
        isDarkMagicUsed = noDarkMagic1[1] and noDarkMagic2[1]
        return noDarkMagic, isDarkMagicUsed
    
    else:
        isDarkMagicUsed = True
        return darkMagic, isDarkMagicUsed

def pacman_game(c):
    leafNodes = [3, 6, 2, 3, 7, 1, 2, 0]
    treeDeapth = int(math.log(len(leafNodes), 2))
    darkMagicCost = c
    isMaximizer = True
    
    result = minMax(0, 0, isMaximizer, leafNodes, treeDeapth, darkMagicCost)
    
    if (result[2]):
        sideWent = "left"
    else:
        sideWent = "right"
        
    if (result[1]):
        doesOrDoesNot = "uses"
    else:
        doesOrDoesNot = "does not use"
        
    print(f"The new minimax value is {result[0]}. Pacman goes {sideWent} and {doesOrDoesNot} dark magic.")

darkMagicCost = int(input("Enter dark magic's cost: "))
pacman_game(darkMagicCost)






