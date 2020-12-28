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
        Aset.append(packages[0])
        Bset.append(packages[1])
        Cset.append(packages[2])
        set = checkFormcNuggetCombo(number - packages[0] , Aset) 
        if set is not False :
            return set
        set = checkFormcNuggetCombo(number - packages[1] , Bset) 
        if set is not False :
            return set
        set = checkFormcNuggetCombo(number - packages[2] , Cset) 
        if set is not False :
            return set
    return False 

##Start iterations with 1
iterate = 1
resolved = False
#packages = (6,9,20)
#packages = (200,900,1200)
packages = (7,26,80)
checkCombo = []
#Results stored in the following lists
numberSet = []
solutionSet = []
#Iterate with each number to n
while not resolved :
    #Check if number has resolvable combo
    numberSet.append(iterate)
    checkCombo = checkFormcNuggetCombo(iterate,[])
    if checkCombo is not False:
        #If combo is greater than or equal packages smallest package then the problem is solved
        solutionSet.append(checkCombo)
        if len(solutionSet) >= packages[0] :
            print "Given package sizes",packages[0],",",packages[1],", and",packages[2],", the largest number of McNuggets that cannot be bought in exact quantity is: ", iterate - packages[0] 
            resolved = True 
    else :
        #If one of the consecutive sets isn't resolved, reset the combo
        solutionSet = []        
        numberSet = []
    iterate = iterate + 1
    if iterate >= 200 :
        print "No solution below 200"
        break


#Print resolved combinations for each checked quantity
print numberSet 
print solutionSet 

##TB 01
#checkCombo.append(checkFormcNuggetCombo(5,[]))
#print checkCombo 