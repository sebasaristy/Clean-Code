import unittest
import logica_tarjeta

class TestCalculoCuotaTarjeta(unittest.TestCase):
    
    def test_normal_1(self):
        compra = 200_000
        interes = 0.031
        plazo = 36
        
        cuota_calculada = logica_tarjeta.calcular_cuota(compra, interes, plazo)
        
        cuota_esperada = 9297.96
        
        self.assertAlmostEqual(cuota_calculada,cuota_esperada,2)
        
    def test_tasa_cero(self):
        compra = 480_000        
        interes = 0
        plazo = 48
        
        cuota_calculada = logica_tarjeta.calcular_cuota(compra, interes, plazo)
        
        self.assertEqual(cuota_calculada, 10000)
        
        
if __name__ == '__main__':
    unittest.main()