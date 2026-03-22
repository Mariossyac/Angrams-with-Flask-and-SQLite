import json
from app import validAnagrams  # Importăm funcția ta de calcul

def process_json_file(input_filename, output_filename):
    try:
        # 1. Citim datele din fișierul de intrare
        with open(input_filename, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        # Presupunem că JSON-ul are structura {"strings": [...]}
        input_list = data.get('strings', [])
        
        if not input_list:
            print("Eroare: Lista de cuvinte este goală sau lipsește cheia 'strings'.")
            return

        # 2. Calculăm anagramele folosind funcția ta existentă
        result = validAnagrams(input_list)

        # 3. Salvăm rezultatul într-un fișier nou
        with open(output_filename, 'w', encoding='utf-8') as f:
            json.dump(result, f, indent=4) # indent=4 îl face ușor de citit (pretty print)
            
        print(f"Succes! Rezultatele au fost salvate în {output_filename}")

    except FileNotFoundError:
        print(f"Eroare: Fișierul {input_filename} nu a fost găsit.")
    except Exception as e:
        print(f"A apărut o eroare neașteptată: {e}")

if __name__ == "__main__":
    # Exemplu de utilizare
    process_json_file('input.json', 'output.json')