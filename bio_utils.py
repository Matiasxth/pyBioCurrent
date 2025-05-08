def normalizar(datos):
    return (datos - np.min(datos)) / (np.max(datos) - np.min(datos))

def calcular_fft(datos, fs):
    freqs = np.fft.rfftfreq(len(datos), d=1/fs)
    fft_vals = np.abs(np.fft.rfft(datos))
    return freqs, fft_vals
