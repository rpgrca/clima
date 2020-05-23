import unittest
import json
from ddt import ddt, data
from pronostico import Pronostico

@ddt
class PronosticoUnitTests(unittest.TestCase):
    def test_constructor_con_json_valido_deberia_incorporarlo(self):
        # Arrange
        json_data = json.loads('{"coord":{"lon":-0.13, "lat":51.51}, "weather":[{"id":300, "main":"Drizzle", "description":"light intensity drizzle", "icon":"09d"}], "base":"stations", "main":{"temp":280.32, "pressure":1012, "humidity":81, "temp_min":279.15, "temp_max":281.15}, "visibility":10000, "wind":{"speed":4.1, "deg":80}, "clouds":{"all":90}, "dt":1485789600, "sys":{"type":1, "id":5091, "message":0.0103, "country":"GB", "sunrise":1485762037, "sunset":1485794875}, "id":2643743, "name":"London", "cod":200}')

        # Act
        pronostico = Pronostico(json_data, "fahrenheit")

        # Assert
        self.assertIsNotNone(pronostico)
        self.assertEqual("London", pronostico.ciudad)
        self.assertEqual((51.51, -0.13), pronostico.coordenadas)
        self.assertEqual("Drizzle", pronostico.titulo)
        self.assertEqual("light intensity drizzle", pronostico.descripcion)
        self.assertEqual(280.32, pronostico.temperatura)
        self.assertEqual(279.15, pronostico.temperatura_minima)
        self.assertEqual(281.15, pronostico.temperatura_maxima)
        self.assertEqual("GB", pronostico.pais)


    def test_constructor_con_json_nulo_deberia_lanzar_valueerror(self):
        with self.assertRaises(ValueError) as ve:
            sut = Pronostico(None, "fahrenheit")

    @data(("kelvin", "K"), ("fahrenheit", "F"), ("celsius", "C"))
    def test___str__con_json_valido_deberia_generar_oracion(self, grados: (str, str)):
        # Arrange
        json_data = json.loads('{"coord":{"lon":-0.13, "lat":51.51}, "weather":[{"id":300, "main":"Drizzle", "description":"light intensity drizzle", "icon":"09d"}], "base":"stations", "main":{"temp":280.32, "pressure":1012, "humidity":81, "temp_min":279.15, "temp_max":281.15}, "visibility":10000, "wind":{"speed":4.1, "deg":80}, "clouds":{"all":90}, "dt":1485789600, "sys":{"type":1, "id":5091, "message":0.0103, "country":"GB", "sunrise":1485762037, "sunset":1485794875}, "id":2643743, "name":"London", "cod":200}')
        pronostico = Pronostico(json_data, grados[0])

        # Act
        resultado = str(pronostico)

        # Result
        self.assertEqual(f"London (GB) currently has light intensity drizzle with a temperature of 280.32{grados[1]}.", resultado);

if __name__ == "__main__":
          unittest.main()
