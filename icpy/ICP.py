import itertools as it
from collections import namedtuple

import numpy as np
import scipy.stats
import sklearn.linear_model


def all_parent_sets(S, max_num_parents):
    return it.chain.from_iterable(
        it.combinations(S, n_parents) for n_parents in range(min(len(S), max_num_parents) + 1))


def f_test(x1, x2):
    """
    Perform F-test for equal variance.
    """
    F = np.var(x1, ddof=1) / np.var(x2, ddof=1)
    return 2 * min(scipy.stats.f.cdf(F, len(x1) - 1, len(x2) - 1), scipy.stats.f.sf(F, len(x1) - 1, len(x2) - 1))


def test_plausible_parent_set(X, y, z):
    n_e = len(np.unique(z))
    environments = np.unique(z)
    lm = sklearn.linear_model.LinearRegression(fit_intercept=False)
    X_with_intercept = np.hstack((X, np.ones((X.shape[0], 1))))
    lm.fit(X_with_intercept, y)
    residuals = lm.predict(X_with_intercept) - y

    return min([2 * min(scipy.stats.ttest_ind(residuals[np.equal(z, e)],
                                              residuals[np.logical_not(np.equal(z, e))],
                                              equal_var=False).pvalue,
                        f_test(residuals[np.equal(z, e)],
                               residuals[np.logical_not(np.equal(z, e))]))
                for e in environments]) * n_e


def preselect_parents(X, y, n):
    _, selected, _ = sklearn.linear_model.lars_path(X, y, method='lasso', max_iter=n, return_path=False)
    return selected


ICP = namedtuple("ICP", ["S_hat", "q_values", "p_value"])


def invariant_causal_prediction(X, y, z, alpha=0.1):
    """
    Perform Invariant Causal Prediction.

    Not yet implemented.

    Parameters
    ----------
    X : (n, p) ndarray
        predictor variables
    y : (n,) ndarray
        target variable, numpy array of shape `(n)`
    Z : array_like
        index of environment, length(Z)==`n`
    alpha : float
        Confidence level of the tests and FDR to control. P(\hat{S} \subset S^*) \gte 1-`alpha`

    Returns
    -------
    list
        The identified causal parent set, \hat{S}, as list of indices

    """

    n = X.shape[0]
    p = X.shape[1]

    max_num_parents = 8

    S_0 = list(range(p))
    q_values = np.zeros(p)
    p_value_model = 0

    for S in all_parent_sets(S_0, max_num_parents):
        not_S = np.ones(p, np.bool)
        not_S[list(S)] = False
        p_value = test_plausible_parent_set(X[:, S], y, z)
        q_values[not_S] = np.maximum(q_values[not_S], p_value)
        p_value_model = max(p_value_model, p_value)

    q_values = np.minimum(q_values, 1)
    S_hat = np.where(q_values <= alpha)[0]
    return ICP(S_hat, q_values, p_value_model)
