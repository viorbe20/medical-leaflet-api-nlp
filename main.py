from flask import Flask, render_template, request, jsonify, make_response
import os
import pandas as pd
import spacy
from spacy.matcher import Matcher
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import pyttsx3
import speech_recognition as sr
import pyaudio
import requests

API_URL = "https://cima.aemps.es/cima/rest/medicamento"

app = Flask(__name__)

# Obtiene el path del directorio actual
script_dir = os.path.dirname(__file__)
model_path = os.path.join(script_dir, 'data', 'Medicamentos.xlsx')
df = None

def read_excel():
    """Lee el archivo Excel y lo almacena en un DataFrame de Pandas, actualiza la variable global df."""
    global df
    df = pd.read_excel(model_path)

def search_number_medicine(medicine_name):
    """Busca un medicamento en el archivo Excel y devuelve el número de registro asociado."""
    if df is None:
        read_excel()
    
    medicine_name = medicine_name.upper()
    medicine_data = df[df['medicamento'].str.contains(medicine_name)]
    if len(medicine_data) > 0:
        return medicine_data['nregistro'].values[0]
    else:
        return None


def text_to_speech(text):
    """Convierte texto a voz."""
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def make_request(number):
    """Realiza una petición a la API de la AEMPS para obtener información sobre un medicamento."""
    response = requests.get(f"{API_URL}?nregistro={number}")
    if response.status_code == 200:
        return response.json()
    else:
        return None
    
def get_medicine_info(medicine_name):
    """Obtiene información sobre un medicamento."""
    number = search_number_medicine(medicine_name)
    if number:
        return make_request(number)
    else:
        return None

@app.route('/', methods=['GET'])
def home():

    # # Inicializar Spacy
    # nlp = spacy.load("es_core_news_sm")

    # # Inicializar NLTK
    # stop_words = set(stopwords.words("spanish"))
    # matcher = Matcher(nlp.vocab)

    # # Inicializar TTS (Text-to-Speech) con pyttsx3
    # engine = pyttsx3.init()

    # # Inicializar ASR (Automatic Speech Recognition) con SpeechRecognition
    # recognizer = sr.Recognizer()

    # def text_to_speech(text):
    #     engine.say(text)
    #     engine.runAndWait()

    # def speech_to_text():
    #     with sr.Microphone() as source:
    #         print("Hable ahora...")
    #         recognizer.adjust_for_ambient_noise(source)
    #         audio = recognizer.listen(source, timeout=5)
    #         print("¡Listo!")

    #     try:
    #         user_input = recognizer.recognize_google(audio, language="es")
    #         return user_input.lower()
    #     except sr.UnknownValueError:
    #         return None

    # def process_text(text):
    #     # a) Eliminar stop words
    #     words = [word for word in word_tokenize(text) if word.lower() not in stop_words]
        
    #     # b) Unificar mayúsculas, minúsculas y signos
    #     cleaned_text = " ".join(words)
        
    #     # c) Tokenizar y etiquetar con Spacy
    #     doc = nlp(cleaned_text)
        
    #     # d) Encontrar tokens correspondientes a verbos de acción
    #     action_verbs = [token.text for token in doc if token.pos_ == "VERB"]
        
    #     # e) Encontrar tokens correspondientes a valores numéricos
    #     numeric_values = [token.text for token in doc if token.like_num]
        
    #     # f) Agregación sintagmática
    #     noun_phrases = [chunk.text for chunk in doc.noun_chunks]
    
    #     return {
    #         "cleaned_text": cleaned_text,
    #         "action_verbs": action_verbs,
    #         "numeric_values": numeric_values,
    #         "noun_phrases": noun_phrases
    #     }
    
    # # Iniciar el diálogo. sin no habla da errro. controlar eso
    # text_to_speech("Por favor, indique el nombre del medicamento del cual desea obtener información.")
    # user_input = speech_to_text()
    
    # if user_input:
    #     processed_data = process_text(user_input)
    #     print("Texto limpio:", processed_data["cleaned_text"])
    #     print("Verbos de acción:", processed_data["action_verbs"])
    #     print("Valores numéricos:", processed_data["numeric_values"])
    #     print("Agregación sintagmática:", processed_data["noun_phrases"])
    # else:
    #     print("No se ha detectado ninguna entrada de voz.")
    
    # Renderiza la página
    return render_template('home.html')

@app.route('/test', methods=['GET'])
def test():
    data = get_medicine_info("ibuprofeno")
    showable_data = {
        "nombre": data["nombre"],
        "receta": data["receta"],
        "generico": data["generico"],
        "conduc": data["conduc"],
        "dosis": data["dosis"],
        "img": "???"
    }
    return render_template('test.html', data=showable_data)
    

if __name__ == '__main__':
    app.run(debug=True)



