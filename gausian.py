
def make_triangle(lst,k):
    for i in range(k,len(lst)-1):
        multiplyer = lst[i+1][k]
        for j in range(len(lst[i])):
            lst[i+1][j] -= (multiplyer/lst[k][k])*lst[k][j]

def shafal(lst,idx):
    for i in range(idx,len(lst)):
        if lst[i][idx] == 1:
            lst[i], lst[idx] = lst[idx], lst[i]
            break

def var_value(lst):
    j = lst[len(lst)-1]
    for i in range(len(lst)-2,-1,-1):
        if lst[i-1] != 0 and i != 0:
            j -= lst[i]
        else: 
            j = j/lst[i]
            return j

def solution(lst):
    for i in range(len(lst)-1):
        shafal(lst,i)
        make_triangle(lst,i)
    solu = []    
    for j in range(len(lst)-1,-1,-1):
        if solu == []:
            solu.append(var_value(lst[j]))
        else:
            for i in range(len(solu)):
                lst[j][len(lst)-1-i] *= solu[i]        
            solu.append(var_value(lst[j]))

    var = ['z','y','x','a','b','c','d','e']
    for i in range(len(solu)):    
        print (var[i],'=', solu[i],end=",  ")

lst = [[1,2,3,5],
    [2,5,3,3],   
    [1,0,8,17]]

solution(lst)



# -----------------------------testing--------------------------

# lst = [[1,-2,3,9],
#     [-1,3,0,-4],   
#     [2,-5,5,17]]


# z = 2.0,  y = -1.0,  x = 1.0,  
# lst = [[2,-2,3,2],
#     [1,2,-1,3],   
#     [3,-1,2,1]]
# z = 3.999999999999997,  y = 3.999999999999998,  x = -0.9999999999999991,  

# lst = [[1,1,1,3],
#     [2,3,7,0],   
#     [1,3,-2,17]]
# z = -2.0,  y = 4.0,  x = 1.0,  

# lst = [[1,3,2,2],
#     [2,7,7,-1],   
#     [2,5,2,7]]
# z = -2.0,  y = 1.0,  x = 3.0,  

