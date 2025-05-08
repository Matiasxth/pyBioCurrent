def traducir_binario(datos, umbral=0.01):
    """
    Convierte una señal en cadena binaria simple.
    Permite visualizar patrones repetitivos o eventos como pulsos o espigas eléctricas.
    """
    binario = ''.join(['1' if x > umbral else '0' for x in datos])
    return binario
