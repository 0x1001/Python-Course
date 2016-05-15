import unittest
import timeit
import rsa


class TestRSA(unittest.TestCase):
    def test_rsa_small(self):
        m = 1234

        n = 3233
        e = 17
        d = 2753

        c = rsa.rsa_encode(m, n, e)
        decoded_m = rsa.rsa_decode(c, n, d)

        self.assertEqual(m, decoded_m)

    def test_rsa_big(self):
        m = 10

        n = 1872701
        e = 3581
        d = 135221

        c = rsa.rsa_encode(m, n, e)
        decoded_m = rsa.rsa_decode(c, n, d)

        self.assertEqual(m, decoded_m)

    def test_optimized_rsa_small(self):
        m = 1234

        n = 3233
        e = 17
        d = 2753

        c = rsa.rsa_optimized_encode(m, n, e)
        decoded_m = rsa.rsa_optimized_decode(c, n, d)

        self.assertEqual(m, decoded_m)

    def test_optimized_rsa_big(self):
        m = 123456

        n = 1872701
        e = 3581
        d = 135221

        c = rsa.rsa_optimized_encode(m, n, e)
        decoded_m = rsa.rsa_optimized_decode(c, n, d)

        self.assertEqual(m, decoded_m)

    def test_optimized_rsa_very_big(self):
        m = 1976620216402300889624482718775150

        n = 145906768007583323230186939349070635292401872375357164399581871019873438799005358938369571402670149802121818086292467422828157022922076746906543401224889672472407926969987100581290103199317858753663710862357656510507883714297115637342788911463535102712032765166518411726859837988672111837205085526346618740053
        e = 65537
        d = 89489425009274444368228545921773093919669586065884257445497854456487674839629818390934941973262879616797970608917283679875499331574161113854088813275488110588247193077582527278437906504015680623423550067240042466665654232383502922215493623289472138866445818789127946123407807725702626644091036502372545139713

        c = rsa.rsa_optimized_encode(m, n, e)
        decoded_m = rsa.rsa_optimized_decode(c, n, d)

        self.assertEqual(m, decoded_m)

    def test_execution_time_compare(self):
        m = 10

        n = 1872701
        e = 3581
        d = 135221

        t1 = timeit.Timer(lambda: rsa.rsa_decode(rsa.rsa_encode(m, n, e), n, d)).timeit(1)
        t2 = timeit.Timer(lambda: rsa.rsa_optimized_decode(rsa.rsa_optimized_encode(m, n, e), n, d)).timeit(1)

        self.assertGreaterEqual(t1, t2)
