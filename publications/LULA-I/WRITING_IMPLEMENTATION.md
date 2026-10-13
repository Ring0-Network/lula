# Ejecución de las 17 propuestas de redacción

Las **17 propuestas R01–R17 están aplicadas** al manuscrito actual, conservando las revisiones posteriores de familia, abstract y bibliografía. El documento completo actualizado está en `LULA-I.tex` y en el PDF compilado de 34 páginas. El análisis original de `editorial/writing-r6` se conserva como registro histórico; esta ejecución y su verificación están en `editorial/writing-r9`.

## Cambios aplicados

| Propuesta | Resultado |
|---|---|
| R01 | La sección 13 se titula “Historical measurements and publication replay” y distingue su contenido de la campaña comparativa. |
| R02 | La sección 11 se titula “Signature format and computation costs”; no promete una selección de parámetros que no desarrolla. |
| R03 | La oración de invariancia nombra los bytes de firma y explicita las condiciones de caché honesta. La corrección anterior del sustantivo se conserva. |
| R04 | La campaña empieza por las operaciones medidas; conserva fecha, corte, controladores, procesos, archivos y límites de conformidad. |
| R05 | Se elimina una recapitulación local, preservando terminación, evidencia emitida y la necesidad de acoplar transcripciones para el caso aleatorizado. |
| R06 | La leyenda de CacheRestore explica lookup y recomputación. El nombre público y todo el pseudocódigo se conservan. |
| R07 | El modelo geométrico ideal y su aplicación con contadores finitos quedan en párrafos contiguos; las fórmulas y condiciones son las mismas. |
| R08 | KeyGen, y no la tupla del esquema, aparece como actor que devuelve las claves y el estado inicial. |
| R09 | La leyenda del contraejemplo identifica las observaciones anteriores que conserva el adversario; no le atribuye las publicaciones del firmante. |
| R10 | La mediana se calcula entre las sumas carga+firma de cada proceso, conservando la exclusión del arranque y la advertencia sobre medianas marginales. |
| R11 | El máximo de 100,586 tiene unidad explícita de compresiones instrumentadas y permanece como máximo de una muestra. |
| R12 | La diferencia del modelo de coste se expresa en compresiones; el valor y la fórmula no cambian. |
| R13 | El mapa final incluye diferencias de terminación además de diferencias de bytes, bajo sus premisas. No promete terminación universal. |
| R14 | Los criterios de inclusión y las etiquetas del resumen de campaña se nombran directamente. Se integra en el mismo párrafo que R04. |
| R15 | Se comparan medianas con medianas y se explicita por qué no existe un ranking a un nivel de seguridad común. |
| R16 | Se identifican las cargas externas concurrentes y las interrupciones de planificación, manteniendo los cuatro factores no controlados del replay. |
| R17 | Se fusiona la recapitulación de clases de evidencia, preservando históricos, replay, campaña, preparación y las dos llamadas sin caché. |

El registro literal original → revisión, localizadores y obligaciones protegidas de cada propuesta está en `editorial/writing-r9/CHANGELOG.json`. R03 se adaptó a la corrección ya existente de la revisión de familia; R15 explicita “than those of” para comparar medianas. R04/R14 comparten un párrafo final y se verificaron conjuntamente además de por separado. No se reemplazó todo el paper por una voz editorial nueva.

## Verificación

Un agente cotejó cada uno de los 17 cambios con el texto original congelado y sus condiciones de preservación. Registró **17/17 PASS_WITHIN_LISTED_CHECKS**, con las verificaciones de conservación y adición documentadas en `editorial/writing-r9/agents/SEMANTIC_REVIEW.md` y `.json`. Esta comparación manual estructurada no constituye una prueba formal de equivalencia semántica ni una certificación criptográfica.

Las comprobaciones sobre archivos confirman:

- Abstract, bibliografía, metadatos de envío y resultados del replay: idénticos byte a byte a la versión anterior a esta ejecución.
- Tres pruebas, dos diagramas TikZ, cinco ecuaciones numeradas, dos bloques align y cuerpos de los cinco algoritmos: sin cambios. Se modificaron únicamente las dos leyendas autorizadas.
- Las 14 tablas distintas del mapa final: sin cambios. En el mapa sólo cambió el texto del falsificador de transparencia; no sus valores ni otras filas.
- Claves de cita, localizadores bibliográficos y etiquetas LaTeX: conservados. Siguen presentes las 12 referencias citadas, las 20 citas y los 17 destinos externos completos del PDF.
- R04, R10 y R14 también están en `scripts/integrate_comparison.py`, para que la regeneración conserve las correcciones.
- Compilación correcta, 34 páginas A4, cero referencias pendientes y cero desbordamientos. Se inspeccionaron todas las páginas renderizadas y, en detalle, las leyendas y el mapa final.

No se hicieron nuevos benchmarks ni se alteraron implementaciones o datos crudos. Se mantienen las limitaciones experimentales y la obligación abierta de establecer la cota del firmante de referencia. La separación entre restauración honesta y corrupción, entre validez y unforgeability, y entre máximo observado y garantía permanece explícita.

**Estado editorial: COMPLETE_WITHIN_SCOPE.** No quedan propuestas R01–R17 bloqueadas ni preguntas de autor necesarias para esta ejecución. Las obligaciones científicas abiertas del paper no se declaran resueltas por mejorar su redacción.
