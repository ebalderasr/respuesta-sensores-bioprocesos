# Datos, análisis y mantenimiento

Proyecto educativo para [www.slatcc.com](https://www.slatcc.com/). El contenido principal es la guía `practica/Practica_respuesta_sensores.md`. Los participantes deben identificar las sondas como parte de la práctica; los modelos no están confirmados al preparar este material.

## Archivos y dependencias

- `B2 Respuesta electrodos.xlsx`: entrada original; no se modifica.
- `analizar_respuesta.py`: carga, revisión de calidad, métricas y figuras.
- `ventanas_piloto.json`: ventanas, niveles e inicios inferidos; decisiones explícitas y editables.
- `datos_limpios/`: CSV completos por hoja y ventanas seleccionadas.
- `resultados/piloto.json`: calidad, niveles, criterios y métricas por ventana.
- `resultados/piloto.md`: tabla legible de los resultados exploratorios.
- `figuras/`: cinco imágenes generadas (montaje, ejemplo didáctico y piloto).
- `practica/generar_word.py`: Pandoc convierte Markdown y python-docx aplica el formato.
- `plantilla_documento.docx`: formato del evento, con encabezados y pie.
- `tests/test_metricas.py`: comprobaciones de la definición de tiempos, huecos y estabilización.

Python usa NumPy, pandas, Matplotlib, openpyxl y python-docx, declarados en `requirements.txt`. Pandoc y LibreOffice se instalan por separado. Las versiones no están fijadas: cambios de bibliotecas, fuentes y conversores pueden modificar el aspecto y los archivos binarios.

## Base de tiempo y calidad

El Excel tiene las hojas `pH` y `OD`, registradas por separado el 14 de octubre de 2026. Se descartan las filas de encabezados auxiliares sin `PDatTime`; `pH_1` y `pO2_1` se convierten a números. `ProcessTime` está en horas: se resta el primer valor de cada hoja y se multiplica por 3600 para obtener `t_s`.

Se utiliza `ProcessTime` porque conserva resolución subsegundo; hay marcas `PDatTime` repetidas al final de ambas hojas. El intervalo mediano es aproximadamente 1.01 s. El contador `tiempo` de la hoja no sustituye esta base temporal.

La hoja pH tiene 8432 filas con marca temporal, 15 valores faltantes en cada señal, cinco registros de ceros simultáneos y un intervalo máximo de unos 17 s. Los ceros simultáneos de pH/OD se marcan como `posible_artefacto`: no prueban un medio con pH 0 ni un cambio físico de oxígeno. Se conservan en los CSV completos con su bandera; se excluyen en las curvas de referencia y métricas. Los datos originales permanecen intactos. La hoja OD tiene 1156 filas y no presenta esos faltantes o ceros simultáneos.

El archivo no informa modelo de sonda, gases, temperatura de los vasos ni eventos de transferencia. La columna de setpoint de pH no identifica un buffer. Tampoco permite afirmar cuándo se consiguió o aplicó el N₂: ese dato procede del relato de la sesión.

## Ventanas elegidas

Se seleccionaron **dos ejemplos ilustrativos**, no todos los cambios visibles:

| Hoja | Inicio inferido [s] | Ventana de análisis [s] | Nivel inicial [s] | Nivel final [s] |
|---|---|---|---|---|
| pH | 1204.15 | 1140–1710 | 1140–1200 | 1640–1700 |
| OD | 836.25 | 790–1164 | 805–835 | 1000–1160 |

Los segundos comienzan en cada hoja. El descenso de pH tiene una transición identificable y una cola; la transición final de OD es ascendente y rápida. Los intentos previos de OD tienen entradas desconocidas y pueden incluir cambios lentos del medio. No se reportan como tiempos intrínsecos de respuesta.

El análisis usa la mediana de las ventanas inicial y final. También exporta pendiente y rango de la ventana final para revisar su calidad: **no certifica automáticamente una meseta**. Antes de aplicar el método a un nuevo ensayo, comprobar el montaje, t₀ marcado, mesetas y suficiencia del registro. Los inicios históricos son inferidos; cambiar t₀ desplaza los tiempos aparentes. El taller propone promedios de 30 s para una lectura manual sencilla, por lo que no se deben exigir decimales idénticos al análisis del piloto.

## Definición de las métricas

El recorrido normalizado es `(y − y0) / (yf − y0)`. Sirve para ascenso y descenso; en pH representa el recorrido de la lectura, no una fracción de concentración de H⁺. Se lee el primer cruce de 0.1, 0.632 y 0.9 mediante interpolación lineal de muestras consecutivas. El 63.2 % es una salida exploratoria adicional y no es necesario para completar la práctica.

El script no suaviza la señal para calcular los tiempos. No extrapola cruces ni interpola a través de huecos mayores de 3 s o de valores faltantes. Si el primer punto disponible ya supera un umbral y no permite localizar su cruce, se devuelve `null`.

La estabilización es la primera muestra dentro de **±5 % de |yf − y0|** que permanece dentro hasta el final de la ventana, con **al menos 30 s de observación** y sin huecos mayores de 3 s o muestras no finitas en ese tramo. La falta de confirmación se escribe como `null`, no como cero. El resultado depende de cuánto tiempo se observó y no garantiza que el sistema no cambie posteriormente.

**Los t90 y tiempos de estabilización históricos son aparentes.** La diferencia t10–90 reduce la dependencia del origen supuesto, pero no elimina los efectos del montaje, del filtrado ni de la selección de niveles. Los tiempos de la tabla de la guía proceden del JSON generado con las ventanas incluidas.

## Ejecutar y revisar

Desde la raíz del proyecto:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python analizar_respuesta.py
python -m unittest discover -s tests -v
```

Se puede especificar otro archivo y otra configuración:

```bash
python analizar_respuesta.py "B2 Respuesta electrodos.xlsx" --config ventanas_piloto.json
```

El lector espera las hojas pH/OD y columnas de esta exportación. Adaptar la carga si cambia el formato. La figura de intentos OD está contextualizada al piloto incluido, con una marca histórica alrededor de 836 s; no se adapta automáticamente a otro experimento. No reutilizar ese marcado para datos nuevos sin modificarlo.

Las salidas se escriben en las carpetas del proyecto y se sobrescriben al repetir el análisis. Revisar gráficas y calidad antes de actualizar la tabla del instructor. Las pruebas usan señales con tiempos conocidos y verifican ascenso, descenso, cruce sin estabilidad, huecos, ventana corta y cambio nulo; no suponen una respuesta “correcta” para las sondas reales.

## Actualizar los documentos

Editar el Markdown y después generar Word con Pandoc instalado:

```bash
python practica/generar_word.py
libreoffice --headless --convert-to pdf --outdir practica practica/Practica_respuesta_sensores.docx
```

El generador usa la plantilla, mantiene texto justificado y centra ecuaciones y figuras. Sobrescribe el Word; incorporar primero cualquier edición manual a la fuente. Si se actualizan datos, regenerar figuras antes del documento. Si cambian ventanas o criterios, revisar también las cifras y el texto del anexo.

Revisar visualmente el PDF: legibilidad de ecuaciones y etiquetas, tablas, saltos de página y espacio para completar las fichas. Comprobar que los cuatro sentidos de transferencia, los buffers **pH 8 y pH 3** y el registro de identificación sigan presentes.

El entorno virtual, archivos temporales y respaldos locales quedan excluidos por `.gitignore`. El material no presupone que las sondas sean de un fabricante particular; las referencias técnicas de la guía orientan el montaje y no sustituyen la identificación y el manual del modelo utilizado.
