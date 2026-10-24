# Reproducción y mantenimiento del proyecto

| Simposio | Curso avanzado |
|:---:|:---:|
| [![XI Simposio Latinoamericano de Tecnología de Cultivos Celulares](imagenes/Simposio_portada.png)](https://www.slatcc.com/) | [![Curso Avanzado de Tecnologías de Cultivo Celular 2026](imagenes/Curso_portada.png)](https://www.slatcc.com/) |

Material educativo para el **SLATCC**: [www.slatcc.com](https://www.slatcc.com/). Esta guía describe cómo reproducir el análisis y mantener los materiales del taller **“Tiempo de respuesta de los sensores de pH y oxígeno disuelto”**.

## Estructura

| Ruta | Función |
|---|---|
| `analizar_respuesta.py` | Carga el Excel, revisa calidad, calcula métricas y genera figuras |
| `ventanas_piloto.json` | Ventanas, niveles e inicios inferidos del análisis histórico |
| `practica/Practica_respuesta_sensores.md` | Fuente del texto, fichas y notas del instructor |
| `practica/generar_word.py` | Convierte Markdown con Pandoc y aplica formato con python-docx |
| `plantilla_documento.docx` | Tamaño de página, márgenes, encabezados, pie y formato del evento |
| `B2 Respuesta electrodos.xlsx` | Datos originales; conservar como entrada del análisis |
| `datos_limpios/` | CSV completos por hoja y ventanas seleccionadas |
| `resultados/` | Calidad, niveles y métricas en `piloto.json`; tabla legible en `piloto.md` |
| `figuras/` | Montaje, respuesta didáctica, registros y ventanas del piloto |
| `tests/test_metricas.py` | Comprobaciones de tiempos, huecos y estabilización |
| `requirements.txt` | Dependencias de Python |

## Entorno

Se necesita Python 3 y las bibliotecas de `requirements.txt`: NumPy, pandas, Matplotlib, openpyxl y python-docx. Para generar Word también se requiere el ejecutable `pandoc`; para exportar PDF desde la terminal, LibreOffice.

Desde la raíz del proyecto:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Las dependencias no están fijadas a versiones específicas. El entorno permite reproducir el procedimiento, pero no garantiza archivos binarios idénticos entre versiones de bibliotecas, fuentes tipográficas o conversores.

## Datos y condiciones experimentales

El Excel tiene las hojas `pH` y `OD`, registradas por separado el 14 de octubre de 2026. Se descartan las filas de encabezados auxiliares sin `PDatTime`; `pH_1` y `pO2_1` se convierten a números. `ProcessTime` está en horas: se resta el primer valor de cada hoja y se multiplica por 3600 para obtener `t_s`.

Se utiliza `ProcessTime` porque conserva resolución subsegundo; hay marcas `PDatTime` repetidas al final de ambas hojas. El intervalo mediano es aproximadamente 1.01 s. El contador `tiempo` de la hoja no sustituye esta base temporal.

La hoja pH tiene 8432 filas con marca temporal, 15 valores faltantes en cada señal, cinco registros de ceros simultáneos y un intervalo máximo de unos 17 s. Los ceros simultáneos de pH/OD se marcan como `posible_artefacto`: no prueban un medio con pH 0 ni un cambio físico de oxígeno. Se conservan en los CSV completos con su bandera; se excluyen en las curvas de referencia y métricas. Los datos originales permanecen intactos. La hoja OD tiene 1156 filas y no presenta esos faltantes o ceros simultáneos.

El archivo no informa modelo de sonda, gases, temperatura de los vasos ni eventos de transferencia. La columna de setpoint de pH no identifica un buffer. Tampoco permite afirmar cuándo se consiguió o aplicó el N₂: ese dato procede del relato de la sesión.

## Ejecutar el análisis

Con el entorno activado, desde la raíz del proyecto:

```bash
python analizar_respuesta.py
python -m unittest discover -s tests -v
```

Se puede especificar otro archivo y otra configuración:

```bash
python analizar_respuesta.py "B2 Respuesta electrodos.xlsx" --config ventanas_piloto.json
```

El lector espera las hojas pH/OD y columnas de esta exportación. Adaptar la carga si cambia el formato. La figura de intentos OD está contextualizada al piloto incluido, con una marca histórica alrededor de 836 s; no se adapta automáticamente a otro experimento. No reutilizar ese marcado para datos nuevos sin modificarlo.

Las salidas se escriben en las carpetas del proyecto y se sobrescriben al repetir el análisis. Revisar gráficas y calidad antes de actualizar la tabla del instructor. Las pruebas usan señales con tiempos conocidos y verifican ascenso, descenso, cruce sin estabilidad, huecos, ventana corta y cambio nulo; no suponen una respuesta “correcta” para las sondas reales.

## Interpretar los resultados

### Ventanas elegidas

Se seleccionaron **dos ejemplos ilustrativos**, no todos los cambios visibles:

| Hoja | Inicio inferido [s] | Ventana de análisis [s] | Nivel inicial [s] | Nivel final [s] |
|---|---|---|---|---|
| pH | 1204.15 | 1140–1710 | 1140–1200 | 1640–1700 |
| OD | 836.25 | 790–1164 | 805–835 | 1000–1160 |

Los segundos comienzan en cada hoja. El descenso de pH tiene una transición identificable y una cola; la transición final de OD es ascendente y rápida. Los intentos previos de OD tienen entradas desconocidas y pueden incluir cambios lentos del medio. No se reportan como tiempos intrínsecos de respuesta.

El análisis usa la mediana de las ventanas inicial y final. También exporta pendiente y rango de la ventana final para revisar su calidad: **no certifica automáticamente una meseta**. Antes de aplicar el método a un nuevo ensayo, comprobar el montaje, t₀ marcado, mesetas y suficiencia del registro. Los inicios históricos son inferidos; cambiar t₀ desplaza los tiempos aparentes. El taller propone promedios de 30 s para una lectura manual sencilla, por lo que no se deben exigir decimales idénticos al análisis del piloto.

### Definición de las métricas

El recorrido normalizado es `(y − y0) / (yf − y0)`. Sirve para ascenso y descenso; en pH representa el recorrido de la lectura, no una fracción de concentración de H⁺. Se lee el primer cruce de 0.1, 0.632 y 0.9 mediante interpolación lineal de muestras consecutivas. El 63.2 % es una salida exploratoria adicional y no es necesario para completar la práctica.

El script no suaviza la señal para calcular los tiempos. No extrapola cruces ni interpola a través de huecos mayores de 3 s o de valores faltantes. Si el primer punto disponible ya supera un umbral y no permite localizar su cruce, se devuelve `null`.

La estabilización es la primera muestra dentro de **±5 % de |yf − y0|** que permanece dentro hasta el final de la ventana, con **al menos 30 s de observación** y sin huecos mayores de 3 s o muestras no finitas en ese tramo. La falta de confirmación se escribe como `null`, no como cero. El resultado depende de cuánto tiempo se observó y no garantiza que el sistema no cambie posteriormente.

**Los t90 y tiempos de estabilización históricos son aparentes.** La diferencia t10–90 reduce la dependencia del origen supuesto, pero no elimina los efectos del montaje, del filtrado ni de la selección de niveles. Los tiempos de la tabla de la guía proceden del JSON generado con las ventanas incluidas.

## Actualizar la guía, Word y PDF

Editar los Markdown de la guía y de `practica/Anexo_instructor.md`. El generador produce ambos Word; con `--pdf` exporta también ambos PDF mediante LibreOffice:

```bash
python practica/generar_word.py --pdf
```

El generador usa la plantilla, mantiene texto justificado y centra ecuaciones y figuras. Sobrescribe el Word; incorporar primero cualquier edición manual a la fuente. Si se actualizan datos, regenerar figuras antes del documento. Si cambian ventanas o criterios, revisar también las cifras y el texto del anexo.

Revisar visualmente el PDF: legibilidad de ecuaciones y etiquetas, tablas, saltos de página y espacio para completar las fichas. Comprobar que los cuatro sentidos de transferencia, los buffers **pH 3 y pH 10** y el registro de identificación sigan presentes.

## Criterios para mantener el material

Conservar separados los datos originales, las estimaciones del análisis y las observaciones de operación. Registrar la identidad de cada sonda, condiciones del ensayo y eventos de transferencia. No atribuir valores nominales de buffers ni modelos de sonda al piloto sin una fuente verificable.

El entorno virtual, archivos temporales y respaldos locales quedan excluidos por `.gitignore`. El material no presupone que las sondas sean de un fabricante particular; las referencias técnicas de la guía orientan el montaje y no sustituyen la identificación y el manual del modelo utilizado.

## Identidad visual y materiales relacionados

Los archivos `docs/imagenes/Simposio_portada.png` y `docs/imagenes/Curso_portada.png` son copias de las portadas proporcionadas para el simposio y el curso. Se conservan con sus nombres y sin modificaciones. Son recursos de documentación, separados de las figuras generadas por el análisis. El README y esta guía usan rutas relativas para que los logos se vean tanto en GitHub como en una copia local.

La presentación de Word y PDF se obtiene de `plantilla_documento.docx`. Para cambios solo de documentación no es necesario regenerar datos ni sobrescribir documentos editados. Si se actualizan los logos de la serie, sustituir las copias en ambos repositorios para mantener la misma identidad visual.

Taller complementario: [Control de oxígeno en biorreactores](https://github.com/ebalderasr/control-oxigeno-biorreactores). Ambos repositorios usan la misma estructura de README y guía de reproducción, con instrucciones específicas para sus datos.
