import xarray as xr
import numpy as np
from scipy import signal, stats


def smooth_butter(data, order=8):
    b, a = signal.butter(order, 0.125)
    y = signal.filtfilt(b, a, data, padlen=150)
    return y


def smooth_temp_solar(temperature, solar, order = 8):
    smooth_temp = np.zeros(temperature.shape)
    
    for i in range(0,temperature.shape[1]):
        for j in range(0, temperature.shape[2]):
            smooth_temp[:,i,j] = smooth_butter(temperature[:,i,j], order)
    
    smooth_solar = smooth_butter(solar, order)

    return smooth_temp, smooth_solar
