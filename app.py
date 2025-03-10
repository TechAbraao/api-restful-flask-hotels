from flask import Flask
from flask_restful import Api
from resources.hotel import Hoteis, Hotel

from dotenv import load_dotenv
import os
load_dotenv()

app = Flask(__name__)
diretorio = os.getenv("DATABASE_URL")
app.config['SQLALCHEMY_DATABASE_URI'] = diretorio
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
api = Api(app)

@app.before_request
def cria_banco():
    banco.create_all()

api.add_resource(Hoteis, "/hoteis")
api.add_resource(Hotel, "/hotel/<string:hotel_id>")

if __name__ == "__main__":
    from sql_alchemy import banco
    banco.init_app(app)
    app.run(port = 3030, host = '0.0.0.0', debug = True)