import numpy as np
import matplotlib.pyplot as plt
import corner
import h5py

# load GWTC-1 posterior for GW170817
# from here: https://gwosc.org/eventapi/html/GWTC-1-confident/GW170817/v3/
f = h5py.File('../data/GW170817_GWTC-1.hdf5', 'r')
dataset = f['IMRPhenomPv2NRT_lowSpin_posterior']
breakpoint()
cosi = dataset['costheta_jn']
dist = dataset['luminosity_distance_Mpc']

corner.corner(np.vstack((cosi, dist)).T)
# plt.show()
