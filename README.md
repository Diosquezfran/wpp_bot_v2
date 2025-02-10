1️⃣ Requisitos previos
Antes de comenzar, asegúrate de tener instalado en la nueva PC:

✅ Git → Para clonar el repositorio. Descargar Git
✅ Python 3.x → Para ejecutar el proyecto. Descargar Python
✅ PostgreSQL → Para la base de datos. Descargar PostgreSQL

2️⃣ Clonar el repositorio
Abre una terminal y ejecuta:

sh
Copiar
Editar
git clone https://github.com/TU_USUARIO/TU_REPOSITORIO.git
cd TU_REPOSITORIO
(Reemplaza TU_USUARIO y TU_REPOSITORIO con los datos correctos)

3️⃣ Crear y activar un entorno virtual
Es recomendable usar un entorno virtual para instalar las dependencias:

sh
Copiar
Editar
# Crear un entorno virtual (solo la primera vez)
python -m venv venv  

# Activar el entorno virtual:
# En Windows:
venv\Scripts\activate
# En macOS/Linux:
source venv/bin/activate
4️⃣ Instalar dependencias
Ejecuta:

sh
Copiar
Editar
pip install -r requirements.txt
Si el archivo requirements.txt no está en el repo, puedes generarlo con:

sh
Copiar
Editar
pip freeze > requirements.txt
y luego subirlo a GitHub.

5️⃣ Configurar la base de datos
Crea la base de datos en PostgreSQL con el mismo nombre que usaste en app.py:

sql
Copiar
Editar
CREATE DATABASE whatsapp_bot;
Configura las credenciales en app.py (si es necesario):

python
Copiar
Editar
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://USUARIO:CONTRASEÑA@localhost:5432/whatsapp_bot'
Ejecuta la migración para crear las tablas:

sh
Copiar
Editar
python
>>> from app import db
>>> from app import app
>>> with app.app_context():
>>>     db.create_all()
>>> exit()
6️⃣ Iniciar la aplicación
Corre el servidor Flask:

sh
Copiar
Editar
python app.py
Si ves "Running on http://127.0.0.1:5000/", ¡ya puedes probar la API en el navegador o con curl! 🎉

7️⃣ Probar que todo funciona
Ejecuta un curl para verificar la disponibilidad:

sh
Copiar
Editar
curl "http://127.0.0.1:5000/disponibilidad?negocio_id=1&fecha=2024-07-10"
Si todo está bien, recibirás un JSON con los horarios disponibles. 🚀
