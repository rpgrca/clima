import unittest
from climabuilder import ClimaBuilder
from clima import Clima
from pronostico import Pronostico

class SistemaTests(unittest.TestCase):
    def test_con_el_sistema_completo_deberia_funcionar(self):
        # Arrange
        clima = (
            ClimaBuilder().con_apikey("b6907d289e10d714a6e88b30761fae2")
                          .con_ciudad("London")
                          .en_pais("uk")
                          .con_servicio("https://samples.openweathermap.org/data/2.5/weather")
                          .build()
        )

        # Act
        pronostico = clima.obtener()

        # Assert
        self.assertIsNotNone(pronostico)
        self.assertEqual(clima.ciudad, pronostico.ciudad)
        self.assertEqual((51.51, -0.13), pronostico.coordenadas)
        self.assertEqual("Drizzle", pronostico.titulo)
        self.assertEqual("light intensity drizzle", pronostico.descripcion)
        self.assertEqual(280.32, pronostico.temperatura)
        self.assertEqual(279.15, pronostico.temperatura_minima)
        self.assertEqual(281.15, pronostico.temperatura_maxima)
        self.assertEqual("GB", pronostico.pais)

if __name__ == "__main__":
    unittest.main()
