from unittest import TestCase

import numpy as np
import scipy.stats

import pertInv
from .. import ICP


class TestICP(TestCase):
    def test_runs(self):
        n = 100
        p = 4
        E = np.random.randint(3, size=[n])
        E_ = np.zeros([n, p], dtype=np.bool)
        E_[:, E] = True
        X = np.random.normal(size=[n, p])
        X = X.dot(np.random.normal(size=[p, p])) + E_
        beta = np.array([1, -2, 0, 0])
        y = X.dot(beta)
        X[:, 3] += y
        try:
            s = pertInv.invariant_causal_prediction(X, y, E)
        except:
            self.fail("invariant_causal_prediction() raised an exception unexpectedly!")

    def test_simple(self):
        n = 100
        p = 3
        noise = 0.1
        E = np.repeat([0, 1, 2], np.ceil(n / 3.0))[0:n]
        A = np.random.normal(scale=noise, size=[n]) + np.equal(E, 1)
        B = A + np.random.normal(scale=noise, size=[n]) / 3 + np.equal(E, 2)
        C = B + np.random.normal(scale=noise, size=[n])
        S_hat, q_values, _ = pertInv.invariant_causal_prediction(X=np.column_stack((A, B)), y=C, z=E)
        np.testing.assert_array_equal(S_hat, np.array([1]))

    def test_very_simple_R(self):
        E = np.array([0, 1, 2, 0, 1, 2, 0, 1, 2, 0])
        X = np.array([[-0.13, 1.02, 0.09, -0.08, 1.03, -0.06, -0.02, 1.02,
                       -0.03, -0.17], [-0.08, 0.97, 1.08, -0.05, 1.03, 0.84, -0.06, 1.15,
                                       1, 0.03]]).T
        y = np.array([-0.15, 1.06, 1.15, -0.07, 0.96, 0.84, -0.27, 1.09, 0.88, 0.11])
        _, q_values, _ = pertInv.invariant_causal_prediction(X, y, z=E)
        np.testing.assert_array_almost_equal(q_values, [1, 0.0005721278])

    def test_size(self):
        n = 10
        p = 3
        noise = 0.1
        alpha = 0.1

        def one():
            E = np.repeat([0, 1, 2], np.ceil(n / 3.0))[0:n]  # np.random.randint(3, size=[n]);
            A = np.random.normal(scale=noise, size=[n]) + np.equal(E, 1)
            B = A + np.random.normal(scale=noise, size=[n]) / 3 + np.equal(E, 2)
            C = B + np.random.normal(scale=noise, size=[n])
            S_hat, q_values, _ = pertInv.invariant_causal_prediction(X=np.column_stack((A, B)), y=C, z=E, alpha=alpha)
            return 0 in S_hat

        N = 100
        K = sum((one() for _ in range(N)))
        p_value = scipy.stats.binom_test(K, N, alpha, alternative="greater")
        self.assertGreater(p_value, 0.01)

    # class TestHelper(TestCase):
    def test_parent_set_generator(self):
        self.assertEqual(tuple(ICP.all_parent_sets(range(3), 2)), ((), (0,), (1,), (2,), (0, 1), (0, 2), (1, 2)))

    def tes_f_test(self):
        x = np.array([-0.0125254538334171, 0.0365808106496997, -0.152432057452361, 0.132189787940119])
        y = np.array(
            [0.110799906961932, 0.0775142028334219, -0.0517966484888954, 0.0169115436825457, -0.0472594541962366,
             -0.109982638096806])
        self.assertAlmostEquals(ICP.f_test(x, y), 0.4719577)
