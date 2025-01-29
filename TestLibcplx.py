import Libreria_Cuantica as lc
import unittest

class TestCplxOperation(unittest.TestCase):
    
    def test_cplxsum(self):
        suma_1 = lc.sumacplx((5.2, 3), (2, -3.5)) # Prueba 1
        self.assertAlmostEqual(suma_1[0], 7.2)
        self.assertAlmostEqual(suma_1[1], -0.5)
        
        suma_2 = lc.sumacplx((5, -3), (-4, -7)) # Prueba 2
        self.assertAlmostEqual(suma_2[0], 1)
        self.assertAlmostEqual(suma_2[1], -10)
        
    def test_cplxresta(self):
        resta_1 = lc.restacplx((5, -3), (-4, -7)) # Prueba 1
        self.assertAlmostEqual(resta_1[0], 9)
        self.assertAlmostEqual(resta_1[1], 4)
        resta_2 = lc.restacplx((5.2, 3), (2, -3.5)) # Prueba 2
        self.assertAlmostEqual(resta_2[0], 3.2)
        self.assertAlmostEqual(resta_2[1], 6.5)
        
    def test_cplxmult(self):
        mult_1 = lc.multcplx((5.2, 3), (2, -3.5)) # Prueba 1
        self.assertAlmostEqual(mult_1[0], 20.9)
        self.assertAlmostEqual(mult_1[1], -12.2)
        mult_2 = lc.multcplx((5, -3), (-4, -7)) # Prueba 2
        self.assertAlmostEqual(mult_2[0], -41)
        self.assertAlmostEqual(mult_2[1], -23)
        
    def test_cplxdiv(self):
        div_1 = lc.divcplx((5.2, 3), (2, -3.5)) # Prueba 1
        self.assertAlmostEqual(div_1[0], -0.0061538)
        self.assertAlmostEqual(div_1[1], 1.48923076)
        div_2 = lc.divcplx((5, -3), (-4, -7)) # Prueba 2
        self.assertAlmostEqual(div_2[0], (1/65))
        self.assertAlmostEqual(div_2[1], (47/65))
        
    def test_cplxmod(self):
        mod_1 = lc.modcplx((1, 5)) # Prueba 1
        self.assertAlmostEqual(mod_1, (26) ** (1/2))
        mod_2 = lc.modcplx((5, -3)) # Prueba 2
        self.assertAlmostEqual(mod_2, (34) ** (1/2))
        
    def test_cplxconj(self):
        conj_1 = lc.conjcplx((1, 5)) # Prueba 1
        self.assertAlmostEqual(conj_1[0], 1)
        self.assertAlmostEqual(conj_1[1], -5)
        conj_2 = lc.conjcplx((5, -3)) # Prueba 2
        self.assertAlmostEqual(conj_2[0], 5)
        self.assertAlmostEqual(conj_2[1], 3)
if __name__ == "__main__":
    unittest.main()