# most of this code I found on the internet
# sorry, but it was some time ago, i don't remember the sources

def derivative(f, x, h, *args):
    return (f(x+h,args) - f(x-h,args)) / (2.0*h)  # might want to return a small non-zero if ==0
    
def solve(f, x0, h, *args):
    lastX = x0
    nextX = lastX + 10* h  # "different than lastX so loop starts OK
    while (abs(lastX - nextX) > h):  # this is how you terminate the loop - note use of abs()
        newY = f(nextX,args)  # just for debug... see what happens
        print "f(", nextX, ") = ", newY     # print out progress... again just debug
        lastX = nextX
        nextX = lastX - newY / derivative(f, lastX, h, args)  # update estimate using N-R
    return nextX

def func1(x,*args):    # change this function to whatever you want to get the zero
    return x**2+5*x+2

if __name__ == "__main__":
    x0=2
    h = .0001    #desired precision
    res = solve(func1, x0, h)
    print res
