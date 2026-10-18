# Respuesta de sensores en bioprocesos

Material en español para determinar el **tiempo de respuesta de sondas de pH y oxígeno disuelto**, preparado para el **SLATCC**: [www.slatcc.com](https://www.slatcc.com/).

La práctica está dirigida a personas de cultivo celular con distintos perfiles y usa el mismo estilo del taller de [control de oxígeno en biorreactores](https://github.com/ebalderasr/control-oxigeno-biorreactores): explicación accesible, procedimiento de hasta 45 min, roles, hoja de datos y notas del instructor apoyadas en el piloto del 14 de octubre de 2026.

## Actividad

**Tres equipos de seis personas**, de forma sucesiva. Cada equipo identifica las sondas y registra fabricante, modelo, serie/ID, tecnología y datos de calibración disponibles. La información desconocida se anota como “no disponible”. Después realiza cuatro transferencias:

- pH **8 → 3** y **3 → 8**, entre buffers preparados.
- O₂ **aire → N₂** y **N₂ → aire**, entre dos vasos preequilibrados, ambos con burbujeo y agitación magnética.

Se determinan el inicio observable (t₁₀), el tiempo al 90 % (t₉₀), t₁₀–₉₀ y la estabilización en una banda de ±5 % del cambio. La ficha vincula cada resultado con su sonda y condiciones. Se mide el sistema completo de sonda, transferencia y adquisición, sin asumir especificaciones de modelos no identificados.

## Materiales

| Recurso | Contenido |
|---|---|
| [Guía Markdown](practica/Practica_respuesta_sensores.md) | Práctica, fichas de identificación y anexo del instructor |
| [Word](practica/Practica_respuesta_sensores.docx) y [PDF](practica/Practica_respuesta_sensores.pdf) | Material para editar, consultar e imprimir |
| [Datos originales](B2%20Respuesta%20electrodos.xlsx) | Hojas pH y OD del Biostat |
| [Figuras](figuras/) | Montaje, respuesta didáctica y curvas reales del piloto |
| [Resultados exploratorios](resultados/piloto.md) | Referencias cuantitativas con límites de interpretación |
| [Reproducción y mantenimiento](docs/REPRODUCIBILIDAD.md) | Datos, decisiones del análisis, comandos y comprobaciones |

## Reproducir

Desde la raíz del repositorio, con Python 3:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python analizar_respuesta.py
python -m unittest discover -s tests -v
```

Para generar Word se necesita además Pandoc instalado en el sistema; LibreOffice permite exportarlo a PDF:

```bash
python practica/generar_word.py
libreoffice --headless --convert-to pdf --outdir practica practica/Practica_respuesta_sensores.docx
```

## Límites del piloto

El Excel no marca las transferencias ni identifica los buffers o las sondas. El N₂ solo estuvo disponible al final, según el relato de la sesión. Los inicios de las ventanas históricas son inferidos y sus tiempos son **aparentes**, no especificaciones certificadas. Los buffers pH 8 y pH 3 corresponden al taller propuesto; sus valores no se atribuyen retrospectivamente al piloto.

La transición final de OD es ascendente. Los descensos lentos anteriores no demuestran por sí solos la respuesta de la sonda en el sentido aire → N₂. La guía explica cómo evitar esa confusión preparando ambos líquidos antes del ensayo.

Autor: **Emiliano Balderas · Instituto de Biotecnología, UNAM**.
