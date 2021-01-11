from string import *

def subStringMatchExact(target,key):
    done = False
    index = 0
    count = 0
    locTuple = ()
    strTuple = ()
    while not done:
        loc = find(target,key,index)
        if loc is -1:
            done = True
        else:
            locTuple = locTuple + (loc,)
            strTuple = strTuple + (target[loc:],)
            count = count + 1
            index = loc + 1

    print strTuple
    return locTuple 

#Couldn't find way to implement recursively. Problem with unchangeable items in Tuples
#def subStringMatchExact(target, key):
#    loc = find(target,key)
#    #print target
#    if loc is -1:
#        return 
#    else:
#        sTuple = subStringMatchExact(target[loc+len(key):],key)
#        if sTuple is None :
#            sTuple = (loc,)
#        else :
#            for x in sTuple :
#
#            sTuple = (loc,) + sTuple
#            #sTuple = (str(loc), str(loc + sTuple))
#        return sTuple 

#print subStringMatchExact("atgacatgcacaagtatgcatatgcatgcsdfasfdsaatgc","atgc")
target1 = 'atgacatgcacaagtatgcat' 
target2 = 'atgaatgcatggatgtaaatgcag'
key10 = 'a' 
key11 = 'atg' 
key12 = 'atgc' 
key13 = 'atgca'
keys = (key10,key11,key12,key13)
for key in keys:
    print "Target1: KEY -> " + str(key)
    print subStringMatchExact(target1,key)
    print "Target2: KEY -> " + str(key)
    print subStringMatchExact(target2,key)
