import pandas as pd
from data_reader import leer_datos , filtrar_calcular_media

def main():
    print(filtrar_calcular_media(leer_datos()))

if __name__== "__main__":
    main()