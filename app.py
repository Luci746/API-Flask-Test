from app import createApp

app = createApp()

if __name__ == '__main__':
    try:
        app.run(debug=True)
    except Exception as e:
        print(f"Erro de Instância do Flask \n\t{e}")