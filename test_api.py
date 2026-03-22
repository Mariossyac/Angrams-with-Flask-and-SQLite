import requests

url = "http://127.0.0.1:5000/anagrams"
data = {
    "strings": ["eat", "tea", "tan", "ate", "nat", "bat"]
}

response = requests.post(url, json=data)

print(f"Status Code: {response.status_code}")
print(f"Response JSON: {response.json()}")