from flask import Flask, request
import requests
import os

app = Flask(__name__)

ZAPIER_WEBHOOK_URL = os.environ.get("ZAPIER_WEBHOOK_URL")

@app.route("/evento", methods=["POST"])
def criar_evento():
    dados = request.json
    response = requests.post(ZAPIER_WEBHOOK_URL, json=dados)
    return {"status": "enviado para Zapier"}, response.status_code

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
