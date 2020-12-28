#Description : This script should be able to recursively solve the Diapholese problem

#Recursive function checks if provided number can be broken into a combination of quantities (6,9,20)
def checkFormcNuggetCombo(number,set):
    if number < 0 :
        return False 
    elif number == 0 :
        return set 
    else :
        Aset = list(set)
        Bset = list(set)
        Cset = list(set)
        Aset.append(6)
        Bset.append(9)
        Cset.append(20)
        set = checkFormcNuggetCombo(number - 6 , Aset) 
        if set is not False :
            return set
        set = checkFormcNuggetCombo(number - 9 , Bset) 
        if set is not False :
            return set
        set = checkFormcNuggetCombo(number - 20 , Cset) 
        if set is not False :
            return set
    return False 

##Start iterations with 1
iterate = 1
resolved = False
checkCombo = []
numberSet = []
solutionSet = []
#Iterate with each number to n
while not resolved :
    #Check if number has resolvable combo
    numberSet.append(iterate)
    checkCombo = checkFormcNuggetCombo(iterate,[])
    if checkCombo is not False:
        #If combo is greater than or equal 6 consecutive sets then the problem is solved
        solutionSet.append(checkCombo)
        if len(solutionSet) >= 6 :
            print "Largest number of McNuggets that cannot be bought in exact quantity: ", iterate - 6 
            resolved = True 
    else :
        #If one of the consecutive sets isn't resolved, reset the combo
        solutionSet = []        
        numberSet = []
    iterate = iterate + 1


#Print resolved combinations for each checked quantity
print numberSet 
print solutionSet 

##TB 01
#checkCombo.append(checkFormcNuggetCombo(5,[]))
#print checkCombo 