from flask import Flask
import settings as settings


app = Flask(__name__)

@app.route("/optimization")
def optimization():
    return settings.optimization

@app.route("/cleanup")
def cleanup():
    return settings.cleanup

@app.route("/telemetry")
def telemetry():
    return settings.telemetry

@app.route("/autoupdate")
def autoupdate():
    return settings.autoupdate

@app.route("/powerplan")
def powerplan():
    return settings.powerplan

@app.route("/activation")
def activation():
    return settings.activation

@app.route("/network")
def network():
    return settings.network

if __name__ == "__main__":
    app.run(debug=False)