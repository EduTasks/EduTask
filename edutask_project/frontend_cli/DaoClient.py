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
    
    def lliurar_tasca(self, id_tarea, id_alumno, ruta_arxiu_local):
        try:
            # Abrimos el archivo en modo lectura binaria ('rb')
            with open(ruta_arxiu_local, 'rb') as f:
                arxius = {'file': f}
                dades = {'id_tarea': id_tarea, 'id_alumno': id_alumno}
                
                # Hacemos el POST enviando el archivo y los IDs
                response = requests.post(f"{self.base_url}/entregar", files=arxius, data=dades)
                
            if response.status_code == 200:
                return True
            return False
            
        except FileNotFoundError:
            print("[-] Error: No s'ha trobat l'arxiu a la ruta que has indicat.")
            return False
        except requests.exceptions.ConnectionError:
            print("[-] Error: No es pot connectar amb el servidor EduTask.")
            return False