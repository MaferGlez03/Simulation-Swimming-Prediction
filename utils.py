import numpy as np
import pandas as pd

def parse_time_to_seconds(tiempo_str):
    """"
    Convierte el tiempo escrito como minutos:segundos
    en minutos*60 + segundos 
    """
    try:
        minutos, segundos = tiempo_str.split(':')
        minutos = int(minutos)
        segundos = float(segundos)
        total_segundos = minutos * 60 + segundos
        return total_segundos
    except ValueError:
        return float(tiempo_str)
    

def race_simulation_kde(competitors):
    """"
    Recibe un array de (athlete_name, kde), se genera un sample
    de ese atleta en su respectivo kde y se le asocia a cada atleta.
    Se retorna el mismo array ordenado por los samples generados
    """
    results = []
    for competitor in competitors:
        sample = competitor[1].sample(1)
        results.append((competitor[0],competitor[1],sample))
    results = sorted(results, key=lambda x: x[2])
    results = [(x[0], x[1]) for x in results]
    return results

def date_to_value(fecha):
    """"
    Se crea la funcion de peso para el kde
    Se obtiene el numero de dias desde el minimo de la simulacion
    hasta la fecha establecida, se normaliza y se obtiene su valor
    en la funcion escogida para los pesos
    """
    dias_desde_enero_2022 = (fecha - pd.Timestamp('2022-01-01')).days
    normalizado = dias_desde_enero_2022 / (pd.Timestamp('2024-07-01') - pd.Timestamp('2022-01-01')).days
    valor = np.log(normalizado + 1) 
    return valor

def sort_key(item):
    """"
    Ordena de mayor a menor
    """
    name, scores = item
    return tuple(-scores[i] for i in range(1, 9))