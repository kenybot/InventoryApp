# Run when ever to start a webserver.venv/
from website import create_app

app = create_app()

if __name__ == '__main__': #only if 
    app.run(debug=True)