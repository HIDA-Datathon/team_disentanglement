import xarray as xr
import numpy as np
from scipy import signal, stats

def smooth_butter(data, order):
    b, a = signal.butter(order, 0.125)
    y = signal.filtfilt(b, a, data, padlen=150)
    return y

def Smoothed_Temp_Solar(Temperature, Solar, order = 8):
    smooth_Temp = np.zeros(Temperature.shape)
    
    for i in range(0,Temperature.shape[1]):
        for j in range(0, Temperature.shape[2]):
            smooth_Temp[:,i,j] = smooth_butter(Temperature[:,i,j], order)
    
    smooth_solar = smooth_butter(Solar, order)

    return smooth_Temp, smooth_solar