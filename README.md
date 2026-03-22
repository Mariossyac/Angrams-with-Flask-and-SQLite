# Anagram Solver System (API & Batch Processing)

This project is a comprehensive solution for identifying and grouping anagrams from a list of words. It features a **REST API** for real-time processing and a **Batch Utility Script** for handling local JSON files.

## Key Features
* **Optimized Algorithm:** Uses character frequency mapping via ASCII codes ($O(N \cdot K)$), which is significantly more efficient than sorting each individual word.
* **Caching System (SQLite):** API results are persisted in a database. If the same list is submitted again, the response is served instantly from the cache.
* **File I/O Processing:** Supports reading input data from `input.json` and automatically generating an `output.json` file.
* **Robustness:** Automatically handles mixed casing, ignores spaces, and filters out punctuation marks.

## Project Structure
* `app.py` – The Flask server and database integration logic.
* `batch_process.py` – Script for local file processing (JSON in -> JSON out).
* `test_api.py` – A testing utility to send HTTP POST requests.
* `requirements.txt` – List of project dependencies.
* `anagrams.db` – SQLite database (automatically generated on the first run).

## Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone <repo-link>
   cd project-name

2. **Create and activate a virtual environment**
    python -m venv venv
    # On Windows:
    venv\Scripts\activate
    # On macOS/Linux:
    source venv/bin/activate

3. **Install dependencies**
    pip install -r requirements.txt

## Usage Guide

1. **Running the API (Real-time)**
    python app.py

    The API listens for POST requests at http://127.0.0.1:5000/anagrams

2. **Input JSON Format**
    {
    "strings": ["eat", "tea", "tan", "ate", "nat", "bat"]
    }  

    You have to create that before next step

3. **Batch Processing (Local Files)**
    Ensure you have an input.json file in the root directory. Then run:
    python batch_process.py
