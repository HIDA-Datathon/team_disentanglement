# The Paleo Climate Challenge &ndash; Team Disentanglement
In this repository, you can find our code from the [Paleo Climate Challenge](https://helmholtz.tubcloud.tu-berlin.de/s/EEGrkWTJDoHE9r6#pdfviewer) HIDA datathon. We tried to disentangle volcanic from solar activities based on temperature data from the first 1000 years AD (via model simulations). Take a look at our [presentation](Presentation.pdf) to get an overview of our work.

## Installation
1. To execute the code in this repository, install [Conda](https://docs.conda.io/en/latest/) and execute the following commands:
    ```
    conda create --name disentanglement python=3.8
    pip install -r code/requirements.txt
    conda install -c conda-forge xarray netCDF4
    conda install -c conda-forge cartopy
    conda install -c conda-forge ipywidgets
    conda install nodejs
    jupyter labextension install @jupyter-widgets/jupyterlab-manager
    jupyter labextension install jupyterlab-plotly
    jupyter labextension install plotlywidget
    ```
2. Download the [data](ftp://ftp.hzg.de/outgoing/swagner/MyChallengePaleo.tar.gz) and make them accessible by setting the `DATA_PATH` environment variable (see [`code/settings.py`](code/settings.py) for details).
