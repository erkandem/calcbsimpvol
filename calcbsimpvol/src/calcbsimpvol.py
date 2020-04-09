from scipy.special import erf
# it is common to use `import numpy as np`
# but what don't you do to save 3 characters ...
from numpy import (
    # --- logical
    any,
    bitwise_not,
    logical_and,

    # --- constants / data type
    nan,
    pi,
    ndarray,

    # --- creation
    asarray,
    zeros,
    ones,
    full,

    # --- ops
    absolute,
    shape,
    size,
    maximum,
    log,
    exp,
    sqrt,
    sum,

    # --- juggling
    reshape
)


def calcbsimpvol(arg_dict):
    """
    calculates implied volatility surface or smile. Translated from MATLAB code.
    As it is a bare-metal package I would suggest to write an adapter class to feed the function.

    Args:
        arg_dict(dict):
        cp  (ndarray):  int.....Call = [+1], Put = [-1]...[m x n] or [1 x 1]
        P   (ndarray):  float...Option Price Matrix...[m x n]
        S   (ndarray):  float...Underlying Price...[1 x 1]
        K   (ndarray):  float...Strike Price...[m x n]
        tau (ndarray):  float...Time to Expiry in Years...[m x n]
        r   (ndarray):  float...Continuous Risk-Free Rate...[m x n] or [1 x 1]
        q   (ndarray):  float...Continuous Dividend Yield...[m x n] or [1 x 1]

    Returns:
        - **iv** (ndarray) – float...The Implied Volatility...[m x n]

    Examples:
        This is the first example which is also included separate file within
        the examples folder.

    .. code-block:: python

        from calcbsimpvol import calcbsimpvol
        import numpy as np
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
        print(sigma)
        # [[       nan,        nan, 0.20709362, 0.21820954, 0.24188675],
        # [       nan, 0.22279836, 0.20240934, 0.21386148, 0.23738982],
        # [       nan, 0.22442837, 0.1987048 , 0.21063506, 0.23450013],
        # [       nan, 0.22188111, 0.19564657, 0.20798285, 0.23045406]]


    .. code-block:: python

        #%% Plotting the results
        from mpl_toolkits.mplot3d import Axes3D
        import matplotlib.pyplot as plt
        m = np.log(S/K)
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        ax.scatter(m, tau, sigma)
        ax.set_xlabel('log Moneyness')
        ax.set_ylabel('Time Until Expiry')
        ax.set_zlabel('implied Volatility [% p.a.]')
        plt.show()


    This is the second example which is also included separate file within
    the examples folder.


    .. code-block:: python

        from calcbsimpvol import calcbsimpvol
        import numpy as np
        P = [[59.14, 34.21, 10.17, 16.12, 40.58],
        [58.43, 33.59, 10.79, 17.47, 41.15],
        [57.87, 33.16, 11.363, 18.63, 41.74],
        [57.44, 32.91, 11.90, 19.58, 42.27]]
        P = np.asarray(P)
        S = np.asarray(100)
        K = np.arange(40, 160, 25)
        tau = np.arange(0.25, 1.01, 0.25)
        K, tau = np.meshgrid(K, tau)
        cp = np.hstack((np.ones((4, 3)), -1 * np.ones((4, 2))))  # [Calls[4,3], Puts[4,2]]
        r = 0.01 * np.ones((4, 5)) * np.asarray([1.15, 1.10, 1.05, 1]).reshape((4, 1))
        q = 0.03 * np.ones((4, 5)) * np.asarray([1.3, 1.2, 1.1, 1]).reshape((4, 1))
        sigma = calcbsimpvol(dict(cp=cp, P=P, S=S, K=K, tau=tau, r=r, q=q))
        print(sigma)
        # [[0.27911614, 0.23659105, 0.20714849, 0.21834553, 0.24225733],
        # [0.2797917 , 0.2315275 , 0.20249323, 0.21436123, 0.23823301],
        # [0.27436779, 0.22679618, 0.1987485 , 0.21097384, 0.23450519],
        # [0.26918174, 0.22235213, 0.19572994, 0.20807133, 0.2310324 ]]


    .. code-block:: python

        #%% Plotting the results
        from mpl_toolkits.mplot3d import Axes3D  # noqa: F401 unused import
        import matplotlib.pyplot as plt
        m = np.log(S/K)
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        ax.scatter(m, tau, sigma)
        ax.set_xlabel('log Moneyness')
        ax.set_ylabel('Time Until Expiry')
        ax.set_zlabel('implied Volatility [% p.a.]')
        plt.show()


    References:
        1)  Li, 2006, "You Don't Have to Bother Newton for Implied Volatility"
          http://papers.ssrn.com/sol3/papers.cfm?abstract_id=952727
        2)  http://en.wikipedia.org/wiki/Householder's_method
        3)  http://en.wikipedia.org/wiki/Greeks_(finance)
        4)  https://www.mathworks.com/matlabcentral/fileexchange/41473-calcbsimpvol-cp-p-s-k-t-r-q

    """
    # rather have a dict or class instead of seven variables
    feed_keys = ['cp', 'P', 'S', 'K', 'tau', 'r', 'q']
    for key in feed_keys:
        if type(arg_dict[key]) is not ndarray:
            arg_dict[key] = asarray(arg_dict[key])
        # convert to column vector
        if len(shape(arg_dict[key])) == 1 and key is not 'S':
            arg_dict[key] = reshape(arg_dict[key], (size(arg_dict[key]), 1))

    # create short pointers/variables for data inside arg_dict
    cp = arg_dict['cp']
    P = arg_dict['P']
    S = arg_dict['S']
    K = arg_dict['K']
    tau = arg_dict['tau']
    r = arg_dict['r']
    q = arg_dict['q']

    gh = shape(P)
    g = gh[0]
    h = gh[1]

    # for simplicity reasons a risk free rate and or dividend yield can be
    # supplied as a scalar value or previously modeled and supplied as an array / vector
    if size(r) == 1:
        r = r * ones((g, h))
    if size(q) == 1:
        q = q * ones((g, h))
    if size(cp) == 1:
        cp = cp * ones((g, h))

    p = asarray([-0.969271876255, 0.097428338274, 1.750081126685])
    m_values = [
        6.268456292246,
        -6.284840445036,
        30.068281276567,
        -11.780036995036,
        -2.310966989723,
        -11.473184324152,
        -230.101682610568,
        86.127219899668,
        3.730181294225,
        -13.954993561151,
        261.950288864225,
        20.090690444187,
        -50.117067019539,
        13.723711519422
    ]

    m = ones((g, h, 14))
    for zetta in range(14):
        m[:, :, zetta] = ones((g, h)) * m_values[zetta]

    n_values = [
        -0.068098378725,
        0.440639436211,
        -0.263473754689,
        -5.792537721792,
        -5.267481008429,
        4.714393825758,
        3.529944137559,
        -23.636495876611,
        -9.020361771283,
        14.749084301452,
        -32.570660102526,
        76.398155779133,
        41.855161781749,
        -12.150611865704
    ]

    n = ones((g, h, 14))
    for zetta in range(14):
        n[:, :, zetta] = ones((g, h)) * n_values[zetta]

    i_values = [0, 1, 0, 1, 2, 0, 1, 2, 3, 0, 1, 2, 3, 4]
    i = ones((g, h, 14))
    for zetta in range(14):
        i[:, :, zetta] = ones((g, h)) * i_values[zetta]

    j_values = [1, 0, 2, 1, 0, 3, 2, 1, 0, 4, 3, 2, 1, 0]
    j = ones((g, h, 14))
    for zetta in range(14):
        j[:, :, zetta] = ones((g, h)) * j_values[zetta]

    P[cp == -1] = P[cp == -1] + S * exp(-q[cp == -1] * tau[cp == -1]) - K[cp == -1] * exp(-r[cp == -1] * tau[cp == -1])
    P = maximum(P, 0)

    c_values = P / (S * exp(-q * tau))
    x_values = log(S * exp((r - q) * tau) / K)

    c = ones((shape(c_values)[0], shape(c_values)[1], 14))
    x = ones((shape(x_values)[0], shape(x_values)[1], 14))

    for zetta in range(shape(x)[2]):
        x[:, :, zetta] = x_values
        c[:, :, zetta] = c_values

    v1_fixed = _fcnv(p, m, n, i, j, x, maximum(c, 0))  # D- Domain (x < 1)
    v2_fixed = _fcnv(p, m, n, i, j, -x, maximum(exp(x) * c + 1 - exp(x), 0))  # D+ Domain (x > 1)

    v = zeros((g, h))
    v[x[:, :, 0] <= 0] = v1_fixed[x[:, :, 0] <= 0]
    v[x[:, :, 0] > 0] = v2_fixed[x[:, :, 0] > 0]

    # Domain-of-Approximation is x = {-0.5, +0.5}, v = {0, 1}, x/v = {-2, 2}
    domain_filter = logical_and(
        logical_and(logical_and(x[:, :, 0] >= -0.5, x[:, :, 0] <= 0.5), logical_and(v > 0, v < 1)),
        logical_and((x[:, :, 0] / v) <= 2, (x[:, :, 0] / v) >= -2))

    not_domain = bitwise_not(domain_filter)
    v[not_domain] = 0.8
    sigma = v / sqrt(tau)

    # Householder's root-finder
    k_max = 10
    tolerance = asarray(1e-12)

    sigma = sigma.flatten()
    P = P.flatten()
    S = S.flatten()
    K = K.flatten()
    tau = tau.flatten()
    r = r.flatten()
    q = q.flatten()

    C = full((shape(P)), True, dtype=bool)
    s = _core(P, S, K, tau, r, q, sigma, C)

    e = s['obj']
    C = absolute(e) > tolerance
    k = 1

    while logical_and(any(C), k <= k_max):

        s = _core(P, S, K, tau, r, q, sigma, C)
        numerator = (6 * e[C] * s['vega'] ** 2 + 3 * e[C] ** 2 * s['vomma'])
        denominator = (-6 * s['vega'] ** 3 - 6 * e[C] * s['vega'] * s['vomma'] - e[C] ** 2 * s['ultima'])

        sigma[C] = sigma[C] - (numerator / denominator)
        s = _core(P, S, K, tau, r, q, sigma, C)
        e[C] = s['obj']

        C = absolute(e) > tolerance
        k = k + 1

    sigma[C] = nan
    sigma = reshape(sigma, (g, h))
    return sigma


def _core(P, S, K, tau, r, q, sigma, C):
    """ calculation part, takes  ndarrays (column vector)
    S: float, scalar
    P,  K, tau, r, q, sig:  float, [n x 1]
    C: boolean, [n x 1]

    """
    denominator = (sigma[C] * sqrt(tau[C]))
    d1 = (log(S / K[C]) + (r[C] - q[C] + sigma[C] ** 2 * 0.5) * (tau[C])) / denominator
    d2 = (log(S / K[C]) + (r[C] - q[C] - sigma[C] ** 2 * 0.5) * (tau[C])) / denominator

    fcnN_d1 = _fcnN(d1)
    fcnN_d2 = _fcnN(d2)

    fcnn_d1 = _fcnn(d1)
    fcnn_d2 = _fcnn(d2)

    call = exp(-q[C] * tau[C]) * S * fcnN_d1 - exp(-r[C] * tau[C]) * K[C] * fcnN_d2
    obj = (P[C] - call)

    vega = S * exp(-q[C] * (tau[C])) * fcnn_d1 * (sqrt(tau[C]))
    vomma = vega * d1 * d2 / sigma[C]
    ultima = -1 * vega * (d1 * d2 * (1 - d1 * d2) + d1 ** 2 + d2 ** 2) / (sigma[C] ** 2)

    return {
        'd1': d1,
        'd2': d2,
        'fcnN_d1': fcnN_d1,
        'fcnN_d2': fcnN_d2,
        'fcnn_d1': fcnn_d1,
        'fcnn_d2': fcnn_d2,
        'call': call,
        'obj': obj,
        'vega': vega,
        'vomma': vomma,
        'ultima': ultima
    }


def _fcnv(p, m, n, i, j, x, c):
    """  Eq. (19), Li (2006) """
    return p[0] * x[:, :, 0] + p[1] * sqrt(c[:, :, 0]) + p[2] * c[:, :, 0] + (
        sum(n * ((x ** i) * (sqrt(c) ** j)), 2)) / (1 + sum(m * ((x ** i) * (sqrt(c) ** j)), 2))


def _fcnN(x):
    """cumulative density function (cdf) of normal distribution """
    return 0.5 * (1. + erf(x / sqrt(2)))


def _fcnn(x):
    """probability density function (pdf) of normal distribution """
    return exp(-0.5 * x ** 2) / sqrt(2 * pi)

