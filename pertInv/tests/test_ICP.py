from unittest import TestCase
import numpy as np

import pertInv

class TestICP(TestCase):
    def test_runs(self):
        n = 100
        p = 4
        E = np.random.randint(3, size=[n])
        E_ = np.zeros([n,p], dtype=np.bool)
        E_[:,E] = True
        X = np.random.normal(size=[n,p])
        X = X.dot(np.random.normal(size=[p,p])) + E_
        beta = np.array([1,-2,0,0])
        y = X.dot(beta)
        X[:,3] += y
        try:
            s = pertInv.invariant_causal_prediction(X,y,E)
        except:
            self.fail("invariant_causal_prediction() raised an exception unexpectedly!")