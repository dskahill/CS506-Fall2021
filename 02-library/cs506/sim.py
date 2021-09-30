def euclidean_dist(x, y):
    res = 0
    for i in range(len(x)):
        res += (x[i] - y[i])**2
    return res**(1/2)

def manhattan_dist(x, y):
    res =  0
    for i in range(len(x)):
        v = (x[i] - y[i])
        if v < 0:
            res += v * (-1)
        else:
            res += v
    return res 

def jaccard_dist(x, y):
    inter = set(x and y)
    card = len(inter)
    union = set(x or y)
    cardu = len(union)
    if inter == 0:
        return 0
    if cardu == 0:
        return 'undefined'
    
    j = card/cardu
    
    return 1-j
    

def cosine_sim(x, y):
    dot = 0
    for i in x:
        dot += x[i]*y[i]
    
    xlen = 0
    ylen = 0
    for i in x:
        xlen += x[i]**2
        ylen += y[i]**2
    xlen = xlen**(1/2)
    ylen = ylen**(1/2)
    cross = xlen * ylen
    if cross == 0:
        return 'undefined'
    else:    
        return dot / cross
     
# Feel free to add more
