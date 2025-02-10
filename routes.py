from flask import Blueprint, request, jsonify
from models import db
from disponibilidad import consultar_disponibilidad  # Importa la función

routes = Blueprint("routes", __name__)

@routes.route("/disponibilidad", methods=["GET"])
def disponibilidad():
    negocio_id = request.args.get("negocio_id", type=int)
    fecha = request.args.get("fecha")

    if not negocio_id or not fecha:
        return jsonify({"error": "Faltan parámetros negocio_id y/o fecha"}), 400

    resultado = consultar_disponibilidad(negocio_id, fecha)
    return jsonify(resultado)
