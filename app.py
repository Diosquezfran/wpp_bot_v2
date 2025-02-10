from flask import Flask
# from flask_sqlalchemy import text
from sqlalchemy import text
from models import db  # Importa el objeto db de models.py
from routes import routes  # Importa el blueprint

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:Dylan574@localhost:5432/whatsapp_bot'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)  # Asegúrate de inicializar db con la app
app.register_blueprint(routes)  # Registra el blueprint

# @app.route('/test_db')
# def test_db():
#     try:
#         db.session.execute(text('SELECT 1'))  # Consulta simple de prueba
#         return "¡Conexión exitosa con la base de datos!"
#     except Exception as e:
#         return f"Error al conectar: {str(e)}"

# # Bloque para crear las tablas dentro del contexto de la app
# with app.app_context():
#     print("creando tablas")
#     db.create_all()

if __name__ == '__main__':
    app.run(debug=True)
