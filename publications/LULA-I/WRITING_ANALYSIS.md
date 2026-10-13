# Análisis completo de redacción de LULA I

**El paper requiere mejoras locales de precisión, orientación y ritmo; esta revisión no encontró un defecto crítico de redacción ni una retórica grandilocuente dominante.** El problema más visible es la mezcla de lenguaje científico con vocabulario de auditoría y algunas recapitulaciones. Tampoco está justificado borrar en bloque sus advertencias: muchas preservan exactamente las condiciones de la transferencia y la interpretación de las mediciones.

Se revisó la versión de **34 páginas**, con tres agentes que leyeron independientemente todo el texto y repartieron los **97 nodos Markdown de writing-skill** (33/32/32). El principal revisó además los siete archivos auxiliares no Markdown; el revisor de estructura leyó los 25 nodos del marco phd-paper-review. La cobertura incluye título, abstract, 19 secciones principales contando la comparación y apéndices, 56 encabezados de sección/subsección/párrafo, 24 leyendas, 15 tablas, 4 figuras, 5 algoritmos, 3 pruebas y bibliografía. Las fuentes tipográficas completas, no sólo fragmentos del PDF, fueron el sujeto textual.

Los tres revisores registraron 19 propuestas. Dos coincidencias se fusionaron: la agencia de la leyenda de ramas y la recapitulación del párrafo sobre estado no determinista. Quedan **17 registros de propuesta**, no 17 causas independientes ni un porcentaje de «escritura IA». La etiqueta moderada de algunas observaciones locales del revisor de afirmaciones se normalizó a MINOR: el contexto ya permite recuperar el sentido correcto y no se demostró una inversión del resultado. El informe conserva las clasificaciones originales y sus argumentos en los JSON de cada agente.

La petición actual es de **análisis con propuestas**, por lo que no se modificó el manuscrito, PDF, datos, fuentes públicas ni Page. Cada fragmento inglés siguiente es una propuesta que debe cotejarse nuevamente si se integra. El PDF permanece SHA-256 `c25d36018c1d28814c788a2d07ad4a8f2e3ffbf0c21a3e64239027ce781a22db`.

## Lo que conviene corregir primero

1. **Orientar las secciones por su contenido.** “Parameter selection” promete una explicación de selección que el apartado no desarrolla; “Experimental evaluation” no anuncia que allí se mezclan históricos y replay, antes de otra campaña. R01–R02.
2. **Nombrar operaciones y objetos sin elipsis.** Aclarar que KeyGen devuelve las claves; que el adversario conserva observaciones; que la mediana se calcula entre sumas por proceso; y que los “calls” aquí son compresiones. R08–R12.
3. **Dar prioridad a la pregunta del experimento sobre su auditoría.** La apertura actual empieza con controladores y digests; puede empezar por qué operaciones se evaluaron y conservar toda la trazabilidad. Sustituir jerga poco transparente como “admitted latency samples” y “secure-winner claim”. R04, R13–R14.
4. **Separar ideas sin simplificar matemáticamente.** El párrafo geométrico acumula modelo infinito, límite finito, fallo y cuantila conjunta. Dividirlo, sin alejar sus condiciones, mejora el ritmo. R07.
5. **Quitar sólo repeticiones cuyo trabajo ya está hecho.** Dos recapitulaciones locales repiten la oración inmediatamente anterior. No es motivo para borrar las condiciones del abstract, teorema, figuras o conclusión. R05, R17.
6. **Alinear el resumen final con el enunciado central.** El mapa de falsificadores puede representar también la equivalencia de terminación del lema; ahora muestra sólo bytes distintos. Es una mejora del resumen, no un fallo nuevo de la prueba. R13.

## Valoración editorial

Las puntuaciones siguientes son juicios cualitativos del revisor de estructura sobre el texto completo, corroborados en alcance por los otros revisores. No son mediciones calibradas, promedio global, probabilidad de aceptación ni validación científica.

| Dimensión | /5 | Motivo |
|---|---:|---|
| Cohesión | 4 | Los referentes se recuperan; algunas etiquetas pueden nombrar mejor sus objetos. |
| Coherencia | 4 | El argumento central es recuperable; títulos y apertura experimental pueden orientar mejor. |
| Cadencia | 3 | Un párrafo mezcla modelo ideal, dominio finito y cotas; dividirlo preservando las condiciones ayuda. |
| Calidad léxica | 4 | Terminología técnica estable; jerga de auditoría y un par de unidades abreviadas necesitan precisión. |
| Argumentación | 4 | Se mantienen premisas y ámbitos de evidencia; el mapa final debe reflejar ambas partes de transparencia. |
| Registro académico | 4 | Predomina una voz sobria; la procedencia de ejecución desplaza algunas veces la pregunta científica. |
| Convenciones de sección | 4 | Algunos encabezados prometen selección o evaluación general en lugar de su contenido específico. |
| Gramática y mecánica | 4 | No se confirmó un defecto gramatical central; quedan elipsis y referencias mejorables. |

Valoración global de esa revisión: **4/5**, con mayor atención a cadencia. La contribución, el teorema condicionado y las limitaciones experimentales se pueden recuperar. No hay fundamento editorial suficiente para recomendar una reescritura total.

## Literatura sobre patrones de escritura de LLM

Se consultaron siete estudios primarios; método, resultados y límites de acceso están en [LITERATURE.md](C:/Users/angel/Desktop/paper/PAPERS/LUGEL/research/lula22/publications/LULA-I/editorial/writing-r6/LITERATURE.md). Es una selección orientada al encargo, no una revisión sistemática exhaustiva. Los trabajos motivan inspecciones; los pasajes de LULA I aportan la evidencia de cada defecto.

| Fuente | Inspección pertinente | Transferencia que se evita |
|---|---|---|
| [Reinhart et al., PNAS 2025](https://arxiv.org/abs/2410.16107) | Relaciones gramaticales, nominalizaciones y participios | Prohibir toda construcción nominal o participial |
| [Miletić y Falk, LREC 2026](https://aclanthology.org/2026.lrec-1.142/) | Variación y experiencia de lectura | Suponer que estilo asociado a LLM siempre empeora la claridad |
| [Jiang y Hyland, Applied Linguistics](https://kevinjiang.home.blog/wp-content/uploads/2024/09/does-chatgpt-argue-like-students_bundles-in-argumentative-essays.pdf) | Función de frases repetidas y organización discursiva | Tratar un patrón de ensayos como plantilla universal de papers |
| [Peters y Chin-Yee, RSOS 2025](https://doi.org/10.1098/rsos.241776) | Conservar alcance, tiempo y modalidad | Confundir observación con garantía o condenar el presente de un teorema |
| [Kobak et al., Science Advances 2025](https://github.com/berenslab/llm-excess-vocab) | Énfasis léxico sin contenido; versiones en nota de acceso | Aplicar frecuencias poblacionales a la autoría de un documento |
| [Rallapalli et al., preprint 2026](https://arxiv.org/html/2604.14111v1) | Control por género | Comparar criptografía con ficción o charla informal |
| [Liang et al., Patterns 2023](https://arxiv.org/html/2304.02819v3) | Evitar falsos positivos de atribución | Penalizar inglés no nativo o dar un porcentaje de autoría IA |

La distinción clave es **rasgo → posible problema → defecto demostrado**. Un rasgo sólo se convierte en hallazgo cuando oculta un actor, una relación, un ámbito o una pregunta del lector. Esta revisión no usó detectores ni intentó evadirlos.

## Pasajes y propuestas verificables

Todas las citas se comprobaron contra la línea original y su presencia única en las fuentes congeladas. Los localizadores siguientes apuntan al manuscrito sin modificar. Las ecuaciones y condiciones de los fragmentos pertenecen al autor; ninguna propuesta añade una reducción, benchmark o mecanismo nuevo.

### R01 — Distinguir históricos/replay de la campaña — MINOR

Fuente: [LULA-I.tex:471](C:/Users/angel/Desktop/paper/PAPERS/LUGEL/research/lula22/publications/LULA-I/editorial/writing-r6/baseline/LULA-I.tex:471). Revisor: structure; registro STR-01.

**Pasaje exacto**

```latex
\section{Experimental evaluation}
```

**Diagnóstico**

El título general de la sección13 no anuncia que aquí se presentan los históricos y el replay de un fixture, mientras que la campaña comparativa es otra sección. La diferencia se recupera leyendo los métodos, pero el lector debe reconstruir la jerarquía de evidencia.

**Propuesta inglesa, no aplicada**

```latex
\section{Historical measurements and publication replay}
This section reports historical measurements and the fixed-fixture publication replay. The separately frozen implementation campaign is presented in \Cref{sec:benchcomparison}.
```

**Lectura legítima alternativa**

Separar ambas secciones ya protege la procedencia; un lector que lea de corrido puede distinguirlas sin una nueva frase. La propuesta mejora navegación, no corrige una contradicción.

**Conservar al integrar**

- Mantener muestras, entorno, fixture único, negativos, cronología y convención de cuantiles de cada grupo.
- No trasladar ni fusionar cifras de campañas distintas.
- La frase propuesta usa sólo clases de evidencia ya presentes.

### R02 — El encabezado promete selección de parámetros — MINOR

Fuente: [LULA-I.tex:381](C:/Users/angel/Desktop/paper/PAPERS/LUGEL/research/lula22/publications/LULA-I/editorial/writing-r6/baseline/LULA-I.tex:381). Revisor: structure; registro STR-02.

**Pasaje exacto**

```latex
\section{Parameter selection, signature size, and computation}
```

**Diagnóstico**

“Parameter selection” promete un criterio o procedimiento de elección. La sección expone formato y costes del conjunto fijado, con efectos analíticos de los parámetros, sin desarrollar por qué fue escogido frente a otros.

**Propuesta inglesa, no aplicada**

```latex
\section{Signature format and computation costs}
```

**Lectura legítima alternativa**

Los efectos de los parámetros pueden entenderse como orientación para seleccionar. No se infiere que los autores nunca hicieron selección; se observa qué explica esta sección.

**Conservar al integrar**

- Preservar el conjunto fijo y todas sus fórmulas, contadores y condiciones.
- No inventar una búsqueda de parámetros ni una razón técnica ausente.

### R03 — “Evidence” cambia de objeto según el contexto — MINOR

Fuente: [LULA-I.tex:51](C:/Users/angel/Desktop/paper/PAPERS/LUGEL/research/lula22/publications/LULA-I/editorial/writing-r6/baseline/LULA-I.tex:51). Revisor: structure; registro STR-03.

**Pasaje exacto**

```latex
The cache affects computation time rather than the published evidence.
```

**Diagnóstico**

“Evidence” designa aquí la firma emitida; en otras secciones designa pruebas y observaciones. El contexto resuelve el referente, pero “signature bytes” evita esa doble función léxica en una afirmación central.

**Propuesta inglesa, no aplicada**

```latex
Under these honest cache conditions, the cache changes computation time while preserving the signature bytes whenever signing terminates.
```

**Lectura legítima alternativa**

“Published evidence” puede ser una elección deliberada para expresar autorización verificable. La sustitución se limita a este caso, donde la frase anterior habla de la misma firma; no se reemplaza “evidence” globalmente.

**Conservar al integrar**

- Conservar clave y mensaje fijos, caché honesta y terminación.
- No afirmar invariancia de tiempo, de observaciones de fuga ni de cachés corruptas.

### R04 — La apertura experimental empieza como un registro de ejecución — MINOR

Fuente: [comparison-results.tex:3](C:/Users/angel/Desktop/paper/PAPERS/LUGEL/research/lula22/publications/LULA-I/editorial/writing-r6/baseline/comparison-results.tex:3). Revisor: structure; registro STR-04.

**Pasaje exacto**

```latex
This section incorporates the campaign's final retained execution cut, frozen at 14:52 UTC on 12 October 2026. All four controllers have completion markers; all 81 recorded processes completed with exit code zero. We independently checked the 477 retained file digests and recomputed distributions from 64 campaign CSV files, excluding smoke tests. Process completion establishes that scheduled jobs ended, not that every implementation is conformant or that the original experimental protocol is complete. Quiet-host trials, equivalent backends and a common-security cohort remain absent. The tables use raw observations and explicit admission boundaries rather than inherited summary labels.
```

**Diagnóstico**

El inicio de la sección14 antepone controladores, archivos y cierre de procesos antes de indicar qué pregunta empírica aborda la campaña. La trazabilidad sirve al estudio, pero presentada primero hace que el lector entre en un informe de ejecución. Se propone orientar con operaciones ya medidas y conservar todos los datos de procedencia.

**Propuesta inglesa, no aplicada**

```latex
The campaign recorded signing and verification latencies, initialization costs, and LULA I fixed-snapshot behavior. Its final retained record was frozen at 14:52 UTC on 12 October 2026. All four controllers have completion markers, and all 81 recorded processes completed with exit code zero. We independently checked the 477 retained file digests and recomputed distributions from 64 campaign CSV files, excluding smoke tests. Process completion establishes that scheduled jobs ended; it does not establish conformance or completion of the original experimental protocol. Quiet-host trials, equivalent backends and a common-security cohort remain absent. The tables use raw observations and explicit admission boundaries rather than inherited summary labels.
```

**Lectura legítima alternativa**

La auditoría de procedencia es una parte real de la contribución y protege frente a resúmenes heredados. El orden actual es defendible; no debe suprimirse la trazabilidad ni presentarse su revisión como prueba criptográfica.

**Conservar al integrar**

- Mantener corte 14:52 UTC, fecha, cuatro controladores, 81 procesos, 477 digests, 64 CSV y exclusión de smoke.
- La apertura propuesta enumera operaciones existentes; no exige todas esas operaciones a cada implementación.
- Conservar límites de conformidad, protocolo y comparación de seguridad.

### R05 — Una recapitulación interrumpe el avance hacia el caso aleatorizado — MINOR

Fuente: [LULA-I.tex:325](C:/Users/angel/Desktop/paper/PAPERS/LUGEL/research/lula22/publications/LULA-I/editorial/writing-r6/baseline/LULA-I.tex:325). Revisor: structure; registro STR-05.

**Pasaje exacto**

```latex
State need not consist exclusively of deterministic key-derived bytes. A diagnostic counter or random eviction policy can be harmless if it preserves termination behavior and emitted evidence in the declared interface. The relevant requirement is the signing behavior in the declared security interface. For randomized reference signers, equality of separate marginal distributions at each frozen state is insufficient when restored randomness creates correlations across calls; a joint transcript coupling is required.
```

**Diagnóstico**

La oración “The relevant requirement...” repite el criterio de comportamiento que acaba de formular la condición del ejemplo y que ya establece el teorema. El párrafo gana continuidad al pasar del ejemplo permitido al caso aleatorizado sin esa recapitulación.

**Propuesta inglesa, no aplicada**

```latex
State need not consist exclusively of deterministic key-derived bytes. A diagnostic counter or random eviction policy can be harmless if it preserves termination behavior and emitted evidence in the declared interface. For randomized reference signers, equality of separate marginal distributions at each frozen state is insufficient when restored randomness creates correlations across calls; a joint transcript coupling is required.
```

**Lectura legítima alternativa**

La oración puede funcionar como bisagra pedagógica hacia el caso aleatorizado. Si el autor quiere enfatizar la idea, conservarla es razonable; no se diagnostica circularidad de la prueba ni se elimina el caso aleatorizado.

**Conservar al integrar**

- Preservar terminación y evidencia emitida en el ejemplo de estado no determinista.
- Preservar la distinción entre distribuciones marginales y acoplamiento de transcripciones.
- El criterio general conserva representación en el teorema; una aplicación futura necesitaría comparación bidireccional.

Coincidencia fusionada: patterns/PT05.

### R06 — CacheRestore puede confundirse con restauración persistente — MINOR

Fuente: [LULA-I.tex:254](C:/Users/angel/Desktop/paper/PAPERS/LUGEL/research/lula22/publications/LULA-I/editorial/writing-r6/baseline/LULA-I.tex:254). Revisor: structure; registro STR-06.

**Pasaje exacto**

```latex
\caption{LULA I CacheRestore and cache-miss handling}
```

**Diagnóstico**

“CacheRestore” en el caption puede sugerir que el algoritmo restaura una snapshot persistente, aunque describe lookup y recomputación. Esa distinción aparece después del pseudocódigo. Un caption descriptivo permite entender el algoritmo aislado.

**Propuesta inglesa, no aplicada**

```latex
\caption{LULA I CacheRestore: cache lookup and cache-miss recomputation}
```

**Lectura legítima alternativa**

CacheRestore puede ser un nombre público deliberado de la operación. En ese caso conservar el nombre y añadir “lookup and recomputation” sería una alternativa; no se cambia un identificador ejecutable sin autorización.

**Decisión de consolidación**

Preserve CacheRestore as the existing public algorithm name; clarify caption rather than silently renaming the operation.

**Conservar al integrar**

- No cambiar cuerpo, guards, orden ni interfaz del algoritmo.
- No atribuir persistencia, codec o validación de integridad.
- No confundir lookup con Restore(u) del juego.

### R07 — Modelo infinito y aplicación finita en una sola unidad de lectura — MINOR

Fuente: [LULA-I.tex:439](C:/Users/angel/Desktop/paper/PAPERS/LUGEL/research/lula22/publications/LULA-I/editorial/writing-r6/baseline/LULA-I.tex:439). Revisor: structure; registro STR-07.

**Pasaje exacto**

```latex
For an idealized unbounded sequence of independent uniform candidate digests, the trial-count proxy for $G_F$ is geometric with success probability $2^{-9}$. At layer $j$, let $\nu_j=[x^{S_j}](1+x+\cdots+x^{w_j-1})^{\ell_j}$. Its search success probability is $p_j=\nu_j/w_j^{\ell_j}$. The unbounded geometric proxy has mean $1/p_j$ and tail $(1-p_j)^t$. The tail law describes executable trials only while counters remain distinct, with $t\le 2^{32}$. Under the independence premise, the event that all $N=2^{32}$ candidates are rejected has probability $(1-p_j)^N$; this model does not establish that every executable search terminates. A confidence budget split among all five online searches gives a probabilistic work quantile through a union bound. It does not give certified worst-case time.
```

**Diagnóstico**

Una sola unidad de lectura combina la variable geométrica ideal, la ley finita de supervivencia, el fallo en 2^32 candidatos y el límite de una cuantila conjunta. La relación es válida en el texto, pero separar el modelo ideal de su aplicación ejecutable reduce carga sin tocar una palabra matemática.

**Propuesta inglesa, no aplicada**

```latex
For an idealized unbounded sequence of independent uniform candidate digests, the trial-count proxy for $G_F$ is geometric with success probability $2^{-9}$. At layer $j$, let $\nu_j=[x^{S_j}](1+x+\cdots+x^{w_j-1})^{\ell_j}$. Its search success probability is $p_j=\nu_j/w_j^{\ell_j}$. The unbounded geometric proxy has mean $1/p_j$ and tail $(1-p_j)^t$.

The tail law describes executable trials only while counters remain distinct, with $t\le 2^{32}$. Under the independence premise, the event that all $N=2^{32}$ candidates are rejected has probability $(1-p_j)^N$; this model does not establish that every executable search terminates. A confidence budget split among all five online searches gives a probabilistic work quantile through a union bound. It does not give certified worst-case time.
```

**Lectura legítima alternativa**

Mantener las condiciones en el mismo párrafo reduce el riesgo de que alguien cite el modelo ideal sin sus límites. La separación debe conservar continuidad explícita; no se recomienda extraer la advertencia a una nota o apéndice.

**Conservar al integrar**

- Sólo insertar un salto de párrafo.
- Preservar distribución ideal, independencia, todas las fórmulas, t <= 2^32, no totalidad y ausencia de WCET.
- F24 aquí es un control de regresión de una futura simplificación, no atribución de autoría.

### R08 — Precisar quién devuelve las claves — MINOR

Fuente: [LULA-I.tex:95](C:/Users/angel/Desktop/paper/PAPERS/LUGEL/research/lula22/publications/LULA-I/editorial/writing-r6/baseline/LULA-I.tex:95). Revisor: claims; registro CLAIM-01.

**Pasaje exacto**

```latex
Let $\Pi=(\KG,\Sign,\Vf)$ return a public key $pk$, a secret key $sk$, and initial mutable state $\mu_0$.
```

**Diagnóstico**

La tupla que define un esquema queda como sujeto de return. En una definición de juego, el lector debe recuperar que KeyGen, no la tupla, produce las claves y el estado.

**Propuesta inglesa, no aplicada**

```latex
Let $\Pi=(\KG,\Sign,\Vf)$ be a signature scheme whose key-generation algorithm $\KG$ returns a public key $pk$, a secret key $sk$, and initial mutable state $\mu_0$.
```

**Lectura legítima alternativa**

Un criptógrafo puede leerlo como abreviatura convencional. La forma anterior sigue requiriendo esa elipsis cuando justo se define la interfaz.

**Conservar al integrar**

- Misma tupla y mismos tres resultados.
- No añadir aleatoriedad, uniformidad, tiempo de generación o garantías de producción.

### R09 — El adversario observa la evidencia; no es quien la publica — MINOR

Fuente: [LULA-I.tex:343](C:/Users/angel/Desktop/paper/PAPERS/LUGEL/research/lula22/publications/LULA-I/editorial/writing-r6/baseline/LULA-I.tex:343). Revisor: claims; registro CLAIM-02.

**Pasaje exacto**

```latex
restoration does not erase the adversary's publications
```

**Diagnóstico**

Publications atribuye al adversario la emisión que, en el relato y el diagrama, realiza el firmante. Lo permanente es lo que el adversario ha observado entre ramas.

**Propuesta inglesa, no aplicada**

```latex
restoration does not erase the adversary's earlier observations
```

**Lectura legítima alternativa**

Publications podría ser metonimia del transcript que el adversario conserva. Es una lectura recuperable, pero cambia quién publica la evidencia.

**Decisión de consolidación**

Minimal noun repair; avoids implying an additional distinct class of published objects. The surrounding share/signature relations remain.

**Conservar al integrar**

- Mantener la independencia individual de cada share respecto de sk.
- Mantener las dos ramas y la persistencia del transcript.
- No atribuir al adversario nuevas capacidades de publicación o lectura de estado secreto.

Coincidencia fusionada: patterns/PT03.

### R10 — La mediana se obtiene entre procesos — MINOR

Fuente: [comparison-results.tex:82](C:/Users/angel/Desktop/paper/PAPERS/LUGEL/research/lula22/publications/LULA-I/editorial/writing-r6/baseline/comparison-results.tex:82). Revisor: claims; registro CLAIM-03.

**Pasaje exacto**

```latex
\Cref{tab:comparison-recovery} reports the median of each process's load-plus-sign sum; adding marginal medians would be incorrect.
```

**Diagnóstico**

Cada proceso aporta una suma escalar, no una mediana propia. El singular distributivo each process's puede inducir una agregación distinta de la que la tabla y el párrafo posterior especifican.

**Propuesta inglesa, no aplicada**

```latex
\Cref{tab:comparison-recovery} reports the median across the per-process load-plus-sign sums; adding marginal medians would be incorrect.
```

**Lectura legítima alternativa**

En habla corriente median of each puede entenderse como mediana de la colección. La repetición precisa posterior resuelve el sentido, pero se puede evitar la ambigüedad local.

**Conservar al integrar**

- Diez procesos, una misma clave y primer mensaje.
- Sumar carga y firma dentro de cada proceso antes de calcular mediana.
- Excluir arranque del proceso y no sumar medianas marginales.

### R11 — Precisar la unidad del máximo de trabajo — MINOR

Fuente: [LULA-I.tex:441](C:/Users/angel/Desktop/paper/PAPERS/LUGEL/research/lula22/publications/LULA-I/editorial/writing-r6/baseline/LULA-I.tex:441). Revisor: claims; registro CLAIM-04a.

**Pasaje exacto**

```latex
The measured maximum of 100,586 calls is simply the largest value in one recorded sample.
```

**Diagnóstico**

Calls sin modificador puede leerse como hash invocations, aunque el manuscrito distingue expresamente invocaciones y compresiones. En el pasaje de costos, conviene conservar la unidad específica.

**Propuesta inglesa, no aplicada**

```latex
The measured maximum of 100,586 instrumented compressions is simply the largest value in one recorded sample.
```

**Lectura legítima alternativa**

La oración previa ya dice instrumented compressions y el lector puede heredar la unidad; no hay evidencia de número incorrecto.

**Conservar al integrar**

- Mismo100586, máximo medido, una sola muestra.
- No convertir máximo observado en garantía.

### R12 — Mantener esa unidad en la diferencia del modelo — MINOR

Fuente: [LULA-I.tex:456](C:/Users/angel/Desktop/paper/PAPERS/LUGEL/research/lula22/publications/LULA-I/editorial/writing-r6/baseline/LULA-I.tex:456). Revisor: claims; registro CLAIM-04b.

**Pasaje exacto**

```latex
The recovered expected-cost model differs by $2^{22}$ calls from this source-exact expression, although its rounded exponent remains close.
```

**Diagnóstico**

El mismo cambio de etiqueta de unidad puede hacer pensar que se comparan funciones hash en lugar de bloques comprimidos. No es un hallazgo por repetir vocabulario, sino por la distinción de unidades ya establecida.

**Propuesta inglesa, no aplicada**

```latex
The recovered expected-cost model differs by $2^{22}$ compressions from this source-exact expression, although its rounded exponent remains close.
```

**Lectura legítima alternativa**

Toda la subsección habla de trabajo de compresión; el contexto permite recuperar la unidad correcta.

**Conservar al integrar**

- Misma diferencia2^22 y mismo estado de modelo esperado.
- Conservar el modelo idealizado ilimitado de la frase anterior.
- No cambiar la fórmula ni prometer expectativa ejecutable sin condición.

### R13 — El mapa de falsificadores omite una parte del lema — MINOR

Fuente: [LULA-I.tex:570](C:/Users/angel/Desktop/paper/PAPERS/LUGEL/research/lula22/publications/LULA-I/editorial/writing-r6/baseline/LULA-I.tex:570). Revisor: claims; registro CLAIM-05.

**Pasaje exacto**

```latex
Any terminating honest-cache case with different bytes
```

**Diagnóstico**

El lema formula dos compromisos: equivalencia de terminación y bytes iguales al retornar. El mapa final muestra solo el segundo como falsificador; puede orientar una comprobación incompleta del mismo claim.

**Propuesta inglesa, no aplicada**

```latex
Different termination behavior, or different signature bytes on a terminating honest-cache request
```

**Lectura legítima alternativa**

La tabla se titula Principal claims y no promete enumerar todos los falsificadores. Por ello no es una contradicción lógica ni una refutación del lema, sino un resumen incompleto de una dimensión central.

**Conservar al integrar**

- Mantener honestidad de caché y clave generada correctamente.
- Retener igualdad de bytes como obligación separada.
- No garantizar terminación de toda búsqueda ni añadir respuesta de error productiva.

### R14 — Jerga de admisión sin el objeto a la vista — MINOR

Fuente: [comparison-results.tex:3](C:/Users/angel/Desktop/paper/PAPERS/LUGEL/research/lula22/publications/LULA-I/editorial/writing-r6/baseline/comparison-results.tex:3). Revisor: patterns; registro PT01.

**Pasaje exacto**

```latex
The tables use raw observations and explicit admission boundaries rather than inherited summary labels.
```

**Diagnóstico**

“Admission boundaries” e “inherited summary labels” comprimen decisiones editoriales cuyo objeto queda implícito. El lector tiene que reconstruir qué criterios incluyen una fila y a qué resumen se alude.

**Propuesta inglesa, no aplicada**

```latex
The tables use raw observations subject to the inclusion criteria stated here, rather than relying on the campaign's summary labels.
```

**Lectura legítima alternativa**

El contraste sí protege una distinción de procedencia. No se propone aceptar las etiquetas como validación ni alterar qué observaciones entran; sólo nombrar criterios y resúmenes con mayor claridad.

**Conservar al integrar**

- Observaciones crudas y criterios de inclusión explícitos.
- Las etiquetas del resumen no controlan por sí solas la admisión.

### R15 — Comparar medianas con medianas y nombrar el límite — MINOR

Fuente: [LULA-I.tex:533](C:/Users/angel/Desktop/paper/PAPERS/LUGEL/research/lula22/publications/LULA-I/editorial/writing-r6/baseline/LULA-I.tex:533). Revisor: patterns; registro PT02.

**Pasaje exacto**

```latex
Observed medians improve on the named OpenSSL SLH-DSA implementations in those cells, but backend, preprocessing and unestablished common-security assumptions prevent a secure-winner claim.
```

**Diagnóstico**

La oración compara medianas con implementaciones, y “secure-winner claim” no define la propiedad que impide ordenar las construcciones. El orden medido y la limitación de seguridad pueden decirse directamente.

**Propuesta inglesa, no aplicada**

```latex
LULA I has lower observed medians than the named OpenSSL SLH-DSA implementations in those cells, but differences in backends and preprocessing, together with the absence of established comparable security bounds, prevent ranking the constructions at a common security level.
```

**Lectura legítima alternativa**

La cautela y el contraste son pertinentes. La propuesta conserva exactamente las celdas observadas y la ausencia de cotas de seguridad comparables; no elimina el but ni propone un ranking.

**Conservar al integrar**

- Las mismas medianas y celdas de Sign/Verify de las implementaciones OpenSSL nombradas.
- Diferencias de backend y preprocesamiento.
- Ausencia de una base común de seguridad establecida.

### R16 — Una frase nominal poco clara sobre interferencia — MINOR

Fuente: [LULA-I.tex:475](C:/Users/angel/Desktop/paper/PAPERS/LUGEL/research/lula22/publications/LULA-I/editorial/writing-r6/baseline/LULA-I.tex:475). Revisor: patterns; registro PT04.

**Pasaje exacto**

```latex
Processor frequency, thermal state, complete foreign concurrency, and per-sample scheduling interruptions were not controlled.
```

**Diagnóstico**

“Complete foreign concurrency” es una combinación nominal poco idiomática: no nombra con claridad las cargas externas concurrentes cuyo conjunto no se controló.

**Propuesta inglesa, no aplicada**

```latex
Processor frequency, thermal state, the full set of concurrent external workloads, and scheduling interruptions affecting individual samples were not controlled.
```

**Lectura legítima alternativa**

El contexto anterior permite entender foreign workloads. La propuesta hace explícito ese referente y conserva separados frecuencia, temperatura, concurrencia e interrupciones de planificación.

**Conservar al integrar**

- Mantener los cuatro factores no controlados.
- Esta oración describe el replay; no negar las muestras de carga que sí existen en la campaña posterior.

### R17 — La misma clasificación de evidencia se anuncia dos veces — MINOR

Fuente: [LULA-I.tex:528](C:/Users/angel/Desktop/paper/PAPERS/LUGEL/research/lula22/publications/LULA-I/editorial/writing-r6/baseline/LULA-I.tex:528). Revisor: patterns; registro PT06.

**Pasaje exacto**

```latex
Historical preparation and cache-loss runs, a fixed-fixture verification replay, and the separately frozen campaign comparison support different observations. The final campaign cut includes new complete-cache preparation and two absent-cache signing calls, with their own fixture and timing boundaries. These evidence classes support different parts of the mechanism analysis and are identified separately.
```

**Diagnóstico**

La primera y última oración vuelven a anunciar la separación de evidencia sin añadir otro resultado. La información concreta sobre preparación y dos llamadas frías queda encerrada entre dos recapitulaciones generales.

**Propuesta inglesa, no aplicada**

```latex
Historical preparation and cache-loss runs, the fixed-fixture verification replay, and the separately frozen campaign comparison support distinct observations of the mechanism and are identified separately. The final campaign includes complete-cache preparation and two absent-cache signing calls, with their own fixture and timing boundaries.
```

**Lectura legítima alternativa**

La repetición busca evitar mezclar ejecuciones como una mejora controlada. La propuesta conserva históricos, replay y campaña, identificación separada, fixture y fronteras temporales; sólo reúne los dos anuncios.

**Conservar al integrar**

- No mezclar históricos y campaña ni sus ámbitos de evidencia.
- Conservar preparación completa y dos llamadas sin caché, con fixture y temporizadores propios.
- No convertir llamadas consecutivas en ensayos independientes.

## Rasgos que deben conservarse

Las negaciones que distinguen restauración honesta de corrupción, validez de una firma de unforgeability, muestra finita de prueba, y máximo observado de WCET cumplen una función. Sus diferencias no son antítesis decorativas. Repetir la premisa del firmante de referencia en abstract, teorema, lectura de resultados y conclusión permite entender cada parte sin promover una reducción condicional a seguridad concreta.

“Exact”, “canonical”, “partial” y “honest” tienen contenido técnico especificado; sustituirlos para variar vocabulario dañaría el texto. FORS, WOTS, child root, reference signer y signature bytes identifican entidades, no sinónimos intercambiables. El presente y los cuantificadores universales de los lemas están delimitados por sus hipótesis. Los participios de reconstrucción describen operaciones reales; no se confirmó una cola participial que añadiera una garantía inexistente.

Un cribado literal de doce familias léxicas frecuentes en listas populares —incluidas delve, groundbreaking, transformative y seamless— dio cero coincidencias en main+comparison+replay. El método y el denominador están en SCREENING.json. Esto sólo describe esas búsquedas: no es un detector, un estudio de autoría ni prueba de ausencia de todos los adornos posibles.

## Tres maneras de abordar la revisión posterior

**A. Reparaciones locales — opción preferida.** Precisar actores/unidades, aclarar títulos y etiquetas, dividir el párrafo del modelo finito y fusionar las dos recapitulaciones inmediatas. El resto del argumento queda próximo a su forma actual.

**B. Reorganización moderada.** Introducir explícitamente las clases de evidencia y las preguntas de la campaña antes de los detalles de trazabilidad. Conservar cifras, controles, condicionantes y fuentes en sus ámbitos. Es una elección editorial, no una necesidad de reescribir todo el paper ni autorización para eliminar resultados históricos.

**C. Conservar formulaciones deliberadas.** Algunas abreviaturas son recuperables para criptógrafos. Si se conserva “CacheRestore” como nombre público, aclarar su leyenda antes de renombrarlo. Si “Parameter selection” debe mantenerse, el apartado necesitaría una explicación real de la selección; esta revisión no puede inventarla. No hay una pregunta que bloquee la entrega del análisis.

## Comprobaciones para una futura integración

El mapa AUDIT_MODEL.md registra las obligaciones protegidas. Cada propuesta debe comprobarse desde el original hacia la revisión y en sentido inverso: actor, negación, modalidad, unidad, ámbito, orden temporal y cita. Se preservan especialmente equivalencia de terminación y de bytes; referencia criptográfica no establecida; estados honestos e interfaz atómica; distinción entre independencia y comprobación nativa; firma fría primera/segunda; mediana de sumas emparejadas; ausencia de ranking común y de WCET.

La propuesta de leyenda de CacheRestore conserva su nombre; el cambio de actor en la figura conserva la independencia individual de las shares, sin inventar independencia conjunta. Los dos “calls” se precisan porque el contexto identifica compresiones: no se recalculan números ni se comparan invocaciones con bloques. El mapa de falsificadores sólo incorpora una dimensión ya presente en el lema y no declara que todas las búsquedas terminen.

No se realizaron pruebas nuevas, comparación estilométrica con un corpus de papers criptográficos, análisis sintáctico automático, revisión visual nueva del PDF, evaluación de todos los artículos criptográficos citados o certificación de pruebas. La lectura de bibliografía y adjunción de citas no equivale a revalidar todas sus fuentes externas. Estas son limitaciones del encargo editorial, no hallazgos científicos adversos nuevos.

## Evidencia y trazabilidad

- [Literatura y acceso](C:/Users/angel/Desktop/paper/PAPERS/LUGEL/research/lula22/publications/LULA-I/editorial/writing-r6/LITERATURE.md).
- [Mapa de obligaciones y preguntas del lector](C:/Users/angel/Desktop/paper/PAPERS/LUGEL/research/lula22/publications/LULA-I/editorial/writing-r6/AUDIT_MODEL.md).
- [Cobertura de los 97 nodos, con hashes y aplicación](C:/Users/angel/Desktop/paper/PAPERS/LUGEL/research/lula22/publications/LULA-I/editorial/writing-r6/NODE_COVERAGE.csv).
- [Registros consolidados y originales](C:/Users/angel/Desktop/paper/PAPERS/LUGEL/research/lula22/publications/LULA-I/editorial/writing-r6/FINDINGS_CONSOLIDATED.json).
- [Revisión de estructura](C:/Users/angel/Desktop/paper/PAPERS/LUGEL/research/lula22/publications/LULA-I/editorial/writing-r6/structure/REPORT.md), [patrones locales](C:/Users/angel/Desktop/paper/PAPERS/LUGEL/research/lula22/publications/LULA-I/editorial/writing-r6/patterns/REPORT.md), [afirmaciones](C:/Users/angel/Desktop/paper/PAPERS/LUGEL/research/lula22/publications/LULA-I/editorial/writing-r6/claims/REPORT.md).
- [Validación del alcance y archivos sin cambios](C:/Users/angel/Desktop/paper/PAPERS/LUGEL/research/lula22/publications/LULA-I/editorial/writing-r6/VALIDATION.json).

**Estado: COMPLETE_WITHIN_SCOPE — análisis completo del texto y lectura colectiva de todos los nodos, con propuestas puntuales.** No se entrega un manuscrito reescrito porque el encargo fue analizar. No se afirma una probabilidad de autoría IA, aceptación editorial, equivalencia semántica global de una revisión no aplicada ni seguridad de la construcción.
