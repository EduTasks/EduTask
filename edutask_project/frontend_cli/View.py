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
            print("2. Sortir")
            opcio = input("Tria una opció: ")
            
            if opcio == '1':
                tasques = self.dao.get_tasques()
                print("\n--- TASQUES PUBLICADES ---")
                for t in tasques:
                    print(f"[{t['curso']}] {t['titulo']} - {t['descripcion']}")
            elif opcio == '2':
                print("Fins aviat!")
                break

    def menu_professor(self):
        print("\n--- MENÚ PROFESSOR ---")
        print("Opcions de professor en desenvolupament per a l'Sprint 3...")
        # Aquí aniria la lògica del professor per posar notes

if __name__ == '__main__':
    app = ViewConsole()
    app.iniciar()