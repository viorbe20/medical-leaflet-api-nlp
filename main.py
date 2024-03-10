from flask import Flask, render_template
import os

from functions import speech_to_text, text_to_speech, process_text, get_medicine_info

API_URL = "https://cima.aemps.es/cima/rest/medicamento"
# https://cima.aemps.es/cima/rest/medicamento?nregistro=1181322002IP

app = Flask(__name__)

# Obtiene el path del directorio actual
script_dir = os.path.dirname(__file__)
model_path = os.path.join(script_dir, 'data', 'Medicamentos.xlsx')

    
@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('home.html')


@app.route('/information', methods=['GET'])
def information():
    # Iniciar el diálogo. sin no habla da errro. controlar eso
    text_to_speech("Por favor, indique el nombre del medicamento del cual desea obtener información.")
    try:
        user_input = speech_to_text()
    except Exception as e:
        return render_template('notFound.html', data={"msg": "No se ha detectado ninguna entrada de voz, recarga la página y vuelve a intentarlo."})
    
    if user_input:
        processed_data = process_text(user_input)
        print("Texto limpio:", processed_data["cleaned_text"])
        print("Verbos de acción:", processed_data["action_verbs"])
        print("Valores numéricos:", processed_data["numeric_values"])
        print("Agregación sintagmática:", processed_data["noun_phrases"])
    else:
        print("No se ha detectado ninguna entrada de voz.")

    data = get_medicine_info(processed_data["noun_phrases"][0])
    # print(data["fotos"][0]["url"])

    if data is None:
        return render_template('notFound.html', data={"msg": "No se ha encontrado información sobre el medicamento solicitado."})

    if "fotos" not in data:
        data["fotos"] = [{"url": "static/img/medicamento.jpg"}]

    if "docs" not in data or len(data["docs"]) < 2:
        data["docs"] = [{"url": "notFound"}, {"url": "notFound"}]
        
    showable_data = {
        "nombre": data["nombre"],
        "receta": data["receta"],
        "generico": data["generico"],
        "conduc": data["conduc"],
        "dosis": data["dosis"],
        "fichaTec": data["docs"][0]["url"],
        "prospecto": data["docs"][1]["url"],
        "imgCaja": data["fotos"][0]["url"],
    }
    return render_template('information.html', data=showable_data)
    
@app.route('/notFound', methods=['GET'])
def notFound():
    data = {"msg" : "No se ha encontrado información sobre el medicamento solicitado."}
    return render_template('notFound.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)
