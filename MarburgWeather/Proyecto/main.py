import argparse
from utils.weather_parser import parse_weather_log

def main():
    """
    Punto de entrada del script que recibe argumentos para procesar los datos del clima.
    """
    parser = argparse.ArgumentParser(description="Procesa datos del clima desde output.log a CSV")
    parser.add_argument("--log", type=str, default="/home/juanubuntu/Clima-Marburg-App/MarburgWeather/Proyecto/Crontab/output.log", help="Ruta del archivo de log")
    parser.add_argument("--csv", type=str, default="clima-Marburg-hoy.csv", help="Nombre del archivo CSV de salida")
    args = parser.parse_args()
    parse_weather_log(args.log, args.csv)

if __name__ == "__main__":
    main()
