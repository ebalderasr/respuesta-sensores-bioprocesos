# Respuesta de sensores en bioprocesos

| Simposio | Curso avanzado |
|:---:|:---:|
| [![XI Simposio Latinoamericano de Tecnología de Cultivos Celulares](docs/imagenes/Simposio_portada.png)](https://www.slatcc.com/) | [![Curso Avanzado de Tecnologías de Cultivo Celular 2026](docs/imagenes/Curso_portada.png)](https://www.slatcc.com/) |

Material educativo en español preparado para el **Simposio Latinoamericano de Tecnología de Cultivos Celulares (SLATCC)** y su actividad de formación en bioprocesos. Sitio del evento: **[www.slatcc.com](https://www.slatcc.com/)**.

El proyecto reúne una guía de taller, datos experimentales del **14 de octubre de 2026** y herramientas de análisis para identificar las sondas de pH y oxígeno disuelto y determinar su tiempo de respuesta con registro en Biostat. Está dirigido a personas de cultivo celular con distintos perfiles —biología, bioingeniería, genética y personal técnico—, sin requerir una formación matemática avanzada.

## La actividad

**Taller:** “Tiempo de respuesta de los sensores de pH y oxígeno disuelto”. **Organización:** 3 equipos de 6 personas, de forma sucesiva, con **45 minutos como máximo por equipo**.

| Aspecto | Descripción |
|---|---|
| Trabajo del equipo | Registrar fabricante, modelo, serie/ID, tecnología y calibración disponibles; realizar las transferencias **pH 8 → 3**, **pH 3 → 8**, **aire → N₂** y **N₂ → aire**. |
| Condiciones principales | Dos buffers preparados y dos vasos de agua preequilibrados con aire o N₂, ambos con burbujeo y agitación magnética. |
| Resultado | **t₁₀, t₉₀, t₁₀–₉₀ y estabilización** en una banda de ±5 % del cambio, asociados a cada sonda y sus condiciones. |

La guía contiene fundamentos accesibles, roles, procedimiento, hoja de datos y un anexo del instructor que distingue lo observado en el piloto de lo calculado después.

## Materiales y documentación

| Recurso | Contenido |
|---|---|
| [Guía Markdown](practica/Practica_respuesta_sensores.md) | Fuente editable de la práctica, fichas y notas del instructor |
| [Word](practica/Practica_respuesta_sensores.docx) y [PDF](practica/Practica_respuesta_sensores.pdf) | Versiones para edición, consulta e impresión |
| [Guía de reproducción y mantenimiento](docs/REPRODUCIBILIDAD.md) | Instalación, scripts, datos, interpretación y actualización de documentos |
| [Datos originales](B2%20Respuesta%20electrodos.xlsx) | Exportación del Biostat con las hojas pH y OD del piloto |
| [Datos procesados](datos_limpios/) | Registros y ventanas de análisis en CSV |
| [Resultados](resultados/) | Parámetros y métricas calculados, con su contexto |
| [Figuras](figuras/) | Montaje, respuesta didáctica y curvas reales del piloto |

## Inicio rápido

Desde la raíz del repositorio, con Python 3 instalado:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python analizar_respuesta.py
python -m unittest discover -s tests -v
```

Los scripts generan o actualizan archivos en `datos_limpios/`, `resultados/` y `figuras/`. La [guía de reproducción](docs/REPRODUCIBILIDAD.md) explica las entradas, decisiones del análisis y comprobaciones correspondientes a este taller.

## Actualizar Word y PDF

Se requieren **Pandoc** para generar Word y **LibreOffice** para exportar PDF desde la terminal:

```bash
python practica/generar_word.py
libreoffice --headless --convert-to pdf --outdir practica practica/Practica_respuesta_sensores.docx
```

El generador sobrescribe el Word a partir del Markdown. Si se editó el Word directamente, incorporar primero esos cambios a la fuente. Revisar visualmente el PDF después de generarlo. Los logos de esta página se conservan en `docs/imagenes/`; el formato de los documentos de la práctica procede de `plantilla_documento.docx`.

## Alcance de los resultados

El Excel no marca las transferencias ni identifica los buffers o las sondas. El N₂ solo estuvo disponible al final, según el relato de la sesión. Los inicios de las ventanas históricas son inferidos y sus tiempos son **aparentes**, no especificaciones certificadas. Los buffers pH 8 y pH 3 corresponden al taller; sus valores no se atribuyen retrospectivamente al piloto.

La transición final de OD es ascendente. Los descensos lentos anteriores no demuestran por sí solos la respuesta aire → N₂. Se mide el sistema completo de sonda, transferencia y adquisición; la información de identificación desconocida se anota como “no disponible”.

Los scripts están preparados para el formato de exportación y los datos incluidos en este repositorio. Revisar las condiciones y adaptar el análisis antes de usar nuevos registros.

## Taller complementario

[Control de oxígeno en biorreactores](https://github.com/ebalderasr/control-oxigeno-biorreactores): Dinámica del oxígeno disuelto y afinación de un controlador PI. Ambos repositorios comparten organización y presentación para facilitar su uso conjunto.

## Autor

**Emiliano Balderas · Instituto de Biotecnología, UNAM**.
