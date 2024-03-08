#pip install spacy
#python -m spacy download es_core_news_sm
#pip install nltk

import spacy
from spacy.matcher import Matcher
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import pyttsx3
import speech_recognition as sr

# Inicializar Spacy
nlp = spacy.load("es_core_news_sm")

# Inicializar NLTK
stop_words = set(stopwords.words("spanish"))
matcher = Matcher(nlp.vocab)

# Inicializar TTS (Text-to-Speech) con pyttsx3
engine = pyttsx3.init()

# Inicializar ASR (Automatic Speech Recognition) con SpeechRecognition
recognizer = sr.Recognizer()

def text_to_speech(text):
    engine.say(text)
    engine.runAndWait()

def speech_to_text():
    with sr.Microphone() as source:
        print("Hable ahora...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source, timeout=5)
        print("¡Listo!")
        
    try:
        user_input = recognizer.recognize_google(audio, language="es")
        return user_input.lower()
    except sr.UnknownValueError:
        return None

def process_text(text):
    # a) Eliminar stop words
    words = [word for word in word_tokenize(text) if word.lower() not in stop_words]
    
    # b) Unificar mayúsculas, minúsculas y signos
    cleaned_text = " ".join(words)
    
    # c) Tokenizar y etiquetar con Spacy
    doc = nlp(cleaned_text)
    
    # d) Encontrar tokens correspondientes a verbos de acción
    action_verbs = [token.text for token in doc if token.pos_ == "VERB"]
    
    # e) Encontrar tokens correspondientes a valores numéricos
    numeric_values = [token.text for token in doc if token.like_num]
    
    # f) Agregación sintagmática
    noun_phrases = [chunk.text for chunk in doc.noun_chunks]

    return {
        "cleaned_text": cleaned_text,
        "action_verbs": action_verbs,
        "numeric_values": numeric_values,
        "noun_phrases": noun_phrases
    }

# Iniciar el diálogo
text_to_speech("Por favor, indique el nombre del medicamento del cual desea obtener información.")
user_input = speech_to_text()

if user_input:
    processed_data = process_text(user_input)
    print("Texto limpio:", processed_data["cleaned_text"])
    print("Verbos de acción:", processed_data["action_verbs"])
    print("Valores numéricos:", processed_data["numeric_values"])
    print("Agregación sintagmática:", processed_data["noun_phrases"])
else:
    print("No se ha detectado ninguna entrada de voz.")

