Exoplanet population inference
==============================

These are the data and results from the recently submitted paper "Exoplanet
population inference and the abundance of Earth analogs from noisy, incomplete
catalogs" by Daniel Foreman-Mackey, David W. Hogg, and Timothy Morton.

This archive contains the catalogs of exoplanets (both simulated and real)
used in the analysis and a thinned set of posterior samples generated in the
MCMC analysis. A binned representation of the empirical detection efficiency
function computed using the simulated results from Petigura et al. (2013) is
also included for the sake of completeness ;-).

See the paper for more details.

Products
--------

The HDF5 file `completeness.h5` gives the empirical detection efficiency
computed on a fine grid in (ln-)period and (ln-)radius. The bin edges are
given in the datasets `ln_period_bin_edges` and `ln_radius_bin_edges`. The
dataset `ln_completeness` gives the natural logarithm of the empirical
detection efficiency for *transiting* planets. The dataset `ln_detect_eff` is
the same but it takes the geometric transit probability into account. Both
grids of detection efficiency are padded with a ring of `-infinity` because
the prior detection efficiency is exactly zero outside of the searched range.

The data and results for the simulated catalogs and real catalog are given in
the directories `simulated/*` and `real` respectively. Each directory has two
files: `catalog.txt` and `samples.h5`. The catalog file is the dataset and it
lists the given posterior measurements of period (measured in days), radius
(measured in Earth radii), and radius uncertainty for each candidate. The
samples file give the posterior samples for the *True* occurrence rate density
modeled as a set of bin heights. As above, the `*_bin_edges` datasets give the
bin definitions. The `ln_occurrence_rate_samples` dataset gives a list of
samples from the posterior probability for the log-bin heights. This list was
generated using the method described in the paper and then thinned by the
shortest integrated autocorrelation time of the parameters. Finally, the
`hyperparameter_samples` dataset gives the corresponding list of
hyperparameter samples. In the notation of the paper, the columns give "mu",
"lambda_0", "lambda_P", and "lambda_R", respectively.

License
-------

These data are being publicly shared under the terms of the Creative Commons
Attribution license (v4.0; http://creativecommons.org/licenses/by/4.0/). If
you make use of these data, please cite the paper.

[![DOI](https://zenodo.org/badge/doi/10.5281/zenodo.11507.png)](http://dx.doi.org/10.5281/zenodo.11507)
