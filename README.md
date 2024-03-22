## ICPy
[![CI](https://github.com/jan-glx/ICPy/actions/workflows/ci.yml/badge.svg)](https://github.com/jan-glx/ICPy/actions/workflows/ci.yml) [![Coverage badge](https://raw.githubusercontent.com/jan-glx/ICPy/python-coverage-comment-action-data/badge.svg)](https://htmlpreview.github.io/?https://github.com/jan-glx/ICPy/blob/python-coverage-comment-action-data/htmlcov/index.html)
[![PyPI version](https://img.shields.io/pypi/v/ICPy.svg)](https://pypi.org/project/ICPy/)

This packages provides a simple python implementation of Invariant Causal Prediction (ICP) [1].<br>
The source code for the actual algorithm resides in [./src/icp/ICP.py](./src/icpy/ICP.py). <br>
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
E = np.repeat([0, 1, 2], np.ceil(n / 3.0))[0:n]                       # "Environment"
A = np.random.normal(scale=noise, size=[n]) + np.equal(E, 1)          # Node A
B = A + np.random.normal(scale=noise, size=[n]) / 3 + np.equal(E, 2)  # Node B
C = B + np.random.normal(scale=noise, size=[n])                       # Node C

#  /--->---\
# E -> A -> B -> C

icpy.invariant_causal_prediction(X=np.column_stack((A, B)), y=C, z=E) # test if A or B are parents of C
```
Output

``` python
ICP(S_hat=array([1], dtype=int64),                         # Column 1 = Node B was (correctly) identified as parent of C
    p_values=array([  1.51508232e-01,   4.59577055e-37]),  # error levels at which A and B would/are indentied as parent of C
    p_value=0.16416488336322549)                           # p-value for testing against violation of the model assumptions (e.g. a direct effect of E on C)
```

### News
v0.0.003 (2020-05-15)
* fix failing import (thanks to [@lgmoneda](https://github.com/lgmoneda), [#1](https://github.com/jan-glx/ICPy/pull/1))
* fix issues when environments are not subsequent whole numbers starting at 0 (thanks to [@lgmoneda](https://github.com/lgmoneda), [#1](https://github.com/jan-glx/ICPy/pull/1))

### References
[1] J. Peters, P. Bühlmann, N. Meinshausen, Causal inference by using invariant prediction: identification and confidence intervals, J. R. Stat. Soc. Ser. B Stat. Methodol. 78 (2016) 947-1012. doi:10.1111/rssb.12167.
