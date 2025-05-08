import numpy as np
import time
import scipy.signal as signal

class BioNode:
    def __init__(self, name, input_device, channel=0, vref=3.3, fs=10):
        self.name = name
        self.device = input_device  # Ejemplo: 'ADS1115', 'Simulado', 'Serial'
        self.channel = channel
        self.vref = vref
        self.fs = fs  # Frecuencia de muestreo en Hz

    def leer(self, baseline=2.5, tiempo=10, filtro='bandpass', rango=(0.1, 1.5)):
        datos = []
        for _ in range(tiempo * self.fs):
            valor = self.simular_lectura()  # Reemplazar por hardware real
            datos.append(valor - baseline)
            time.sleep(1 / self.fs)
        datos = np.array(datos)
        if filtro:
            datos = self.aplicar_filtro(datos, filtro, rango)
        return datos

    def aplicar_filtro(self, datos, tipo, rango):
        nyq = 0.5 * self.fs
        if tipo == 'bandpass':
            b, a = signal.butter(2, [r / nyq for r in rango], btype='band')
        elif tipo == 'lowpass':
            b, a = signal.butter(2, rango[1] / nyq, btype='low')
        else:
            return datos
        return signal.filtfilt(b, a, datos)

    def simular_lectura(self):
        base = 2.5 + np.sin(time.time() * 0.5) * 0.03
        ruido = np.random.normal(0, 0.01)
        return base + ruido
