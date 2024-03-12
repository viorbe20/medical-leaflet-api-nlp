# Proyecto PLN para una aplicación de Gestión de Información sobre Medicamentos

Esta aplicación en Flask permite a los usuarios obtener información sobre medicamentos a través de una llamada a API. 

## Contenidos

### 1. Funcionalidad del Proyecto
1. Inicio
El usuario accede a la página de inicio donde se le muestra un botón.

2. Interacción de Voz
Cuando el usuario hace clic en el botón, se solicita al usuario que pronuncie el nombre del medicamento del que desea obtener información.

3. Procesamiento de texto
La entrada de voz del usuario se convierte en texto y se procesa para extraer el nombre del medicamento.

4. Llamada a API
Una vez detectado el nombre del medicamento busca en el excel adjunto su numero de referencia el cual, usa para hacer un llamamiento a la API de CIMA (Centro de información de medicamentos). Esa llamdaa devuelve un json con información  del medicamento.

4. Obtención y visualización de información
La información extraida de la json se muestra al usuario por pantalla. Esa misma página permite acceder de nuevo a la página de inicio.

5. Manejo de Errores:
Si no se encuentra información sobre el medicamento, se mostrará un mensaje de error.

### 2. Archivos del Proyecto
- main.py. Contiene el código principal de la aplicación Flask.
- functions.py. Contiene las funciones relacionadas con el procesamiento de voz, texto y búsqueda de información en el archivo de Excel.
- Medicamentos.xlsx. Un archivo Excel que almacena la información sobre los medicamentos.
- templates: contiene la parte gráfica del proyecto.

### 3. Tecnologías utilizadas
**Flask**
Framework para Python. Se utiliza en este proyecto para crear la aplicación web y manejar las rutas y las solicitudes HTTP.

**SpaCy** 
Biblioteca de procesamiento de lenguaje natural (NLP) de código abierto. Se utiliza para el procesamiento de texto, incluyendo tokenización, análisis gramatical y extracción de información. La clase _Matcher_ es una clase de SpaCy que permite realizar coincidencias de patrones en texto utilizando reglas definidas. Se utiliza para encontrar patrones específicos en el texto, como verbos de acción o frases nominales.

**NLTK**
_wordtokenize_ es una función de NLTK que divide el texto en palabras o tokens. Se utiliza para tokenizar el texto en palabras individuales.

_corpus.stopwords_ es una lista de palabras comunes que se pueden filtrar del texto durante el procesamiento de lenguaje natural.
Se utiliza para eliminar palabras irrelevantes del texto, como por ejemplo artículos.

**pyttsx3**
Biblioteca para texto a voz (TTS) en Python. Se utiliza para convertir texto en voz para la interacción con el usuario.

**Speech Recognition**
Biblioteca para reconocimiento de voz en Python. Se utiliza para convertir la entrada de voz del usuario en texto utilizable por la aplicación.

**Pyaudio**
Módulo de Python para acceder a los dispositivos de audio. Se utiliza para la captura y reproducción de audio, especialmente en el contexto de reconocimiento de voz.

**Textdistance**
Biblioteca de Python que proporciona funciones para calcular la distancia entre cadenas de texto. Se puede utilizar para comparar y encontrar similitudes entre cadenas de texto.

### 4. LLamada a la API

Para realizar una llamada a la API y obtener información sobre un medicamento específico, sigue estos pasos:

1. Definir el Número de Registro:
Busca el número de registro correspondiente con el medicamento que desees. Ese número se encuentra en el excel adjunto. 

Utiliza la URL base de la API y agrega el parámetro nregistro con el número de registro del medicamento que deseas consultar. 

Ejemplo:
```python
n_registro = 1181322002IP
request => https://cima.aemps.es/cima/rest/medicamento?nregistro={n_registro}
```

### 5. Autores
[Álvaro Cañas González](https://github.com/MameHub)
[José Miguel Escribano Ruiz](https://github.com/JMER15)
[Rosa Moreno López](https://github.com/rosaml96)
[Jose Luis Pérez Lara](https://github.com/JoseLuixrax)
[Virginia Ordoño Bernier](https://github.com/viorbe20)