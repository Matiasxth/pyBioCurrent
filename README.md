pyBioCurrent
============

Una librería experimental y científica para la adquisición, estimulación y traducción de señales bioeléctricas generadas por organismos vivos, como plantas, hongos o tejidos celulares.

Fundamento científico:
----------------------
Numerosos estudios han confirmado que las plantas, hongos y algunos organismos simples generan y responden a impulsos eléctricos (Volkov, 2006; Fromm & Lautner, 2007). Las señales pueden tener forma de potenciales de acción (PA) o variaciones de potencial lento (VPS), con frecuencias típicas entre 0.01 Hz y 3 Hz. Estas pueden estar relacionadas con reacciones a la luz, presión, temperatura o agentes químicos.

La traducción de estas señales, así como su interacción entre organismos, abre una vía experimental para estudiar un lenguaje bioeléctrico aún no decodificado completamente.

Componentes:
- signal.py: Adquisición y preprocesamiento de señales (con filtros fisiológicamente relevantes).
- translate.py: Conversión de patrones eléctricos a representaciones binarias o visuales.
- stimulus.py: Generación controlada de impulsos eléctricos.
- network.py: Comunicación e interacción entre múltiples nodos biológicos.

Advertencia:
------------
Esta librería tiene fines exclusivamente investigativos y educativos. Su uso en seres vivos debe respetar la ética científica. Cualquier intento de aplicar estimulación eléctrica debe tener una base experimental segura y nunca con fines invasivos o sin revisión ética.
"""
