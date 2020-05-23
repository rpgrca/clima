import unittest
from unittest.mock import patch
from ddt import ddt, data, unpack
from climabuilder import ClimaBuilder
from clima import Clima

@ddt
class ClimaUnitTests(unittest.TestCase):
    def test_constructor_con_una_apikey_valida_deberia_incorporarla(self):
        apikey = "abcdefg"

        sut = ClimaBuilder().con_apikey(apikey).build()

        self.assertEqual(apikey, sut.apikey)

    def test_constructor_con_una_apikey_vacia_deberia_lanzar_valueerror(self):
        with self.assertRaises(ValueError) as ve:
            sut = ClimaBuilder().con_apikey("").build()

    def test_constructor_con_una_apikey_en_blanco_deberia_lanzar_valueerror(self):
        with self.assertRaises(ValueError) as ve:
            sut = ClimaBuilder().con_apikey("    ").build()

    def test_constructor_con_none_deberia_lanzar_valueerror(self):
        with self.assertRaises(ValueError) as ve:
            sut = ClimaBuilder().con_apikey(None).build()

    def test_constructor_con_ciudad_valida_deberia_incorporarla(self):
        ciudad = "London"
        apikey = "abcdefg"

        sut = ClimaBuilder().con_apikey(apikey).con_ciudad(ciudad).build()
        self.assertEqual(ciudad, sut.ciudad)

    @data(None, -11, 0, 10, 2172797)
    def test_constructor_con_cualquier_id_deberia_incorporarlo(self, cualquier_id: int):
        # Arrange
        cualquier_id = id

        # Act
        sut = ClimaBuilder().con_apikey("abcdefg").con_id(cualquier_id).build()

        # Assert
        self.assertEqual(cualquier_id, sut.id)

    @data(None, "", "ar", "uy")
    def test_constructor_con_cualquier_pais_deberia_incorporarlo(self, cualquier_pais: str):
        # Act
        sut = ClimaBuilder().con_apikey("abcdefg").en_pais(cualquier_pais).build()

        # Assert
        self.assertEqual(cualquier_pais, sut.pais)

    @data(None, "", "13233")
    def test_constructor_con_cualquier_codigo_postal_deberia_incorporarlo(self, cualquier_cp: str):
        # Act
        sut = ClimaBuilder().con_apikey("abcdefg").en_codigo_postal(cualquier_cp).build()

        # Assert
        self.assertEqual(cualquier_cp, sut.codigo_postal)

    def test_constructor_con_cualquier_coordenadas_deberia_incorporarlo(self):
        # Arrange
        latitud, longitud = (34.6037, 58.3816)

        # Act
        sut = ClimaBuilder().con_apikey("abcdefg").en_coordenadas(latitud, longitud).build()

        # Assert
        self.assertEqual((latitud, longitud), sut.coordenadas)

    @data(None, "", "sp")
    def test_constructor_con_cualquier_idioma_deberia_incorporarlo(self, cualquier_idioma: str):
        # Act
        sut = ClimaBuilder().con_apikey("abcdefg").en_idioma(cualquier_idioma).build()

        # Assert
        self.assertEqual(cualquier_idioma, sut.idioma)

    def test_constructor_con_fahrenheit_deberia_incorporarlo(self):
        # Act
        sut = ClimaBuilder().con_apikey("abcdefg").en_fahrenheit().build()

        # Assert
        self.assertEqual("fahrenheit", sut.grados)

    def test_constructor_con_celsius_deberia_incorporarlo(self):
        # Act
        sut = ClimaBuilder().con_apikey("abcdefg").en_celsius().build()

        # Assert
        self.assertEqual("celsius", sut.grados)

    def test_constructor_con_kelvin_deberia_incorporarlo(self):
        # Act
        sut = ClimaBuilder().con_apikey("abcdefg").en_kelvin().build()

        # Assert
        self.assertEqual("kelvin", sut.grados)

    @data(
        ( 2172797, None, None, None, (None, None), "", "fahrenheit", "http://api.openweathermap.org/data/2.5/weather?appid=abcdefg&id=2172797&units=imperial" ),
        ( None, "Sydney", "au", None, (None, None), "fr", "kelvin", "http://api.openweathermap.org/data/2.5/weather?appid=abcdefg&q=Sydney,au&lang=fr" ),
        ( None, None, None, None, (34.6037, 58.3816), "es", "celsius", "http://api.openweathermap.org/data/2.5/weather?appid=abcdefg&lat=34.6037&lon=58.3816&lang=es&units=metric" ),
        ( None, None, None, "94040", (None, None), "ja", "fahrenheit", "http://api.openweathermap.org/data/2.5/weather?appid=abcdefg&zip=94040&lang=ja&units=imperial" ),
        ( None, None, "ar", "94040", (None, None), "ja", "fahrenheit", "http://api.openweathermap.org/data/2.5/weather?appid=abcdefg&zip=94040,ar&lang=ja&units=imperial" )
    )
    @unpack
    def test_url_con_datos_deberia_crear_url(self, id: int, ciudad: str, pais: str, cp: str, coordenadas: (float, float), idioma: str, grados: str, url: str):
        # Arrange
        apikey = "abcdefg"
        url_servicio = "http://api.openweathermap.org/data/2.5/weather"

        # Act
        clima = Clima(apikey, id, ciudad, pais, cp, coordenadas, idioma, grados, url_servicio)

        # Assert
        self.assertEqual(url, clima.url)

    def test_constructor_con_ciudad_codigo_postal_coordenadas_id_nulas_deberia_lanzar_valueerror(self):
        # Arrange
        apikey = "abcdefg"
        url_servicio = "http://api.openweathermap.org/data/2.5/weather"

        # Act / Assert
        with self.assertRaises(ValueError) as ve:
            sut = Clima(apikey, None, None, None, None, None, None, None, url_servicio)

    def test_constructor_con_latitud_o_longitud_nulas_y_ninguna_otra_locacion_deberia_lanzar_valueerror(self):
        # Arrange
        apikey = "abcdefg"
        url_servicio = "http://api.openweathermap.org/data/2.5/weather"

        # Act / Assert
        with self.assertRaises(ValueError) as ve:
            sut = Clima(apikey, None, None, None, None, (None, None), None, None, url_servicio)

    @data(None, "", "    ")
    def test_constructor_con_un_url_servicio_invalido_deberia_lanzar_valueerror(self, url_servicio: str):
        with self.assertRaises(ValueError) as ve:
            sut = ClimaBuilder().con_apikey("abcdefg").con_servicio(url_servicio).build()

    def test_obtener_con_el_objeto_creado_deberia_obtener_json(self):
        # Arrange
        respuesta = '{"coord":{"lon":-0.13, "lat":51.51}, "weather":[{"id":300, "main":"Drizzle", "description":"light intensity drizzle", "icon":"09d"}], "base":"stations", "main":{"temp":280.32, "pressure":1012, "humidity":81, "temp_min":279.15, "temp_max":281.15}, "visibility":10000, "wind":{"speed":4.1, "deg":80}, "clouds":{"all":90}, "dt":1485789600, "sys":{"type":1, "id":5091, "message":0.0103, "country":"GB", "sunrise":1485762037, "sunset":1485794875}, "id":2643743, "name":"London", "cod":200}'

        with patch.object(Clima, "_get_server_data", return_value=respuesta) as mock_method:
            clima = (
                ClimaBuilder().con_apikey("abcdefg")
                              .con_ciudad("London")
                              .en_pais("uk")
                              .con_servicio("http://api.openweathermap.org/data/2.5/weather")
                              .build()
            )

            # Act
            pronostico = clima.obtener()

            # Assert
            self.assertIsNotNone(pronostico)
            self.assertEqual(clima.ciudad, pronostico.ciudad)

if __name__ == "__main__":
    unittest.main()
