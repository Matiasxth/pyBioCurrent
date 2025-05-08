def generar_estimulo(frecuencia=1.0, duracion=5, amplitud=0.5):
    """
    Genera un tren de pulsos eléctricos. Se usaría con DAC o relé externo.
    - frecuencia: Hz
    - duración: segundos
    - amplitud: voltaje del pulso (simulado o real)
    """
    intervalo = 1.0 / frecuencia
    pulsos = int(duracion * frecuencia)
    for i in range(pulsos):
        print(f"[Estimulo] Pulso {i+1}/{pulsos} - Amplitud: {amplitud}V")
        time.sleep(intervalo)
