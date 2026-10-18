---
title: "Tiempo de respuesta de los sensores de pH y oxígeno disuelto"
autor: "Emiliano Balderas · Instituto de Biotecnología, UNAM"
---

**Taller:** Caracterización de sensores para bioprocesos

**Duración:** máximo 45 min por equipo; 3 equipos de 6 personas, de forma sucesiva.

**Equipo:** sondas conectadas a Biostat, dos buffers de pH y dos soluciones con diferente contenido de oxígeno.

Material para el **SLATCC**: [www.slatcc.com](https://www.slatcc.com/).

# 1. Medir también toma tiempo

En un cultivo, el pH y el oxígeno disuelto influyen en el entorno de las células. Para conocerlos usamos sensores, pero su lectura no cambia de manera instantánea cuando cambia el medio. La sonda necesita tiempo para responder y el equipo puede añadir procesamiento o filtrado a la señal.

Imagina que el oxígeno disminuye rápidamente: durante unos segundos, la pantalla podría mostrar un valor cercano al anterior. Si interpretamos esa lectura como si fuera instantánea, podemos reaccionar tarde o confundir el retraso de la medición con la dinámica del cultivo. Conocer la rapidez del sistema de medición ayuda a interpretar los datos y a tomar mejores decisiones de operación y control.

**Calibrar y medir el tiempo de respuesta son tareas distintas.** La calibración relaciona la señal con valores conocidos. La prueba de respuesta observa cuánto tarda la lectura en reflejar un cambio. Una sonda puede estar calibrada y responder lentamente.

# 2. ¿Qué cambiaremos y qué observaremos?

Mantendremos dos ambientes preparados y moveremos la sonda rápidamente de uno a otro. La transferencia debe ser breve, pero cuidadosa: “de golpe” significa cambiar el medio en poco tiempo, no golpear el sensor.

| Sensor | Medio inicial y final | Señal que registramos |
|---|---|---|
| pH | Buffer **pH 8 → pH 3**, después **pH 3 → pH 8** | pH indicado por Biostat |
| Oxígeno disuelto (O₂, OD o pO₂) | Agua equilibrada con **aire → agua con N₂**, después el sentido inverso | Oxígeno en % de saturación indicado por Biostat |

En pH medimos la respuesta de un electrodo. En oxígeno puede haber una sonda electroquímica u óptica: **primero registraremos su identificación y no supondremos su tecnología**. Biostat es el equipo que recibe y muestra la señal; no necesariamente es el fabricante de la sonda.

# 3. Tres formas de describir la respuesta

No siempre hay un instante único en que la señal “termina de cambiar”. Por eso acordaremos qué vamos a medir.

| Medida | Qué significa en esta práctica |
|---|---|
| **Inicio observable: t₁₀** | Tiempo desde la inmersión hasta recorrer el 10 % del cambio total. Es un umbral práctico; puede haber cambios menores antes. |
| **Tiempo de respuesta: t₉₀** | Tiempo desde la inmersión hasta recorrer por primera vez el 90 % del cambio. |
| **Tiempo de estabilización** | Primer instante en que la lectura entra en una banda alrededor del valor final y permanece allí al menos 30 s y hasta terminar el registro de ese ensayo. |

También calcularemos **t₁₀–₉₀ = t₉₀ − t₁₀**: cuánto tarda la parte central de la transición. Es útil para comparar curvas, pero no incluye todo el retraso desde la inmersión.

![Cambio ideal del medio y ejemplo de respuesta gradual del sistema de medición](../figuras/01_respuesta_didactica.png)

La figura es ilustrativa, no una medición de las sondas del taller. Para calcular los tiempos no necesitamos ajustar una ecuación exponencial ni resolver derivadas.

El 63.2 % nos interesa porque, en un modelo de primer orden, corresponde a una constante de tiempo (τ), que resume la rapidez de la respuesta. Una τ menor indica una respuesta más rápida; el 90 % se alcanza aproximadamente en 2.3 τ. Estas relaciones son aproximadas para una sonda real y, si hay un retraso inicial, se aplican después de descontarlo.

## La cuenta necesaria: una fracción del cambio

Llamaremos **y₀** a la lectura estable antes de transferir, **y_f** a la lectura final estable y **t₀** al instante en que la parte sensible queda sumergida en el líquido de destino. El tiempo transcurrido se cuenta desde t₀, no desde que empieza a moverse la pantalla.

$$y_{90} = y_0 + 0.90\,(y_f-y_0)$$

Para el 10 % se hace la misma cuenta sustituyendo 0.90 por 0.10. La resta $y_f-y_0$ puede ser negativa: la fórmula sirve tanto al subir como al bajar.

| Ejemplo didáctico | Cambio | Nivel al 10 % | Nivel al 90 % |
|---|---|---|---|
| pH: 8 a 3 | 3 − 8 = −5 | 8 − 0.5 = **7.5** | 8 − 4.5 = **3.5** |
| pH: 3 a 8 | 8 − 3 = 5 | **3.5** | **7.5** |
| O₂: 100 a 0 % | 0 − 100 = −100 puntos | **90 % de saturación** | **10 % de saturación** |

**Atención:** recorrer el 90 % de un descenso de oxígeno no significa llegar a 90 % de saturación. Usa las lecturas estables observadas: si los extremos son 80 y 12 %, el nivel al 90 % es $80 + 0.90(12-80) = 18.8$ % de saturación.

El pH es una escala logarítmica. Aquí describimos el porcentaje del recorrido de la **lectura de pH**, no el porcentaje de cambio de la concentración de iones hidrógeno.

## Banda de estabilización

Usaremos una banda de **±5 % del cambio total** alrededor de y_f:

$$b = 0.05\,|y_f-y_0|\qquad\text{banda: de }y_f-b\text{ a }y_f+b$$

Las barras indican tomar el tamaño del cambio sin su signo. Para una lectura de pH de 8 a 3, b = 0.25 unidades y la banda es 2.75–3.25. Para oxígeno de 80 a 12 %, b = 3.4 puntos y la banda es 8.6–15.4 % de saturación.

Esta banda es un criterio didáctico común para comparar ensayos; no es un criterio universal del fabricante. **Entrar una vez no basta:** si sale de la banda después, buscar una entrada posterior. Si no permanece dentro, escribir “no se estabilizó durante el tiempo observado”.

# 4. Objetivo y organización

**Objetivo:** identificar las sondas utilizadas y determinar t₁₀, t₉₀ y el tiempo de estabilización de las lecturas de pH y O₂, en ambos sentidos de transferencia. Comparar los resultados considerando temperatura, agitación, registro y condiciones de cada ensayo.

Cada uno de los tres equipos realiza las dos pruebas. Las seis personas se reparten estos roles:

1. **Identificación y trazabilidad:** lee etiquetas y llena la ficha de sensores, soluciones y condiciones.
2. **Operación:** transfiere la sonda con ayuda del instructor, sin desconectarla.
3. **Tiempo:** marca cada inmersión y registra la hora exacta de t₀.
4. **Adquisición:** comprueba el registro digital, la señal y las unidades; respalda las observaciones manuales.
5. **Gráfica y cálculo:** localiza niveles inicial/final y cruces del 10 y 90 %.
6. **Verificación y comparación:** revisa las cuentas, la permanencia en banda y la tabla de resultados.

# 5. Montaje y preparación

![Dos medios preparados para cada sensor; la sonda se transfiere manteniendo su conexión](../figuras/00_montaje.png)

## Para pH

Dos vasos identificados con **buffer pH 8** y **buffer pH 3**, a temperatura semejante y con agitación magnética suave y reproducible. Registrar el valor nominal, temperatura de referencia, lote o identificación y temperatura de uso. Usar volumen suficiente para cubrir la parte sensible y la unión de referencia, según la sonda.

Mantener los buffers separados y usar alícuotas frescas y volumen suficiente para reducir contaminación por arrastre. Antes de establecer la lectura inicial, acondicionar o enjuagar la sonda según su manual. **Durante la transferencia cronometrada no hacer un enjuague intermedio:** podría iniciar la respuesta antes del contacto con el vaso de destino. Dejar escurrir brevemente, sin frotar ni secar el bulbo, y transferir directamente con la misma técnica en ambos sentidos. Registrar el tiempo fuera de los vasos. La película de líquido arrastrada forma parte de las limitaciones del ensayo.

## Para O₂

Dos vasos con agua de la misma procedencia y a temperatura semejante. **Cada vaso debe tener agitación magnética y burbujeo continuo:** uno con aire y otro con nitrógeno (N₂). Prepararlos antes de que llegue el equipo. Mantener condiciones constantes durante los ensayos y registrar caudal si puede medirse, o ajuste y tipo de burbujeo si no.

El aire busca un nivel alto de oxígeno; el N₂ desplaza el oxígeno y busca uno bajo. No asumir que las lecturas serán exactamente 100 y 0 %. Comprobar que cada medio tiene una meseta antes de medir. Evitar burbujas adheridas a la punta, contacto con la barra magnética y cambios de profundidad.

**La prueba consiste en cambiar de vaso, no en cambiar de gas dentro del mismo vaso.** Si se empieza a burbujear N₂ justo al transferir, también se mide la desoxigenación del líquido y no se puede separar la respuesta de la sonda. No trasladar el valor de 0.5 vvm del taller de control a este montaje: aquí los caudales se registran por vaso y se eligen para mantener las condiciones preparadas.

El instructor maneja cilindros y reguladores. Usar N₂ en un espacio ventilado, mantener los recipientes con salida de gas y no presurizarlos; el nitrógeno puede desplazar el oxígeno del ambiente.

## Registro y estado del equipo

Antes del taller, el instructor comprueba hidratación y condición de la sonda de pH, calibración disponible y acondicionamiento del sensor de O₂ según su modelo. Algunas sondas electroquímicas requieren polarización; no asumir que eso aplica a todas. Registrar el filtrado o amortiguamiento de Biostat si puede consultarse.

Desactivar con el instructor cualquier actuación automática ligada a las sondas (bombas de ácido/base, gases o cascadas). Aquí **Biostat se usa para registrar**, no para controlar el pH u O₂ de los vasos. Mantener el filtrado igual en todos los ensayos.

Usar adquisición digital con el menor intervalo disponible, **idealmente 1 s o menos**, y confirmar el intervalo real al exportar. Una respuesta de pocos segundos no puede resolverse bien con lecturas cada 10 s. La hoja manual sirve de respaldo, no sustituye un registro rápido.

# 6. Identificar las sondas es parte de la práctica

Antes de transferir, el equipo localiza las etiquetas, las compara con el canal de pantalla y llena la ficha de la sección 9. **No desconectar ni desmontar la sonda para buscar datos.** Si la etiqueta no es accesible, consultar la documentación disponible o al instructor y anotar su origen.

Registrar fabricante, modelo, serie o ID de laboratorio y principio de medición cuando esté indicado. Añadir el estado visible y los datos de calibración disponibles. Si algo no se conoce, escribir **“no disponible”**, no completarlo por apariencia. Si no hay serie visible, asignar un ID temporal que identifique esa sonda durante el taller.

Esta información es parte del resultado: dos sensores con la misma variable medida pueden tener tecnologías, condiciones o ajustes diferentes. Un tiempo sin identificación y condiciones no puede compararse de manera confiable.

# 7. Procedimiento (máximo 45 min por equipo)

| Minutos | Actividad |
|---|---|
| 0–5 | Explicación de las medidas y reparto de roles. |
| 5–9 | Identificar ambas sondas, llenar sus fichas y verificar registro, soluciones y temperatura. |
| 9–20 | pH: lectura inicial en pH 8, transferencia a pH 3 y regreso a pH 8. Marcar t₀ en cada transferencia. |
| 20–22 | Comprobar los dos medios de O₂ y las condiciones de agitación y burbujeo. |
| 22–33 | O₂: aire → N₂ y N₂ → aire. Marcar t₀ y registrar cada transición. |
| 33–41 | Obtener niveles, calcular umbrales y leer tiempos en las gráficas. |
| 41–45 | Completar resultados, discutir límites y entregar el montaje al instructor. |

## Pasos que se repiten en cada transferencia

1. **Antes:** registrar una meseta inicial durante al menos 30 s. Como comprobación operativa, buscar un rango máximo de 0.05 unidades de pH o 2 puntos de O₂ en esos 30 s, sin tendencia evidente. Si no se cumple, estabilizar el montaje; son criterios del taller, no especificaciones de la sonda.
2. **Transferir:** mantener la conexión y minimizar el tránsito, sin un enjuague intermedio en el ensayo cronometrado. El cronometrista marca t₀ al completar la inmersión de la parte sensible en el destino. Registrar duración de transferencia y cualquier incidente.
3. **Observar:** mantener agitación, gas, profundidad y temperatura. Registrar aproximadamente 3–4 min por transición o hasta contar con una meseta final y confirmar 30 s dentro de la banda. No terminar al primer cruce del 90 %.
4. **Definir el final:** si hay una meseta sin tendencia evidente, usar como y_f el promedio de sus últimos 30 s. Comprobar la estabilidad con el mismo criterio del paso 1. Usar las lecturas medidas y no reemplazarlas por el pH nominal o un 0/100 % supuesto.
5. **Calcular:** promediar los 30 s iniciales para y₀, obtener y₁₀, y₉₀ y la banda final. Leer los instantes de cruce y restar t₀. Si el cruce queda entre dos muestras, reportar el intervalo o interpolar linealmente, indicando que se hizo.
6. **Comprobar la estabilización:** buscar la primera entrada que permanezca en banda hasta el fin del registro, con al menos 30 s de observación posterior. Anotar duración total. Al regresar, repetir como un ensayo nuevo, con su propio t₀ y sus propios niveles.

Si faltan mesetas, no fijar un y_f arbitrario. Registrar **“ensayo incompleto: no hay meseta final”** y la duración observada; no calcular t₉₀ usando la última lectura como si fuera el equilibrio. Si falta tiempo, trabajar el cálculo con el ejemplo o con el piloto, identificando la procedencia. No sustituir una dirección no ensayada por la otra.

# 8. Comparación y discusión

1. ¿Qué identificadores permiten reconocer cada sonda? ¿Qué información quedó pendiente y cómo podría verificarse?
2. ¿La primera señal de cambio, t₉₀ y la estabilización dieron el mismo tiempo? ¿Por qué pueden diferir?
3. ¿Fue igual ir de pH 8 a 3 que regresar? ¿Qué efecto pudieron tener el arrastre, el acondicionamiento y la temperatura?
4. ¿Por qué cambiar el gas en un mismo vaso no equivale a transferir entre dos medios preequilibrados?
5. ¿Qué parte de la respuesta puede venir de la sonda, del líquido, del tránsito y del filtrado de Biostat?
6. Si el registro es cada 1 s y una transición dura unos 8 s, ¿cuántos puntos la describen? ¿Qué pasaría al registrar cada 10 s?
7. ¿Se puede concluir que una sonda es mejor solo por ser más rápida? Considerar estabilidad, exactitud y aplicación.

# 9. Hoja de datos

**Equipo:** ______  **Fecha/hora:** ______  **Responsable del registro:** ______

## Identificación de los sensores

| Información | Sonda de pH | Sonda de O₂ |
|---|---|---|
| Fabricante | | |
| Modelo | | |
| Número de serie o ID de laboratorio/temporal | | |
| Principio de medición (si está documentado) | | |
| Canal y unidades en Biostat | | |
| Estado visible: punta, membrana/capuchón, cable | | |
| Fecha y referencias de calibración disponibles | | |
| Acondicionamiento/polarización, si aplica | | |
| Filtrado/amortiguamiento y fuente de ese dato | | |
| Origen de la información: etiqueta, manual, instructor | | |

**Equipo de lectura:** modelo/ID Biostat ______  **Archivo de registro:** ______  **Intervalo real:** ______ s

## Soluciones y condiciones

| Medio | Identificación/lote | Valor nominal o gas | Temperatura [°C] | Agitación y caudal/ajuste |
|---|---|---|---|---|
| Buffer A | | pH 8 | | |
| Buffer B | | pH 3 | | |
| Agua con aire | | Aire | | |
| Agua con N₂ | | N₂ | | |

**Acondicionamiento previo y técnica de transferencia de pH:** ______  **Observaciones del montaje:** ______

## Un registro por transferencia

Copiar o imprimir este bloque cuatro veces: pH 8 → 3, pH 3 → 8, O₂ aire → N₂ y O₂ N₂ → aire.

**ID de sonda:** ______  **Dirección:** ______  **t₀ (hora del archivo):** ______

**Duración de tránsito:** ______ s  **Ventana inicial:** ______ a ______  **Ventana final:** ______ a ______

| Tiempo desde t₀ [s] | Lectura | Tiempo desde t₀ [s] | Lectura |
|---|---|---|---|
| −30 | | 15 | |
| −15 | | 20 | |
| 0 | | 30 | |
| 1 | | 45 | |
| 2 | | 60 | |
| 3 | | 90 | |
| 5 | | 120 | |
| 8 | | 180 | |
| 10 | | 240 | |

Esta tabla resume puntos del registro; conservar el archivo digital completo. Anotar unidades y no redondear los tiempos a estas filas para localizar un cruce.

| y₀ | y_f | y₁₀ | y₉₀ | Banda final inferior–superior | Duración registrada |
|---|---|---|---|---|---|
| | | | | | |

## Resultados de las cuatro transferencias

| Ensayo e ID de sonda | t₁₀ [s] | t₉₀ [s] | t₁₀–₉₀ [s] | Estabilización [s] o motivo de no cálculo |
|---|---|---|---|---|
| pH 8 → 3 / ID: ______ | | | | |
| pH 3 → 8 / ID: ______ | | | | |
| O₂ aire → N₂ / ID: ______ | | | | |
| O₂ N₂ → aire / ID: ______ | | | | |

**Incidentes, incertidumbre de t₀, datos faltantes e interpretación:** ____________________

# Anexo para el instructor

## A. Preparar antes de los equipos

Preparar los cuatro medios y verificar las dos sondas con anticipación. La llegada del nitrógeno no debe ser parte del tiempo de 45 minutos. Probar burbujeo, mezcla, temperatura y adquisición. Tener etiquetas, fichas, calculadora y acceso al registro exportado. Confirmar que las salidas automáticas estén en un estado seguro.

Los participantes deben identificar las sondas por sí mismos. Dejar accesibles las etiquetas y documentos existentes; no proporcionarles un modelo supuesto. Si no es posible identificar la tecnología, el informe puede quedar con “no disponible”, pero debe conservar un ID que permita reconocer la sonda ensayada.

Los buffers **pH 8 y pH 3** corresponden al montaje confirmado para el taller. No están confirmados los valores nominales de los buffers del piloto. La lectura histórica no demuestra por sí sola qué buffer se usó.

## B. Qué contiene el archivo del 14 de octubre de 2026

`B2 Respuesta electrodos.xlsx` contiene las hojas **pH** y **OD**, con registros independientes. No sumar sus tiempos ni asumir continuidad entre ellas. La hoja pH abarca unos 142 min y la hoja OD unos 19 min. El intervalo mediano es aproximadamente **1.01 s**.

![Registros completos de las hojas pH y OD del piloto; cada eje temporal comienza en su propia hoja](../figuras/02_piloto_completo.png)

Se utiliza `ProcessTime`, expresado originalmente en horas, para reconstruir el tiempo transcurrido con resolución subsegundo. Hay marcas de reloj repetidas al final de las hojas. En pH también hay 15 filas con señales faltantes, cinco puntos con ambas señales en cero y un intervalo de unos 17 s sin muestreo; los ceros simultáneos se marcan como posibles artefactos y no se interpretan como transferencias. Los originales se conservan en el Excel.

El archivo no registra eventos de inmersión, gases, agitación, temperatura de los vasos, identidad de buffers ni modelo/serie de sondas. El setpoint de pH que aparece en la hoja pH no identifica la solución del vaso. Por eso **no permite obtener tiempos intrínsecos certificados** ni verificar todo el procedimiento propuesto.

## C. Qué tramos son útiles y cuáles no

| Tramo observado | Lectura de los datos | Uso en la enseñanza |
|---|---|---|
| pH, primer descenso (aprox. 95–160 s) | Cambio en varias etapas antes de acercarse a pH 3.3. | Mostrar por qué una transferencia o entrada mal definida impide fijar un t₀ confiable. |
| pH, segundo descenso (aprox. 1204 s) | Lectura de alrededor de 6.89 hacia 3.47, con una cola lenta. | Ejemplo exploratorio de t₉₀ y estabilización, declarando el inicio inferido. |
| pH, ascensos y registro prolongado | Recuperación lenta y deriva; la señal acaba cerca de 7.9 mucho después. | Discutir arrastre, acondicionamiento, cambios de medio y temperatura como posibilidades, no diagnósticos demostrados. |
| OD, antes de aprox. 836 s | Descensos lentos y variaciones con condiciones de entrada desconocidas. | No atribuirlos automáticamente al tiempo de la sonda ni a un ensayo aire → N₂ bien ejecutado. |
| OD, transición final ascendente | Paso rápido de alrededor de 12.6 a 77.2 % de saturación, con oscilación posterior. | Es el ejemplo más claro para visualizar una respuesta rápida; compatible con pasar de un medio de O₂ bajo a otro mayor. |

Según el relato de la sesión, el N₂ solo estuvo disponible al final. Esto ayuda a contextualizar el ensayo, pero el archivo **no marca el momento de su uso**. La transición final es ascendente: no presentarla como un descenso aire → N₂ ni como una medición independiente de los dos sentidos.

![Hoja OD: intentos previos y transición final; el inicio señalado se infirió de la señal](../figuras/04_OD_intentos.png)

## D. Ejemplos cuantitativos exploratorios

Los inicios de esta tabla se **infieren de las curvas**, no de una marca de transferencia. Se fijaron en 1204.15 s para el segundo descenso de pH y 836.25 s para el cambio final de OD, medidos desde el inicio de cada hoja. Los decimales localizan la muestra usada: no representan exactitud del evento físico.

![Ventanas seleccionadas del piloto con banda final y t90 aparente](../figuras/03_piloto_ventanas.png)

| Ventana ilustrativa | Lectura inicial → final | t₉₀ aparente [s] | t₁₀–₉₀ [s] | Estabilización aparente [s] |
|---|---|---|---|---|
| pH, segundo descenso | 6.89 → 3.47 | 50.8 | 50.6 | 149.2 |
| OD, cambio final ascendente | 12.64 → 77.22 % | 8.3 | 7.0 | 40.5 |

La estimación usa medianas en ventanas especificadas en `ventanas_piloto.json` para reducir la influencia de valores aislados; el cálculo manual del taller usa promedios de mesetas. Los cruces se interpolan linealmente sin filtrar la señal. La banda es ±5 % del cambio y se exige al menos 30 s dentro de ella y permanencia hasta el final de la ventana. Ver las ventanas, calidad y métricas completas en `resultados/piloto.json`.

Estos números dependen del origen inferido, de los niveles elegidos y de la duración de observación. **No son metas que los equipos deban reproducir.** En particular, el descenso lento previo de OD no es una segunda medición válida de la respuesta inversa. Un registro nuevo con t₀ marcado y medios preparados es el resultado principal del taller.

## E. Cómo evitar los problemas del piloto

| Si ocurre esto | Qué revisar o hacer |
|---|---|
| El medio con N₂ sigue bajando | Prepararlo antes y comprobar meseta; no medir la respuesta mientras el vaso se desoxigena. Si no se logra, declarar montaje no preparado. |
| El nivel bajo de O₂ queda lejos de cero | Revisar purga, entrada de aire, burbujas, calibración y tiempo de preparación. No forzar el cero ni recalibrar a mitad del ensayo para “corregir” la curva. |
| La señal cambia por etapas | Revisar tránsito, contacto con otros líquidos, profundidad y burbujas; marcar incidentes. No elegir retrospectivamente el comienzo más conveniente. |
| El pH deriva sin meseta | Revisar temperatura, buffer, arrastre, hidratación y referencia con el manual de la sonda. No sustituir una meseta ausente por el último dato. |
| La respuesta parece instantánea | Comprobar intervalo de adquisición y filtrado. Si ocurre entre dos muestras, reportar que no se resuelve con ese registro. |
| t₉₀ se alcanza, pero la lectura sigue oscilando | Separar cruce del 90 % y estabilización. Revisar mezcla y burbujas; no suavizar retrospectivamente para conseguir una cifra menor. |
| Falta el modelo o el manual | Conservar ID temporal, condiciones y “no disponible”. Comparar sistemas tal como se ensayaron sin exigir un tiempo de ficha técnica. |

Si no se consiguen las condiciones de O₂, usar el registro histórico como análisis de datos y declarar que no hubo una medición nueva válida. No presentar un cambio de gas en un solo vaso como equivalente al protocolo de transferencia.

# Nota final: qué tiempo estamos midiendo

El resultado incluye la **sonda, la película de líquido junto a ella, el procedimiento de transferencia y la adquisición/filtrado de Biostat**. Es un tiempo de respuesta observado del sistema de medición en las condiciones registradas. Una comparación con un fabricante requiere identificar modelo, tecnología, definición del tiempo (t₉₀, t₉₈, etc.), temperatura y condiciones de su ensayo.

Referencias de preparación de Hamilton: [respuesta de pH](https://www.hamiltoncompany.com/knowledge-base/article/response-time) y [referencias de oxígeno](https://www.hamiltoncompany.com/knowledge-base/article/do-sensor-calibration). No identifican las sondas del taller ni sustituyen sus manuales.
