from flask import Flask, request
import requests

ESP32_IP = "http://192.168.1.12"  # Replace with your ESP32's IP

app = Flask(__name__)

@app.route("/speech", methods=["POST"])
def forward_speech():
    text = request.data.decode("utf-8")
    response = requests.post(f"{ESP32_IP}/speech", data=text)
    return response.text, response.status_code

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
