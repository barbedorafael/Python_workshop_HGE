import numpy as np
import pandas as pd
from datetime import datetime,timedelta

def read_mgb_binary_as_dataframe(filebin, nt, nc, dstart):
    """ Read full binary (MGB format) as dataframe """

    # read from file
    #'<f4' indicates little-endian (<) float(f) 4 byte (4)
    dados = np.fromfile(filebin,'<f4').reshape(nt,nc)

    # make timeseries dataframe
    times = [dstart + timedelta(days=i) for i in range(nt)]
    df = pd.DataFrame(dados, columns=range(1,nc+1), index=times)
    
    return df