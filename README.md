## ICPy
[![Build Status](https://travis-ci.com/jan-glx/ICPy.svg?branch=master)](https://travis-ci.com/jan-glx/ICPy) [![codecov](https://codecov.io/gh/jan-glx/ICPy/branch/master/graph/badge.svg)](https://codecov.io/gh/jan-glx/ICPy) [![PyPI version](https://badge.fury.io/py/ICPy.svg)](https://badge.fury.io/py/ICPy)

This packages provides a simple python implementation of Invariant Causal Prediction (ICP) [1].

See also the original implementation in the R package [InvariantCausalPrediction](https://cran.r-project.org/web/packages/InvariantCausalPrediction/index.html).
### Installation
``` bash
pip install ICPy
```
### Usage
``` python
import icpy as icpy
import numpy as np

np.random.seed(seed=1)
n = 100
noise = 0.1
E = np.repeat([0, 1, 2], np.ceil(n / 3.0))[0:n]
A = np.random.normal(scale=noise, size=[n]) + np.equal(E, 1)
B = A + np.random.normal(scale=noise, size=[n]) / 3 + np.equal(E, 2)
C = B + np.random.normal(scale=noise, size=[n])
icpy.invariant_causal_prediction(X=np.column_stack((A, B)), y=C, z=E)
```
Output

```
ICP(S_hat=array([1], dtype=int64), 
    p_values=array([  1.51508232e-01,   4.59577055e-37]), 
    p_value=0.16416488336322549)
```

### News
v0.0.003 (2020-05-15)
* fix failing import (thanks to [@lgmoneda](https://github.com/lgmoneda), [#1](https://github.com/jan-glx/ICPy/pull/1))
* fix issues when environments are not subsequent whole numbers starting at 0 (thanks to [@lgmoneda](https://github.com/lgmoneda), [#1](https://github.com/jan-glx/ICPy/pull/1))

### References
[1] J. Peters, P. Bühlmann, N. Meinshausen, Causal inference by using invariant prediction: identification and confidence intervals, J. R. Stat. Soc. Ser. B Stat. Methodol. 78 (2016) 947-1012. doi:10.1111/rssb.12167.
