# lab2

# Integrantes:

Brayan Audiel Chavarría Romero SMSS020924          
Esmeralda Isabel Cruz Roldán   SMSS011124     


# Interpretación de resultados

a. Describe brevemente de qué trata el dataset utilizado
Es un inventario digital de un zoológico. La lista incluye 101 animales y detalla sus características esenciales: si tienen pelo, plumas, si ponen huevos, o cuántas patas usan para moverse. Básicamente, es una base de datos que usa números (principalmente 0 y 1) para describir la biología de cada animal.
   
b. ¿Qué información permite ver el resumen estadístico?
En este caso el resumen estadístico (el describe()) nos da dos ideas principales al instante:
   ¿Qué tan común es un rasgo? Para cosas como tener pelo o leche, el Promedio nos dice el porcentaje exacto de animales que cumplen con ese rasgo. Si el promedio de "pelo" es 0.40, sabes que cuatro de cada diez animales tienen pelo.
   ¿Qué tanta variedad hay en un número? En la columna de patas, la Desviación Estándar nos confirma que hay mucha locura en los datos; los animales no solo tienen 2 o 4 patas, sino que el número va desde 0 (peces, serpientes) hasta 8 (escorpiones).

c. ¿Qué cambios o tendencias se detectan en la información del dataset?
La principal tendencia es que la lista de animales estaba algo ordenada de antemano. Vemos que todos los mamíferos (Clase 1) están juntos al principio del archivo, y el resto de grupos (invertebrados, bichos, etc.) aparecen revueltos al final. No es una tendencia de los datos en sí, sino de cómo se escribió el archivo original. También notamos que los animales con menos patas (el 0 y el 2) están "jalando" el promedio de patas hacia abajo.

d. ¿Qué categorías sobresalen en la comparación y por qué crees que será?
Cuando organizamos a los animales por el número de patas, vemos claramente quiénes dominan en los extremos:
Los "pata-largas" (6 u 8 patas): Son los Invertebrados y Bichos (como el pulpo o las arañas). Esto tiene sentido porque su biología es totalmente diferente a la nuestra.
Los "sin-patas" (0 patas): Son los Peces y los Reptiles sin patas (serpientes). Simplemente no las necesitan para nadar o arrastrarse.

e. ¿Qué diferencias se observan entre los primeros y últimos registros?
Es como si el dataset comenzara con un enfoque y terminara con otro:
Al principio: Ves a los animales más "familiares" o "grandes", casi todos son Mamíferos (4 patas, pelo).
Al final: Muestra a una mezcla más caótica y diversa de aves, insectos y gusanos (patas, 2,6 o 0).
En resumen, los primeros son muy parecidos entre sí, y los últimos son muy variados.

f. ¿Qué aportan las medidas estadísticas al análisis del dataset?
Estas medidas son el corazón del análisis, nos dan el contexto real de los números:
Promedio de Patas (3.41): El animal promedio tiene menos de 4 patas. Esto nos dice que hay muchísimos animales con 0 o 2 patas en el zoo.
Mediana de Patas (4.00): Nos confirma que el número más común o central de patas es cuatro.
Desviación Estándar de Patas (2.44): Como este número es grande, confirma que el número de patas es muy inestable. Si fuera bajo, significaría que casi todos los animales tendrían el mismo número de patas.
