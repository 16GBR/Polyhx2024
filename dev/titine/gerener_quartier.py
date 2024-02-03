# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt

#theta est en degres, superficie en m^2
def centeredAngledElliptic(theta, eccentricite, superficie):
    theta = np.radians(theta)
    #print(theta)
    phi = np.arange(0, 2*np.pi, 0.00001)
    a = (superficie/(np.pi*(1-eccentricite**2)**(1/2)))**(1/2)
    b = a*(1-eccentricite**2)**(1/2)
    
    r = b / (1-(eccentricite**2)*(np.cos(phi)**2))**(1/2)
    
    x = r*np.cos(phi)*np.cos(theta) - r*np.sin(phi)*np.sin(theta)
    y = r*np.sin(phi)*np.cos(theta) + r*np.cos(phi)*np.sin(theta)
    
    return x, y, a, b, superficie 

theta, eccentricite, superficie = 120, 0.95, 45000
x, y, a, b, superficie = centeredAngledElliptic(theta, eccentricite, superficie)

plt.plot(x, y, "-r")
plt.xlim(-1*a, a)
plt.ylim(-1*a, a)
plt.axhline(ls=":", c="k")
plt.axvline(ls=":", c="k")
#plt.show()