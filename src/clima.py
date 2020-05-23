import urllib.request, json
from pronostico import Pronostico
from typing import Any

class Clima:
    def __init__(self, apikey: str, id: int, ciudad: str, pais: str, cp: str, coordenadas: (float, float), idioma: str, grados: str, url_servicio: str):
        self.__apikey = apikey.strip() if apikey is not None else ""
        if self.__apikey == "":
            raise ValueError()

        self.__url_servicio = url_servicio.strip() if url_servicio is not None else ""
        if self.__url_servicio == "":
            raise ValueError()

        self.__id = id
        self.__ciudad = ciudad
        self.__pais = pais
        self.__codigo_postal = cp
        self.__coordenadas = coordenadas
        self.__idioma = idioma
        self.__grados = grados
        self.__url = self._build_url()

    @property
    def url_servicio(self) -> str:
        return self.__url_servicio

    def _build_url(self):
        url = f"{self.__url_servicio}?appid={self.__apikey}"
        if self.__id is not None:
            url = f"{url}&id={self.__id}"
        elif self.__ciudad is not None:
            url = f"{url}&q={self.__ciudad}"

            if self.__pais is not None:
                url = f"{url},{self.__pais}"
        elif self.__codigo_postal is not None:
            url = f"{url}&zip={self.__codigo_postal}"

            if self.__pais is not None:
                url = f"{url},{self.__pais}"
        elif self.__coordenadas is not None:
            if None in self.__coordenadas:
                raise ValueError()

            url = f"{url}&lat={self.__coordenadas[0]}&lon={self.__coordenadas[1]}"
        else:
            raise ValueError()

        if self.__idioma is not None and self.__idioma != "" and self.__idioma != "en":
            url = f"{url}&lang={self.__idioma}"

        if self.__grados is not None:
            if self.__grados == "fahrenheit":
                url = f"{url}&units=imperial"
            elif self.__grados == "celsius":
                url = f"{url}&units=metric"

        return url

    @property
    def url(self) -> str:
        return self.__url

    @property
    def apikey(self) -> str:
        return self.__apikey

    @property
    def ciudad(self) -> str:
        return self.__ciudad

    @property
    def id(self) -> int:
        return self.__id

    @property
    def pais(self) -> str:
        return self.__pais

    @property
    def codigo_postal(self) -> str:
        return self.__codigo_postal

    @property
    def coordenadas(self) -> (float, float):
        return self.__coordenadas

    @property
    def idioma(self) -> str:
        return self.__idioma

    @property
    def grados(self) -> str:
        return self.__grados

    def obtener(self) -> Pronostico:
        data = self._get_server_data(self.__url)

        if data:
            json = self._deserialize_json(data)

            if json:
                return Pronostico(json, self.__grados)

    def _deserialize_json(self, data: str) -> Any:
        try:
            return json.loads(data)
        except:
            return None

    def _get_server_data(self, link: str) -> str:
        try:
            with urllib.request.urlopen(link) as url:
                data = url.read().decode()
        except:
            data = None

        return data
