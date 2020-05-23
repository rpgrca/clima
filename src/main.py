import sys
import argparse
from climabuilder import ClimaBuilder
from clima import Clima
from pronostico import Pronostico

def main():
    climaBuilder = ClimaBuilder()
    parser = argparse.ArgumentParser(description="Process Clima calls.")

    parser.add_argument('--id', help='id de la ciudad', default=climaBuilder.id, type=int)
    parser.add_argument('--coordenadas', help='latitud,longitud de la ciudad', default=None, action='append', type=float)
    parser.add_argument('--ciudad', help='nombre de la ciudad', default=climaBuilder.ciudad)
    parser.add_argument('--codigo-postal', help='código postal de la ciudad', default=climaBuilder.codigo_postal)
    parser.add_argument('--pais', help='país', default=climaBuilder.pais)
    parser.add_argument('--key', help='la API key a usar en la conexión', default=climaBuilder.apikey)
    parser.add_argument('--temperatura', help='formato de la temperatura', choices=['fahrenheit', 'celsius', 'kelvin'], default=climaBuilder.grados)
    args = parser.parse_args()

    climaBuilder = (
        climaBuilder.con_apikey("3fce6c5b0d0d33d0766739c6b1473517")
                    .con_servicio("http://api.openweathermap.org/data/2.5/weather")
                    .con_ciudad(args.ciudad)
                    .en_pais(args.pais)
                    .en_codigo_postal(args.codigo_postal)
                    .en_pais(args.pais)
                    .con_id(args.id)
    )

    if args.temperatura == 'fahrenheit':
        climaBuilder.en_fahrenheit()
    elif args.temperatura == 'celsius':
        climaBuilder.en_celsius()
    else:
        climaBuilder.en_kelvin()

    clima = climaBuilder.build()

    if clima:
        pronostico = clima.obtener()

        if pronostico:
            print(pronostico)


if __name__ == "__main__":
    main()
