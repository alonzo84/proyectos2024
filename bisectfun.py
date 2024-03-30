import numpy as np

def bisect(f,a,b,tol):
#we will do the first iterate before our while loop starts so that we
#have a value to test against the tolerance
    x = (a+b)/2
    while np.abs(f(x))>tol:
        print('a={:.5f} f(a)={:.5f}, b={:.5f} f(b)={:.5f}, x={:.5f} f(x)={:.5f}'.format(a,f(a),b,f(b),x,f(x)))
        #now decide whether we replace a or b with x
        if f(a)*f(x) < 0:
            #root is between a and x so replace b
            b = x
        elif f(b)*f(x)<0:
            # root is between b and x so replace a
            a = x
        else:
            # in this case, f(x) must be 0 and we have found the root
            # so we will know the root value is x and we can end the loop
            break
    #recompute the approximation
        x = (a+b)/2
    return x

def shifted_exp(x):
    y = np.exp(x) - 3
    return y

tol = 0.0001
a = 1
b = 2
#x = bisect(shifted_exp,a,b,tol)
#print('final x =',x)
#print('final f(x) =',shifted_exp(x))