from DaoClient import DaoClient

class ViewConsole:
    def __init__(self):
        self.dao = DaoClient()
        self.current_user = None

    def iniciar(self):
        print("="*40)
        print("🎓 BENVINGUT A EDUTASK 🎓")
        print("="*40)
        
        while not self.current_user:
            self.menu_login()
            
        if self.current_user['id_role'] == 1:
            self.menu_professor()
        else:
            self.menu_alumne()

    def menu_login(self):
        print("\n--- INICI DE SESSIÓ ---")
        user = input("Usuari: ")
        pwd = input("Contrasenya: ")
        
        usuari_validat = self.dao.login(user, pwd)
        if usuari_validat:
            self.current_user = usuari_validat
            print(f"\n[+] Accés permès. Hola, {self.current_user['username']}!")
        else:
            print("\n[-] Usuari o contrasenya incorrectes. Torna-ho a provar.")

    def menu_alumne(self):
        while True:
            print("\n--- MENÚ ALUMNE ---")
            print("1. Veure Tasques Pendents")
            print("2. Lliurar Tasca")
            print("3. Sortir")
            opcio = input("Tria una opció: ")
            
            if opcio == '1':
                tasques = self.dao.get_tasques()
                print("\n--- TASQUES PUBLICADES ---")
                for t in tasques:
                    # Añadido el ID para que el alumno sepa qué tarea está entregando
                    print(f"[ID: {t['id']}] [{t['curso']}] {t['titulo']} - {t['descripcion']}")
                    
            elif opcio == '2':
                id_tasca = input("Introdueix l'ID de la tasca a lliurar: ")
                ruta = input("Introdueix la ruta del teu arxiu (ex: el_meu_treball.pdf): ")
                id_alumne = self.current_user['id'] # Sacamos el ID del alumno logueado
                
                print("[*] Pujant arxiu al servidor...")
                exito = self.dao.lliurar_tasca(id_tasca, id_alumne, ruta)
                
                if exito:
                    print("[+] Tasca enviada i guardada correctament!")
                else:
                    print("[-] Hi ha hagut un problema amb l'enviament de la tasca.")
                    
            elif opcio == '3':
                print("Fins aviat!")
                break

    def menu_professor(self):
        print("\n--- MENÚ PROFESSOR ---")
        print("Opcions de professor en desenvolupament per a l'Sprint 3...")
        # Aquí aniria la lògica del professor per posar notes

if __name__ == '__main__':
    app = ViewConsole()
    app.iniciar()