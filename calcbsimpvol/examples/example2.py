from calcbsimpvol import calcbsimpvol
import numpy as np


def calcbsimpvol_example_2(verbose=False):
    P = [[59.14, 34.21, 10.17, 16.12, 40.58],
        [58.43, 33.59, 10.79, 17.47, 41.15],
        [57.87, 33.16, 11.363, 18.63, 41.74],
        [57.44, 32.91, 11.90, 19.58, 42.27]]
    P = np.asarray(P)
    S = np.asarray(100)
    K = np.arange(40, 160, 25)
    tau = np.arange(0.25, 1.01, 0.25)
    K, tau = np.meshgrid(K, tau)
    cp = np.hstack((np.ones((4, 3)), -1 * np.ones((4, 2))))  # [Calls[4, 3], Puts[4, 2]]

    r = 0.01 * np.ones((4, 5)) * np.asarray([1.15, 1.10, 1.05, 1]).reshape((4, 1))
    q = 0.03 * np.ones((4, 5)) * np.asarray([1.3, 1.2, 1.1, 1]).reshape((4, 1))

    sigma = calcbsimpvol(dict(cp=cp, P=P, S=S, K=K, tau=tau, r=r, q=q))
    if verbose:
        print(sigma)
    return sigma


if __name__ == '__main__':
    result = calcbsimpvol_example_2(verbose=True)
