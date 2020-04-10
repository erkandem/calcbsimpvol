
[![Build Status](https://travis-ci.com/erkandem/calcbsimpvol.svg?token=EM8YQfR9wuLvQFQzBZ5o&branch=master)](https://travis-ci.com/erkandem/calcbsimpvol)
![](https://img.shields.io/badge/License-MIT-blue.svg)
![](https://img.shields.io/badge/Python-3.4%20%7C%203.5%20%7C%203.6%20%7C%203.7%20%7C%203.8%20%7C%20PyPy3-blue.svg)
[![](https://img.shields.io/badge/PyPi-v1.14.0-blue.svg)](https://pypi.org/project/calcbsimpvol/)

# calcbsimpvol

*Calculate Black-Scholes Implied Volatility - Vectorwise*

----------------------

* `:)` native python code
* `:)` lightweight footprint
* `:)` sample data included
* `:(` not suited for single / low number of options
* `:(` code reads un-pythonic
* `:(` not yet thoroughly tested

## Getting started

### Requirements

* Python 3.x (currently) or PyPy3
* NumPy
* SciPy
* (MatPlotLib to visualize results in some examples)

###  Installation

While the code consists of single digit functions,
I recommend using the `pip install` way to get the code.
That way you would take advantage of bug fixes, updates,
and possible extensions.

```bash
$ pip install calcbsimpvol
```

### Example

Pass your `args` bundled in a `dict`.

```python
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

# [[      nan,       nan,  0.20709362, 0.21820954, 0.24188675],
# [       nan, 0.22279836, 0.20240934, 0.21386148, 0.23738982],
# [       nan, 0.22442837, 0.1987048 , 0.21063506, 0.23450013],
# [       nan, 0.22188111, 0.19564657, 0.20798285, 0.23045406]]

```

More usage examples are available in [example3.py](https://github.com/erkandem/calcbsimpvol) 
(additional sample data required which is  available at [GitHub Repo](https://github.com/erkandem/calcbsimpvol)

## Performance
```
Design a test. 
Get the results you want.
```

* `k_max = 10` (default) 
* `tolerance = 10E-12` (default)
* linear regression steps are commented out (default)

```bash
# assuming you did install it already
git clone https://github.com/erkandem/calcbsimpvol.git
cd calcbsimpvol
python examples/example3.py --steps 100 --mode reference
```


* 15 µs per option
* 41 ms per surface

tested with 3.6, 3.7 and PyPy3
```bash
matlab -nodisplay -nosplash -nodesktop -r "run('mlb_reference_example.m');"
```

* 12 µs per option
* 34 ms per surface 


Obviously, these values are per core (i5 4210U 1.7 GHz).


## Notes
Good Python code reads like a novel. Right? So should math.
I preferred short math-like variable names in this case.
That makes the code less readable compared to other Python code 
but the docstrings should make up for the lack of readability.

Originally, I left the camelCase function name and spelling in place but eventually got annoyed.
> calcbsimpvol it is


## Code Origin

* first thought of by Li (2006) (see References)
* implemented and published by Mark Whirdy as MATLAB .m-code (see References)
* numpyified from `.m` to `.py` by me


## Contact
* email: [erkan.dem@pm.me](mailto:erkan.dem@pm.me)
* documentation: [erkandem.github.io/calcbsimpvol/](https://erkandem.github.io/calcbsimpvol/)
* source: [github.com/erkandem/calcbsimpvol](https://github.com/erkandem/calcbsimpvol)
* issues: [github.com/erkandem/calcbsimpvol/issues](https://github.com/erkandem/calcbsimpvol/issues)

## ToDos
* make the code compatible with `Python 2`
* make it `PyPy` compatible



## References
1)  Li, 2006, "You Don't Have to Bother Newton for Implied Volatility"

    [http://papers.ssrn.com/sol3/papers.cfm?abstract_id=952727](http://papers.ssrn.com/sol3/papers.cfm?abstract_id=952727)

2)  MATLAB source code available at:

    [https://www.mathworks.com/matlabcentral/fileexchange/41473-calcbsimpvol-cp-p-s-k-t-r-q](https://www.mathworks.com/matlabcentral/fileexchange/41473-calcbsimpvol-cp-p-s-k-t-r-q)

## License
The included Python code is licensed under `MIT` [License](https://github.com/calcbsimpvol/calcbsimpvol/LICENCE)

The Code by Mark Whirdy is licensed under `MIT` [License](https://github.com/erkandem/calcbsimpvol/calcBSImpVol_mlab/LICENSE)

The translation is not related or endorsed by the original author.
