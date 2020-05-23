from clima import Clima

class ClimaBuilder:
    def __init__(self):
        self.__apikey = None
        self.__id = None
        self.__coordenadas = None
        self.__codigo_postal = None
        self.__grados = "kelvin"
        self.__pais = "ar"
        self.__ciudad = "Buenos%20Aires"
        self.__idioma = "en"
        self.__url_servicio = "http://api.openweathermap.org/data/2.5/weather"

    def con_servicio(self, url_servicio: str):
        self.__url_servicio = url_servicio
        return self

    @property
    def url_servicio(self) -> str:
        return self.__url_servicio

    def con_apikey(self, apikey: str):
        self.__apikey = apikey
        return self

    @property
    def apikey(self) -> str:
        return self.__apikey

    def con_ciudad(self, ciudad: str):
        self.__ciudad = ciudad
        return self

    @property
    def ciudad(self) -> str:
        return self.__ciudad

    def en_pais(self, pais: str):
        self.__pais = pais
        return self

    @property
    def pais(self) -> str:
        return self.__pais

    def en_codigo_postal(self, codigo: str):
        self.__codigo_postal = codigo
        return self

    @property
    def codigo_postal(self) -> str:
        return self.__codigo_postal

    def en_fahrenheit(self):
        self.__grados = "fahrenheit"
        return self

    def en_celsius(self):
        self.__grados = "celsius"
        return self

    def en_kelvin(self):
        self.__grados = "kelvin"
        return self

    @property
    def grados(self) -> str:
        return self.__grados

    def en_idioma(self, idioma: str):
        self.__idioma = idioma
        return self

    @property
    def idioma(self) -> str:
        return self.__idioma

    def con_id(self, id: int):
        self.__id = id
        return self

    @property
    def id(self) -> int:
        return self.__id

    def en_coordenadas(self, latitud: float, longitud: float):
        self.__coordenadas = (latitud, longitud)
        return self

    @property
    def coordenadas(self) -> (float, float):
        return self.__coordenadas

    def _crear_clima(self, apikey: str, id: int, ciudad: str, pais: str, cp: str, coordenadas: (float, float), idioma: str, grados: str, url_servicio: str) -> Clima:
        return Clima(apikey, id, ciudad, pais, cp, coordenadas, idioma, grados, url_servicio)

    def build(self):
        return self._crear_clima(self.__apikey, self.__id, self.__ciudad, self.__pais, self.__codigo_postal, self.__coordenadas, self.__idioma, self.__grados, self.__url_servicio)


