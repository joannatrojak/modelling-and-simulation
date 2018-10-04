import random as r
import math as m

def monteCarloSimulation(n):
    counter = 0
    #loop generating points
    for i in range(1, n):
        x2 = r.random()**2
        y2 = r.random()**2
        #increment if inside unit circle
        if m.sqrt(x2 + y2) < 1.0:
            counter += 1

    #approximation of pi
    return 4*(counter/n)

print(monteCarloSimulation(40000))
    
