import os
import fitsio
import numpy as np

dtype = [("PER", np.float64), ("RAD", np.float64), ("RAD_UNCERT", np.float64)]
units = ["days", "Earth radii", "Earth radii"]

for d in ("real", "simulated/catalog-a", "simulated/catalog-b"):
    data = np.loadtxt(os.path.join(d, "catalog.txt"))
    table = np.array(zip(*(data.T)), dtype=dtype)
    fitsio.write(os.path.join(d, "catalog.fits"), table, clobber=True,
                 units=units)
