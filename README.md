pyBioCurrent
============

Una librería experimental y científica para la adquisición, estimulación y traducción de señales bioeléctricas generadas por organismos vivos, como plantas, hongos o tejidos celulares.

Fundamento científico:
----------------------
Numerosos estudios han confirmado que las plantas, hongos y algunos organismos simples generan y responden a impulsos eléctricos (Volkov, 2006; Fromm & Lautner, 2007). Las señales pueden tener forma de potenciales de acción (PA) o variaciones de potencial lento (VPS), con frecuencias típicas entre 0.01 Hz y 3 Hz. Estas pueden estar relacionadas con reacciones a la luz, presión, temperatura o agentes químicos.

📚 Fundamento Científico
Las plantas y otros organismos no animales generan y responden a señales eléctricas que cumplen funciones de comunicación interna y adaptación al entorno (Volkov, 2006; Fromm & Lautner, 2007). Estas señales se clasifican principalmente en:

Potenciales de Acción (PA): Pulsos rápidos ante estímulos bruscos.

Variaciones de Potencial Lento (VPS): Cambios graduales relacionados con procesos fisiológicos.

Frecuencias típicas registradas: 0.01 Hz a 3 Hz
Amplitudes esperadas: 10 µV a 200 mV (dependiendo de la especie y método de contacto).

La traducción de estas señales, así como su interacción entre organismos, abre una vía experimental para estudiar un lenguaje bioeléctrico aún no decodificado completamente.

Componentes:
- signal.py: Adquisición y preprocesamiento de señales (con filtros fisiológicamente relevantes).
- translate.py: Conversión de patrones eléctricos a representaciones binarias o visuales.
- stimulus.py: Generación controlada de impulsos eléctricos.
- network.py: Comunicación e interacción entre múltiples nodos biológicos.

🔧 Funcionalidades
Módulo	Descripción
signal.py	Lectura y filtrado de señales bioeléctricas (bandpass, lowpass).
translate.py	Traducción a patrones binarios o visualizables.
stimulus.py	Generación de pulsos eléctricos experimentales (DAC o relé).
network.py	Comunicación entre nodos biológicos mediante propagación de eventos.
utils.py	Análisis FFT, normalización de señales y herramientas matemáticas.

Advertencia:
------------
Esta librería tiene fines exclusivamente investigativos y educativos. Su uso en seres vivos debe respetar la ética científica. Cualquier intento de aplicar estimulación eléctrica debe tener una base experimental segura y nunca con fines invasivos o sin revisión ética.
"""

⚡ Ejemplo de uso:
from pybiocurrent.signal import BioNode
from pybiocurrent.translate import traducir_binario

planta = BioNode(name=\"Mimosa\", input_device=\"Simulado\", fs=10)
datos = planta.leer(tiempo=10)
mensaje = traducir_binario(datos, umbral=0.015)

print(\"Mensaje simbólico:\", mensaje)

📖 Bibliografía científica
Volkov, A. G. (2006). Plant Electrophysiology. Springer.

Fromm, J., & Lautner, S. (2007). Electrical signals and their physiological significance in plants. Plant, Cell & Environment.

