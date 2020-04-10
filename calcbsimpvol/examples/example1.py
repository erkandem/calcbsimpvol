import numpy as np
from calcbsimpvol import calcbsimpvol


def calcbsimpvol_example_1(verbose=False):
    S = np.asarray(100)
    K_value = np.arange(40, 160, 25)
    K = np.ones((np.size(K_value), 1))
    K[:, 0] = K_value
    tau_value = np.arange(0.25, 1.01, 0.25)
    tau = np.ones((np.size(tau_value), 1))
    tau[:, 0] = tau_value
    r = np.asarray(0.01)
    q = np.asarray(0.03)
    cp = np.asarray(1)
    P = [[59.35, 34.41, 10.34, 0.50, 0.01],
        [58.71, 33.85, 10.99, 1.36, 0.14],
        [58.07, 33.35, 11.50, 2.12, 0.40],
        [57.44, 32.91, 11.90, 2.77, 0.70]]

    P = np.asarray(P)
    [K, tau] = np.meshgrid(K, tau)

    sigma = calcbsimpvol(dict(cp=cp, P=P, S=S, K=K, tau=tau, r=r, q=q))
    if verbose:
        print(sigma)
    return sigma


if __name__ == '__main__':
    result = calcbsimpvol_example_1(verbose=True)
