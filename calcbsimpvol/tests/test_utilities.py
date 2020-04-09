"""
# list of test to be created

# Variables
# T - expiry date
# t_0 - observation date
# tau - time to expiry = (T - t_0) / 365
# q - continious dividend yield
# r - continious risk free rate

## test equity index
# q(tau), r(tau)
### a) matrix-wise (surface)
### b) vector wise (single expiry)

### I) dividend paying
### II) non dividend paying


## test futures contracts
# q(tau) == r(tau)
### b) vector wise (single expiry)
"""
import pytest
from scipy.stats import norm
from calcbsimpvol.src import _fcnN, _fcnn


@pytest.mark.parametrize(
    'x', [point / 10 for point in range(-5 * 10, -5 * 10, 1)]
)
def test__fcnN(x):
    assert _fcnN(x) == pytest.approx(norm.cdf(x), rel=0.000000000001)


@pytest.mark.parametrize(
    'x', [point / 10 for point in range(-5 * 10, 5 * 10, 1)]
)
def test__fcnn(x):
    assert _fcnn(x) == pytest.approx(norm.pdf(x), rel=0.000000000001)

