# -*- coding: utf-8 -*-

from __future__ import division, print_function

__all__ = []

import h5py
import numpy as np

nstar_petigura = 42557.0


def load_samples(filename):
    with h5py.File(filename, "r") as f:
        ln_p_bins = f["ln_period_bin_edges"][...]
        ln_r_bins = f["ln_radius_bin_edges"][...]
        tmp = f["ln_occurrence_rate_samples"][...]

    # Normalize by the number of stars that Petigura searched and zero pad the
    # rate array.
    ln_rate = -np.inf+np.zeros((len(tmp), len(ln_p_bins)+1, len(ln_r_bins)+1))
    ln_rate[:, 1:-1, 1:-1] = tmp - np.log(42557)

    return ln_p_bins, ln_r_bins, ln_rate


def get_ln_rate_density(samples, ln_p, ln_r):
    ln_p_bins, ln_r_bins, ln_rate = samples
    ix = np.digitize(np.atleast_1d(float(ln_p)), ln_p_bins)
    iy = np.digitize(np.atleast_1d(float(ln_r)), ln_r_bins)
    return ln_rate[:, ix, iy].flatten()


def get_ln_rate(samples, ln_p, ln_r, N=5000):
    lpmn, lpmx = ln_p
    lrmn, lrmx = ln_r
    ln_area = np.log(lpmx - lpmn) + np.log(lrmx - lrmn)

    # Numerically integrate the rate density.
    result = np.mean([np.exp(get_ln_rate_density(samples,
                             np.random.uniform(lpmn, lpmx),
                             np.random.uniform(lrmn, lrmx)))
                      for i in range(N)], axis=0)
    return np.log(result) + ln_area


if __name__ == "__main__":
    samples = load_samples("real/samples.h5")

    # Get the rate density at Earth.
    ln_gamma_earth = get_ln_rate_density(samples, np.log(365.25), np.log(1.0))
    q = np.exp(np.percentile(ln_gamma_earth, [16, 50, 84]))
    print("Gamma_Earth = {0} +{1[1]} -{1[0]}".format(q[1], np.diff(q)))

    # Get the rate integrated over a bin in ln-period and ln-radius.
    ln_rate = get_ln_rate(samples, [np.log(200), np.log(400)],
                          [np.log(1), np.log(2)])
    q = np.exp(np.percentile(ln_rate, [16, 50, 84]))
    print("Int[Gamma]_Earth = {0} +{1[1]} -{1[0]}".format(q[1], np.diff(q)))

    # Integrated over "habitable" giant planets.
    ln_rate = get_ln_rate(samples, [np.log(200), np.log(400)],
                          [np.log(2), np.log(32)])
    q = np.exp(np.percentile(ln_rate, [16, 50, 84]))
    print("Int[Gamma]_Giant = {0} +{1[1]} -{1[0]}".format(q[1], np.diff(q)))
