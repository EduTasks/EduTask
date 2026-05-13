import requests

class DaoClient:
    def __init__(self):
        self.base_url = "http://localhost:5000/api"

    def login(self, username, password):
        try:
            response = requests.post(f"{self.base_url}/login", json={
                "username": username,
                "password": password
            })
            if response.status_code == 200:
                data = response.json()
                return data['data'] # Retorna el diccionari de l'usuari
            return None
        except requests.exceptions.ConnectionError:
            print("[-] Error: No es pot connectar amb el servidor EduTask.")
            return None

    def get_tasques(self):
        try:
            response = requests.get(f"{self.base_url}/tasques")
            if response.status_code == 200:
                return response.json()['data']
            return []
        except requests.exceptions.ConnectionError:
            return []