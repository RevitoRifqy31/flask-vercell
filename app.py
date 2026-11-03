from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>Halo dari Flask di Vercel!</h1>
    <p>Tugas Komputasi Awan - Rifky Alfansyah</p>
    <a href="/api/info">Lihat API</a>
    """

@app.route("/api/info")
def info():
    return jsonify({
        "nama": "Rifky Alfansyah",
        "mata_kuliah": "Komputasi Awan",
        "platform": "Vercel",
        "framework": "Flask"
    })

if __name__ == "__main__":
    app.run(debug=True)