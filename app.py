from app import app

# Inicia o servidor no localhost na porta 3333
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3333, debug=True)