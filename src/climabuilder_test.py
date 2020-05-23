import unittest
from unittest.mock import patch
from ddt import ddt, data, unpack
from clima import Clima
from climabuilder import ClimaBuilder

@ddt
class ClimaBuilderUnitTests(unittest.TestCase):

    @data(None, "", "  ", "abcdefg")
    def test_con_apikey_con_cualquier_apikey_deberia_incorporarla(self, cualquier_apikey: str):
        # Arrange / Act
        builder = ClimaBuilder().con_apikey(cualquier_apikey)

        # Assert
        self.assertEqual(cualquier_apikey, builder.apikey)

    @data(None, "", "  ", "abcdefg")
    def test_con_ciudad_con_cualquier_ciudad_deberia_incorporarla(self, cualquier_ciudad: str):
        # Arrange / Act
        builder = ClimaBuilder().con_ciudad(cualquier_ciudad)

        # Assert
        self.assertEqual(cualquier_ciudad, builder.ciudad)

    @data(None, "", "  ", "abcdefg")
    def test_en_pais_con_cualquier_pais_deberia_incorporarlo(self, cualquier_pais: str):
        # Arrange / Act
        builder = ClimaBuilder().en_pais(cualquier_pais)

        # Assert
        self.assertEqual(cualquier_pais, builder.pais)

    @data(None, "", "  ", "abcdefg")
    def test_en_codigo_postal_con_cualquier_codigo_postal_deberia_aceptarlo(self, cualquier_codigo_postal: str):
        # Arrange / Act
        builder = ClimaBuilder().en_codigo_postal(cualquier_codigo_postal)

        # Assert
        self.assertEqual(cualquier_codigo_postal, builder.codigo_postal)

    @data((0, 0), (-1, 10), (13, -1), (-8, -6))
    @unpack
    def test_en_coordenadas_con_cualquier_coordenada_deberia_incorporarla(self, cualquier_latitud: float, cualquier_longitud: float):
        # Arrange
        cualquier_coordenada = (cualquier_latitud, cualquier_longitud)
        builder = ClimaBuilder()

        # Act
        builder = builder.en_coordenadas(cualquier_latitud, cualquier_longitud)

        # Assert
        self.assertEqual(cualquier_coordenada, builder.coordenadas)

    def test_en_fahrenheit_con_fahrenheit_flag_deberia_incorporarlo(self):
        # Arrange
        builder = ClimaBuilder()

        # Act
        builder = builder.en_fahrenheit()

        # Assert
        self.assertEqual("fahrenheit", builder.grados)

    def test_en_celsius_con_celsius_flag_deberia_incorporarlo(self):
        # Arrange
        builder = ClimaBuilder()

        # Act
        builder.en_celsius()

        # Assert
        self.assertEqual("celsius", builder.grados)

    def test_en_kelvin_con_kelvin_flag_deberia_incorporarlo(self):
        # Arrange
        builder = ClimaBuilder()

        # Act
        builder.en_kelvin()

        # Assert
        self.assertEqual("kelvin", builder.grados)

    @data(-33, 0, 1, 10, 1000)
    def test_con_id_con_cualquier_id_deberia_incorporarlo(self, cualquier_id: int):
        # Arrange
        builder = ClimaBuilder()

        # Act
        builder.con_id(cualquier_id)

        # Assert
        self.assertEqual(cualquier_id, builder.id)

    @data("", "  ", "es", "english")
    def test_en_idioma_con_cualquier_idioma_deberia_incorporarlo(self, cualquier_idioma: str):
        # Arrange
        builder = ClimaBuilder()

        # Act
        builder.en_idioma(cualquier_idioma)

        # Assert
        self.assertEqual(cualquier_idioma, builder.idioma)

    def test_constructor_con_creacion_deberia_tener_idioma_ciudad_grados_pais_url(self):
        # Arrange
        idioma = "en"
        ciudad = "Buenos%20Aires"
        pais = "ar"
        grados = "kelvin"
        url_servicio = "http://api.openweathermap.org/data/2.5/weather"

        # Act
        builder = ClimaBuilder()

        # Assert
        self.assertEqual(pais, builder.pais)
        self.assertEqual(ciudad, builder.ciudad)
        self.assertEqual(idioma, builder.idioma)
        self.assertEqual(grados, builder.grados)
        self.assertEqual(url_servicio, builder.url_servicio)

    @data(
        ( 2172797, None, None, None, None, None, "english", "fahrenheit", "http://api.openweathermap.org/data/1.0/weather" ),
        ( None, "Sydney", "au", None, None, None, "australian english", "kelvin", "http://api.openweathermap.org/data/1.5/weather" ),
        ( None, None, None, None, 34.6037, 58.3816, "sp", "celsius", "http://api.openweathermap.org/data/2.0/weather" ),
        ( None, None, None, "92730", None, None, "en", "fahrenheit", "http://api.openweathermap.org/data/2.5/weather" ),
    )
    @unpack
    def test_build_con_varios_valores_deberia_crearlo_con_ellos(self, id: int, ciudad: str, pais: str, cp: str, latitud: float, longitud: float, idioma: str, grados: str, url_servicio: str):
        # Arrange
        apikey = "abcdefg"

        with patch.object(ClimaBuilder, "_crear_clima", return_value=None) as mock_method:
            builder = (
                ClimaBuilder().con_apikey(apikey)
                              .con_id(id)
                              .con_servicio(url_servicio)
                              .con_ciudad(ciudad)
                              .en_pais(pais)
                              .en_codigo_postal(cp)
                              .en_coordenadas(latitud, longitud)
                              .en_idioma(idioma)
            )

            if grados == "fahrenheit":
                builder.en_fahrenheit()
            elif grados == "celsius":
                builder.en_celsius()
            else:
                builder.en_kelvin()

            # Act
            clima = builder.build()

            # Assert
            self.assertIsNone(clima)
            mock_method.assert_called_once_with(apikey, id, ciudad, pais, cp, (latitud, longitud), idioma, grados, url_servicio)

    @data(None, "", "    ", "http://www.example.com", "http://api.openweathermap.org/data/2.5/weather")
    def test_con_servicio_con_cualquier_url_deberia_incorporarlo(self, cualquier_url: str):
        # Arrange
        builder = ClimaBuilder()

        # Act
        builder.con_servicio(cualquier_url)

        # Assert
        self.assertEqual(cualquier_url, builder.url_servicio)

if __name__ == "__main__":
    unittest.main()
