

def invariant_causal_prediction(X, y, z, alpha):
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

    raise NotImplementedError()
    return