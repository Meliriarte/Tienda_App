import customtkinter as ctk
from models.models import inicializar_bd
from views.main_view import MainView

def main():
    """Función principal que inicia la aplicación"""
    # Inicializar la base de datos
    inicializar_bd()
    
    # Iniciar la aplicación
    app = MainView()
    app.mainloop()

if __name__ == "__main__":
    main()    