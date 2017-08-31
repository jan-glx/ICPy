from unittest import TestCase

import numpy as np
import scipy.stats
from scipy.stats import chi2_contingency

import pertInv
from .. import simulation
from .. import ICP


class TestICP(TestCase):
    def test_zero_truncated_multipoisson(self):
        x = simulation.zero_truncated_multipoisson(3, 10000)
        y = np.random.poisson(3, 10000)
        y = y[y > 0]
        x = x[:len(y), 0]

        S = np.vstack((np.histogram(y, bins=10, range=(1, 11))[0],
                       np.histogram(x, bins=10, range=(1, 11))[0]))

        p_value = chi2_contingency(S)[1]
        self.assertGreater(p_value, 0.01)