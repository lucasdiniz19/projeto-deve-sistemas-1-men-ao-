from dotenv import load_dotenv
load_dotenv()

from src.app import create_app

app = create_app()

from src.app import routes 

if __name__ == "__main__":
    app.run(debug=True, port=5001)
    

