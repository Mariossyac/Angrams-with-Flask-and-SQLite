from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from collections import defaultdict
import json
import os


app = Flask(__name__)

# 1. Spunem Flask unde să găsească fișierul bazei de date (pe hard disk-ul tău)
base_dir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///D:/proiect_anagrame/anagrams.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# 2. DEFINIM OBIECTUL db (Aici era problema ta!)
db = SQLAlchemy(app)


# Tabelul din BD
class AnagramCache(db.Model):
    id = db.Column(db.Integer, primary_key=True) # id - primary_key
    input_key = db.Column(db.String(500), unique=True) # lista de intrare - unica
    result_data = db.Column(db.Text) # rezultat - text



def validAnagrams(strs):
    d = defaultdict(list)
    for i in strs:
        vec = [0 for x in range(27)]
        for litera in i:
            vec[ord(litera) - 97] += 1 
        vec_t = tuple(vec)
        d[vec_t].append(i)
    return list(d.values())


@app.route('/anagrams', methods = ['POST'])
def get_anagrams():
    data = request.get_json()
    print(f"DEBUG: Datele primite sunt: {data}")
    if not data or 'strings' not in data:
        return jsonify({"error" : "Lipsesc datele!"}), 400
    
    input_list = data['strings']
    search_key = ",".join(sorted(input_list))

    cached = AnagramCache.query.filter_by(input_key = search_key).first()
    if cached:
        print("Returnat din baza de date!")
        return jsonify(json.loads(cached.result_data))
    
    print("Calcuated from scratch")
    result = validAnagrams(input_list)
    new_entry = AnagramCache(input_key = search_key, result_data = json.dumps(result))

    db.session.add(new_entry)
    db.session.commit()

    return jsonify(result)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        print("Baza de date creata!")
    app.run(debug = True)
