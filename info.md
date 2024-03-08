1. TTS: La máquina lee un texto preguntando el medicamento 
2. ASR: usuario responde.

Se inicia el diálogo.

2. El texto es procesado:

    a) Se quitan las palabras inútiles (stop words)

    b) Se unifican mayúsculas, minúsculas y signos

    c) Se tokeniza y se etiqueta

    d) Se localizan los tokens correspondientes a verbos de acción

    e) Se localizan los tokens correspondientes a valores numéricos

    f) Se va haciendo agregación sintagmática


## Leer
    "nombre": "MIRCERA 250 microgramos/0,3 ml SOLUCION INYECTABLE EN JERINGA PRECARGADA",
    "receta": true,
    "generico": false,
    "conduc": false,
     "dosis": "250 µg"
     img (defecto)
## Ejemplo de 

{
    "nregistro": "07400013",
    "nombre": "MIRCERA 250 microgramos/0,3 ml SOLUCION INYECTABLE EN JERINGA PRECARGADA",
    "pactivos": "METOXI-POLIETILENGLICOL-EPOETINA BETA",
    "labtitular": "Roche Registration Gmbh",
    "cpresc": "Uso Hospitalario",
    "estado": {
        "aut": 1185832800000
    },
    "comerc": true,
    "receta": true,
    "generico": false,
    "conduc": false,
    "triangulo": false,
    "huerfano": false,
    "biosimilar": false,
    "nosustituible": {
        "id": 1,
        "nombre": "Biológicos"
    },
    "psum": false,
    "notas": false,
    "materialesInf": false,
    "ema": true,
    "docs": [
        {
            "tipo": 1,
            "url": "https://cima.aemps.es/cima/pdfs/ft/07400013/FT_07400013.pdf",
            "urlHtml": "https://cima.aemps.es/cima/dochtml/ft/07400013/FT_07400013.html",
            "secc": true
        },
        {
            "tipo": 2,
            "url": "https://cima.aemps.es/cima/pdfs/p/07400013/P_07400013.pdf",
            "urlHtml": "https://cima.aemps.es/cima/dochtml/p/07400013/P_07400013.html",
            "secc": true
        },
        {
            "tipo": 3,
            "url": "https://cima.aemps.es/cima/pdfs/ipe/07400013/IPE_07400013.pdf",
            "secc": false
        }
    ],
    "atcs": [
        {
            "codigo": "B03X",
            "nombre": "OTROS PREPARADOS ANTIANÉMICOS",
            "nivel": 3
        },
        {
            "codigo": "B03XA",
            "nombre": "Otros preparados antianémicos",
            "nivel": 4
        },
        {
            "codigo": "B03XA03",
            "nombre": "Metoxi propilenglicol epoetina beta",
            "nivel": 5
        }
    ],
    "principiosActivos": [
        {
            "id": 8576,
            "codigo": "8576OV",
            "nombre": "METOXI-POLIETILENGLICOL-EPOETINA BETA",
            "cantidad": "250",
            "unidad": "µg",
            "orden": 1
        }
    ],
    "excipientes": [
        {
            "id": 549,
            "nombre": "FOSFATO MONOSODICO MONOHIDRATO",
            "cantidad": "0",
            "unidad": "-",
            "orden": 1
        },
        {
            "id": 5568,
            "nombre": "MANITOL (E-421)",
            "cantidad": "0",
            "unidad": "-",
            "orden": 3
        },
        {
            "id": 7760,
            "nombre": "SULFATO SODICO",
            "cantidad": "0",
            "unidad": "-",
            "orden": 4
        }
    ],
    "viasAdministracion": [
        {
            "id": 42,
            "nombre": "VÍA INTRAVENOSA"
        },
        {
            "id": 58,
            "nombre": "VÍA SUBCUTÁNEA"
        }
    ],
    "presentaciones": [
        {
            "cn": "659525",
            "nombre": "MIRCERA 250 microgramos/0,3 ml SOLUCION INYECTABLE EN JERINGA PRECARGADA, 1 jeringa precargada 0,3 ml",
            "estado": {
                "aut": 1185832800000
            },
            "comerc": true,
            "psum": false
        }
    ],
    "formaFarmaceutica": {
        "id": 1286,
        "nombre": "SOLUCIÓN INYECTABLE EN JERINGA PRECARGADA"
    },
    "formaFarmaceuticaSimplificada": {
        "id": 34,
        "nombre": "INYECTABLE"
    },
    "vtm": {
        "id": 426360006,
        "nombre": "epoetina beta metoxipolietilenglicol"
    },
    "dosis": "250 µg"
}