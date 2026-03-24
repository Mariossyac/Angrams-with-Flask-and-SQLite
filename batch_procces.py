import json
from app import validAnagrams 

def process_json_file(input_filename, output_filename):
    try:
        with open(input_filename, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        input_list = data.get('strings', [])
        
        if not input_list:
            print("Eroare: Lista de cuvinte este goală sau lipsește cheia 'strings'.")
            return

        result = validAnagrams(input_list)

        with open(output_filename, 'w', encoding='utf-8') as f:
            json.dump(result, f, indent=4) 
            
        print(f"Succes! Rezultatele au fost salvate în {output_filename}")

    except FileNotFoundError:
        print(f"Eroare: Fișierul {input_filename} nu a fost găsit.")
    except Exception as e:
        print(f"A apărut o eroare neașteptată: {e}")

if __name__ == "__main__":
    process_json_file('input.json', 'output.json')
