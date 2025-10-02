1. Cambio de ciudad: León → Yucatán

En la URL de la API, cambié las coordenadas:

- ?latitude=21.12&longitude=-101.68
+ ?latitude=20.97&longitude=-89.62


Esto hace que los datos ahora correspondan al estado de Yucatán (aproximadamente Mérida).

✅ 2. Cambio de variables solicitadas a la API

Antes pedías:

hourly=temperature_2m


Ahora pedimos:

hourly=relativehumidity_2m,windspeed_10m


Esto significa que ahora se obtienen:

Humedad relativa a 2 metros del suelo

Velocidad del viento a 10 metros

✅ 3. Extracción de nuevos datos del JSON

Reemplacé esto:

horas = data["hourly"]["time"]
temperaturas = data["hourly"]["temperature_2m"]


Por esto:

horas = data["hourly"]["time"]
humedad = data["hourly"]["relativehumidity_2m"]
viento = data["hourly"]["windspeed_10m"]


Para ajustarlo a los nuevos datos solicitados.

✅ 4. Personalización de gráficas

Modifiqué el estilo de las gráficas:

En la gráfica de línea:
ax.plot(
    horas,
    datos,
    linestyle="-",
    marker="s",        # marcador cuadrado
    markersize=4,
    linewidth=2,       # línea más gruesa
    alpha=0.7          # transparencia
)

En ambas gráficas (línea y barras):

Agregué:

ax.grid(True, linestyle="--", alpha=0.5)


Para mostrar rejilla punteada y semitransparente, lo que mejora la visualización.

✅ 5. Cambio de títulos y etiquetas

Cambié los textos de las gráficas para que coincidan con las nuevas variables, por ejemplo:

"Temperatura en León (línea)" → "Humedad en Yucatán (línea)"

"Velocidad del viento en Yucatán (barras)"

También ajusté los ejes Y con unidades correctas:

"°C" → "%" para humedad

"km/h" para viento

✅ 6. Ajuste en la función mostrar_graficas

Reemplacé los gráficos de temperatura por gráficos de humedad y viento, llamando a las funciones con los nuevos datos.

✅ 7. Cambios menores en comentarios y nombres

Actualicé descripciones, docstrings y nombres para que reflejen los nuevos datos (humedad y viento).