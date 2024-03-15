# Proyecto PLN para una aplicación de Gestión de Información sobre Medicamentos

## Contenido

- **[1. Descripcion](#1-descripción)**
- **[2. Objetivo](#2-objetivo)**
- **[3. Tecnologías utilizadas](#3-tecnologías-utilizadas)**
- **[4. Fuentes](#4-fuentes)**
- **[5. Estructura del proyecto](#5-estructura-del-proyecto)**
- **[6. Llamada a la API](#6-llamada-a-la-api)**
- **[7. Uso de la aplicación](#7-uso-de-la-aplicación)**
- **[8. Licencia](#8-licencia)**
- **[9. Autores](#9-autores)**

### 1. Descripción
Esta aplicación en Flask permite a los usuarios obtener información sobre medicamentos, a través de una llamada realizada a una API. 

[subir](#contenido)

### 2. Objetivo
El propósito principal es proporcionar a los usuarios información variada sobre medicamentos, basándose únicamente en su nombre. Además, la aplicación utiliza técnicas de Procesamiento del Lenguaje Natural (PLN) para mejorar la accesibilidad, permitiendo tanto la interacción verbal como escritaa.

[subir](#contenido)

### 3. Tecnologías utilizadas
- [Flask](https://flask.palletsprojects.com/en/3.0.x/)
Framework para Python. Se utiliza en este proyecto para crear la aplicación web y manejar las rutas y las solicitudes HTTP.

- [SpaCy](https://spacy.io)
Biblioteca de procesamiento de lenguaje natural (NLP) de código abierto. Se utiliza para el procesamiento de texto, incluyendo tokenización, análisis gramatical y extracción de información. La clase _Matcher_ es una clase de SpaCy que permite realizar coincidencias de patrones en texto utilizando reglas definidas. Se utiliza para encontrar patrones específicos en el texto, como verbos de acción o frases nominales.

- [NLTK](https://www.nltk.org/install.html)
_wordtokenize_ es una función de NLTK que divide el texto en palabras o tokens. Se utiliza para tokenizar el texto en palabras individuales.

- **Corpus.stopwords_** es una lista de palabras comunes que se pueden filtrar del texto durante el procesamiento de lenguaje natural.
Se utiliza para eliminar palabras irrelevantes del texto, como por ejemplo artículos.

- [pyttsx3](https://pypi.org/project/pyttsx3/)
Biblioteca para texto a voz (TTS) en Python. Se utiliza para convertir texto en voz para la interacción con el usuario.

- [Speech Recognition](https://pypi.org/project/SpeechRecognition/)
Biblioteca para reconocimiento de voz en Python. Se utiliza para convertir la entrada de voz del usuario en texto utilizable por la aplicación.

- [Pyaudio](https://pypi.org/project/PyAudio/)
Módulo de Python para acceder a los dispositivos de audio. Se utiliza para la captura y reproducción de audio, especialmente en el contexto de reconocimiento de voz.

- [Textdistance](https://pypi.org/project/textdistance/)
Biblioteca de Python que proporciona funciones para calcular la distancia entre cadenas de texto. Se puede utilizar para comparar y encontrar similitudes entre cadenas de texto.

[subir](#contenido)

### 4. Fuentes
- [Agencia Española de Medicamentos y Productos Sanitarios](https://www.aemps.gob.es)
- [Documentación CIMA REST API](https://sede.aemps.gob.es/docs/CIMA-REST-API_1_19.pdf)
- [Base de Datos: Nomenclator](https://cima.aemps.es/cima/publico/nomenclator.html)

[subir](#contenido)

### 5. Estructura del Proyecto
- main.py. Contiene el código principal de la aplicación Flask.
- functions.py. Contiene las funciones relacionadas con el procesamiento de voz, texto y búsqueda de información en el archivo de Excel.
- data: Aquí es donde se alojará Medicamentos.xlsx, bases de datos etc.
- templates: contiene la parte gráfica del proyecto, los .html de los archivos.
- static: se alojarán el css de la web y las imágenes.

[subir](#contenido)

### 6. LLamada a la API
Para realizar una llamada a la API y obtener información sobre un medicamento específico, sigue estos pasos:

1. Busca el número de registro correspondiente con el medicamento que desees. Ese número se encuentra en el excel adjunto. 

2. Utiliza la URL base de la API y agrega el parámetro _nregistro_ con el número de registro del medicamento que deseas consultar. 

Ejemplo:
```python
n_registro = 1181322002IP
request => https://cima.aemps.es/cima/rest/medicamento?nregistro={n_registro}
```
[subir](#contenido)

### 7. Uso de la aplicación
1. Inicio
El usuario accede a la página de inicio donde se le muestra un botón.

Accederá con la url: ``` 127.0.0.1:5000```

1. Interacción de Voz
Cuando el usuario hace clic en el botón, se solicita al usuario que pronuncie el nombre del medicamento del que desea obtener información.

1. Procesamiento de texto
La entrada de voz del usuario se convierte en texto y se procesa para extraer el nombre del medicamento.

1. Llamada a API
Una vez detectado el nombre del medicamento busca en el excel adjunto su numero de referencia el cual, usa para hacer un llamamiento a la API de CIMA (Centro de información de medicamentos). Esa llamada devuelve un json con información  del medicamento.

1. Obtención y visualización de información
La información extraida de la json se muestra al usuario por pantalla. Esa misma página permite acceder de nuevo a la página de inicio.

1. Manejo de Errores
Si no se encuentra información sobre el medicamento, se mostrará un mensaje de error.

[subir](#contenido)

### 8. Licencia
Este proyecto está licenciado bajo la licencia MIT.

[subir](#contenido)

### 9. Autores
- [Álvaro Cañas González](https://github.com/MameHub)
- [José Miguel Escribano Ruiz](https://github.com/JMER15)
- [Rosa Moreno López](https://github.com/rosaml96)
- [Virginia Ordoño Bernier](https://github.com/viorbe20)
- [Jose Luis Pérez Lara](https://github.com/JoseLuixrax)
