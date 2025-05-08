class BioNetwork:
    def __init__(self):
        self.nodos = []

    def agregar_nodo(self, nodo):
        self.nodos.append(nodo)

    def propagar_evento(self, origen, umbral=0.02):
        """
        Si un nodo detecta una señal > umbral, envía estímulo a los demás.
        """
        datos = origen.leer(tiempo=2)
        if np.max(np.abs(datos)) > umbral:
            print(f"[Red] Evento detectado en {origen.name}. Propagando...")
            for nodo in self.nodos:
                if nodo != origen:
                    generar_estimulo(frecuencia=0.5, duracion=2)
