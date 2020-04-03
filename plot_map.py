import cartopy.crs as ccrs
import cartopy
import xarray as xr
import matplotlib.cm as cm
import matplotlib.pyplot as plt
import numpy as np
from cartopy.util import add_cyclic_point
from mpl_toolkits.axes_grid1.axes_divider import make_axes_locatable


def plot_map(data, title='', colorbar_title='', cmap=cm.Spectral_r):
    assert len(data.shape) == 2, 'Only 2D data can be plotted on the map'

    plt.rcParams['font.size'] = 16

    # Retrieve lot and long values from data file
    ds_temp_r1 = xr.open_dataset('../data/T2m_R1_ym_1stMill.nc')
    lats = ds_temp_r1.variables['lat'][:]
    lons = ds_temp_r1.variables['lon'][:]

    # Make data continuous so that no white line appears in the middle (adds the lon=360° point)
    data, lons = add_cyclic_point(data, coord=lons)

    fig, ax = plt.subplots(1, 1, figsize=(16, 20))

    n_different_values = len(np.unique(data))
    if n_different_values <= 10:
        # Discrete case
        levels = n_different_values - 1
        cmap = plt.cm.get_cmap('tab10', n_different_values)
    else:
        # Continuous case
        levels = 100

    # Plot world map
    ax = plt.axes(projection=ccrs.PlateCarree())
    cs = plt.contourf(lons, lats, data, levels, transform=ccrs.PlateCarree(), cmap=cmap)

    ax.coastlines()
    ax.set_title(title)

    # Add colorbar
    divider = make_axes_locatable(ax)
    cax = divider.new_horizontal(size="5%", pad=0.1, axes_class=plt.Axes)
    fig.add_axes(cax)

    cbar = fig.colorbar(cs, cax=cax)
    cbar.ax.get_yaxis().labelpad = 10
    cbar.ax.set_ylabel(colorbar_title)

    plt.close()

    return fig
