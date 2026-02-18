import math

alpha = 2.5
beta = 5

def distance(x, y):
    length = math.sqrt(x**2 + y**2)
    return length

def increment(alpha):
    alpha += 1
    return alpha

def double():
    # declara variable como global para poder modificarla
    global beta
    beta *= 2

print( distance(3, 4) )
print( increment( alpha ) )
print( double() )
print('alpha = ', alpha)
print('beta = ', beta)
print('length = ', length)
