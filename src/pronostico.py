from typing import Any

class Pronostico:
    def __init__(self, json: Any, grados: str):
        if json is None:
            raise ValueError()

        self.__json_data = json
        self.__titulo = self.__json_data["weather"][0]["main"]
        self.__descripcion = self.__json_data["weather"][0]["description"]
        self.__temperatura = self.__json_data["main"]["temp"]
        self.__tempmin = self.__json_data["main"]["temp_min"]
        self.__tempmax = self.__json_data["main"]["temp_max"]
        self.__ciudad = self.__json_data["name"]
        self.__coordenadas = (self.__json_data["coord"]["lat"], self.__json_data["coord"]["lon"])
        self.__pais = self.__json_data["sys"]["country"]
        self.__grados = grados

    @property
    def titulo(self) -> str:
        return self.__titulo

    @property
    def descripcion(self) -> str:
        return self.__descripcion

    @property
    def temperatura(self) -> str:
        return self.__temperatura

    @property
    def temperatura_minima(self) -> str:
        return self.__tempmin

    @property
    def temperatura_maxima(self) -> str:
        return self.__tempmax

    @property
    def ciudad(self) -> str:
        return self.__ciudad

    @property
    def pais(self) -> str:
        return self.__pais

    @property
    def coordenadas(self) -> (float, float):
        return self.__coordenadas

    def _visualizar_grados(self):
        if self.__grados == "celsius":
            return "C"
        elif self.__grados == "fahrenheit":
            return "F"
        else:
            return "K"

    def __str__(self):
        return f"{self.ciudad} ({self.pais}) currently has {self.descripcion} with a temperature of {self.temperatura}{self._visualizar_grados()}."
