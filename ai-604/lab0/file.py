def cube(n):
    return (n*n*n)

def factorial(n):
    if(n<0):
        print('negative, cannot compute')
        return
    y = 1
    for x in range(1,n+1):
        y = x*y
    return (y)

def count_pattern(pattern,lst):    
    count = 0
    for i in range(len(lst)-len(pattern)+1):        
        if lst[i:i+len(pattern)] == pattern:
            count = count + 1
    return count


# print (count_pattern( ('a', 'b'), ('a','b', 'c', 'e', 'b', 'a', 'b', 'f')))
# print (cube(2))
# print (factorial(4))
# print (factorial(-4))
# print (count_pattern(('a', 'b', 'a'), ('g','a','b','a','b', 'a','b','a')))

# One way to measure the complexity of a mathematical expression is the depth of the expression
# describing it in Python lists. Write a program that finds the depth of an expression.


# def depth(lst):
#     return_depth = 0
#     if isinstance(lst, (list, tuple)):
#         return_depth = 1
#     else:
#         return 0
#     for i in range(len(lst)): 
#         new_depth = return_depth
#         if isinstance(lst[i], (list, tuple)):            
#             depth_of_item = depth(lst[i])
#             if(depth_of_item > 1):
#                 new_depth = new_depth + depth_of_item
#             else:
#                 new_depth = return_depth + 1
#             # print('check depth', lst[i],depth(lst[i]))
#         if new_depth > return_depth:
#             return_depth = new_depth
    
#     return return_depth

# def depth(lst):
#     return_depth = 0
#     if isinstance(lst, (list, tuple)):
#         items_with_tuple = [item for item in range(len(lst)) if isinstance(lst[item], (list, tuple))]
#         for j in range(len(items_with_tuple)):            
#             items_with_tuple[j] = lst[items_with_tuple[j]]        
#         if len(items_with_tuple) == 0:
#             return 1
        
#         while len(items_with_tuple) > 0:
#             items_copy = items_with_tuple
#             items_with_tuple = [item for item in range(len(items_with_tuple)) if isinstance(items_with_tuple[item], (list, tuple))]                
#             for j in range(len(items_with_tuple)):            
#                 items_with_tuple[j] = items_copy[items_with_tuple[j]]            
#             print(items_with_tuple)
#             return_depth = return_depth + 1
#             # items_with_tuple
#         return return_depth
#     else:
#         return return_depth

def depth(lst):
    if not isinstance(lst, (list,tuple)):
        return 0
    sum = 1
    for i in range(len(lst)):
        if isinstance(lst[i], (list,tuple)):            
            new_sum = depth(lst[i]) + 1
            if new_sum > sum:
                sum = new_sum
    return sum

print (depth('x'))
print (depth(('expt', 'x', 2)))
print (depth(('+', ('expt', 'x', 2), ('expt', 'y', 2))))
print (depth(('/', ('expt', 'x', 5), ('expt', ('-', ('expt', 'x', 2), 1), ('/', 5, 2)))))
print (depth(('/', ('expt', 'x', 5,8), ('expt', ('-', ('expt', 'x', ('2',('2')),2), 1), ('/', 5, 2)))))
print (depth((1,(1,2,(3,4),(6,7,('8',1),1),9))))

def tree_ref(tree, input):    
    if type(input) is not tuple:
        return 'Location not found'
    elif len(input) == 1:
        return tree[input[0]]
    else:
        return tree_ref(tree[input[0]], input[1:])

tree = (((1, 2), 3), (4, (5, 6)), 7, (8, 9, 10))
# print ( tree_ref(tree, (3,1)) )
# print ( tree_ref(tree, (1, 1, 1)) )
# print ( tree_ref(tree, (0,)) )
