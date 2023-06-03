import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
from numpy import sqrt
import scipy.constants as const
from scipy.optimize import curve_fit                        # Funktionsfit:     popt, pcov = curve_fit(func, xdata, ydata) 
from uncertainties import ufloat                            # Fehler:           fehlerwert =  ulfaot(x, err)
from uncertainties import unumpy as unp 
from uncertainties.unumpy import uarray                     # Array von Fehler: fehlerarray =  uarray(array, errarray)
from uncertainties.unumpy import (nominal_values as noms,   # Wert:             noms(fehlerwert) = x
                                  std_devs as stds)  



uH = ufloat(0.582,0.241)
uPara = ufloat(7.4667,2.7325)

print(uH-uPara)

ueloon = ufloat(34, 5.83)

ufloon = ufloat(5986.00, 77.37)

def Aktivität(N,t):
    return N/t

print('Aktivität luftleerer Ballon', Aktivität(ueloon,60))
print(Aktivität(ueloon,60)-uH)

print('Aktivität aufgeblasener Ballon', Aktivität(ufloon,300))
print(Aktivität(ufloon,300)-uH)
