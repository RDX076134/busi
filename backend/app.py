from flask import Flask, request, jsonify
import pytesseract
from PIL import Image
import spacy
import re

app = Flask(__name__)

nlp = spacy.load("en_core_web_sm")

def extract_entities(text):
    doc = nlp(text)
    result = {
        "business_name": "",
        "person_name": "",
        "position": "",
        "phone": "",
        "email": "",
        "address": ""
    }

    emails = re.findall(r'\S+@\S+', text)
    result['email'] = emails[0] if emails else ""

    phones = re.findall(r'\+?\d[\d\s\-]{7,}\d', text)
    result['phone'] = phones[0] if phones else ""

    for ent in doc.ents:
        if ent.label_ == "PERSON" and not result['person_name']:
            result['person_name'] = ent.text
        elif ent.label_ == "ORG" and not result['business_name']:
            result['business_name'] = ent.text
        elif ent.label_ in ["GPE", "LOC"] and not result['address']:
            result['address'] = ent.text

    position_keywords = ['Manager', 'Director', 'CEO', 'Founder', 'Officer', 'Developer', 'Engineer']
    for line in text.split('\n'):
        for word in position_keywords:
            if word.lower() in line.lower():
                result['position'] = line.strip()
                break

    return result

@app.route('/extract', methods=['POST'])
def extract():
    image_file = request.files['image']
    image = Image.open(image_file.stream)
    text = pytesseract.image_to_string(image)
    entities = extract_entities(text)
    return jsonify(entities)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
