# bio_utils.py - Funciones auxiliares para análisis de señales bioeléctricas

import numpy as np  # <- Esta línea es imprescindible

def normalizar(datos):
    """Normaliza la señal entre 0 y 1."""
    return (datos - np.min(datos)) / (np.max(datos) - np.min(datos))

def calcular_fft(datos, fs):
    """
    Calcula la Transformada Rápida de Fourier para una señal de entrada.
    - datos: array de señal
    - fs: frecuencia de muestreo (Hz)
    """
    freqs = np.fft.rfftfreq(len(datos), d=1/fs)
    fft_vals = np.abs(np.fft.rfft(datos))
    return freqs, fft_vals
