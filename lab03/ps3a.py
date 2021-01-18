from string import *

def countSubStringMatch(target,key):
    done = False
    index = 0
    count = 0
    while not done:
        #print "Iterate", count
        loc = find(target,key,index)
        if loc is -1:
            done = True
        else:
            count = count + 1
            index = loc + 1

    return count

def countSubStringMatchRecursive (target, key):
    loc = find(target,key)
    #print target
    if loc is -1:
        return 0 
    else:
        sum = countSubStringMatchRecursive(target[loc+len(key):],key) + 1
        return sum


#print countSubStringMatch("atgacatgcacaagtatgcat","atgc")
print countSubStringMatchRecursive("atgacatgcacaagtatgcat","atgc")