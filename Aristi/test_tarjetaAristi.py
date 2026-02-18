import logica_tarjeta
import unittest

class testCalculoCuotaTArjeta(unittest.TestCase):
    def test_normal_1(self):
        #Definir datos de entrada
        compra = 200_000
        tasa = 3.1/100
        plazo = 36

        #Realizar el proceso
        cuotaCalculada = logica_tarjeta.calcular_cuota(compra, tasa, plazo)
        abonoCalculado = logica_tarjeta.calcular_abonos(compra, tasa, plazo)
        interesCalculado = logica_tarjeta.calcular_interes()
    

        #Datos esperadaos a la salida 
        cuotaEsperada = 9297.96
        total_abonos = 334_726.53
        total_interes = 134_726.53

        #Verificar la salida
        self.assertAlmostEqual(cuotaCalculada, cuotaEsperada, 2)

    def test_tasaCero(self):
        compra = 480_000
        interes = 0
        plazo = 48

        cuotaCalculada = logica_tarjeta.calcular_cuota(compra, interes, plazo)

        self.assertEqual(cuotaCalculada, 10_000)


if __name__ == "__main__":
    unittest.main()
